"""
Modern Python features:
- TypeVar for generics
- Protocol for structural subtyping
- Machine learning integration
- Advanced collections
"""
from typing import Protocol, TypeVar, Generic
from collections import defaultdict, Counter
import numpy as np
from sklearn.neighbors import NearestNeighbors

T = TypeVar('T', bound='RecommendableItem')

class RecommendableItem(Protocol):
    id: int
    tags: list[str]
    
class RecommendationEngine(Generic[T]):
    def __init__(self, items: list[T]):
        self.items = items
        self._build_index()
        
    def _build_index(self) -> None:
        """Create vector embeddings from tags"""
        all_tags = {tag for item in self.items for tag in item.tags}
        self.tag_index = {tag: idx for idx, tag in enumerate(all_tags)}
        
        vectors = []
        for item in self.items:
            vec = np.zeros(len(self.tag_index))
            for tag in item.tags:
                vec[self.tag_index[tag]] = 1
            vectors.append(vec)
            
        self.model = NearestNeighbors(n_neighbors=3, metric='cosine')
        self.model.fit(vectors)
    
    def recommend(self, liked_items: list[int]) -> list[T]:
        """Find similar items using KNN"""
        liked_tags = Counter(tag for item_id in liked_items 
                           for item in self.items if item.id == item_id
                           for tag in item.tags)
        
        query_vec = np.zeros(len(self.tag_index))
        for tag, count in liked_tags.items():
            query_vec[self.tag_index[tag]] = min(count, 1)  # Binary weighting
            
        _, indices = self.model.kneighbors([query_vec])
        return [self.items[i] for i in indices[0]]
