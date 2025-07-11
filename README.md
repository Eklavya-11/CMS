# 🍽️ Canteen Management System (CMS) 

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

A full-featured canteen management system built with Django that handles menu management, order processing, user roles, and inventory tracking.

![CMS Dashboard Preview](screenshots/dashboard.png)

## ✨ Key Features

### 🛠️ Admin Capabilities
- **Role-based access control** (Admin, Staff, Customer)
- **Menu management** - Add/update/delete items with images
- **Inventory tracking** with low-stock alerts
- **Sales analytics** dashboard

### 👥 User Experience
- **JWT-authenticated** login/signup
- **Real-time order tracking**:
  ```python
  STATUS_CHOICES = [
      ('PENDING', 'Pending'),
      ('IN_PREPARATION', 'In Preparation'), 
      ('COMPLETED', 'Completed')
  ]
  ```
- **Interactive menu** with search and filtering
- **Feedback system** with ratings (1-5 stars)

### 📊 Business Logic
- Automated billing system
- Inventory management
- Sales reporting (daily/weekly/monthly)

## 🚀 Technology Stack

| Category       | Technologies Used                              |
|----------------|-----------------------------------------------|
| **Backend**    | Django, Django REST Framework                 |
| **Database**   | MySQL (Production), SQLite (Development)      |
| **Frontend**   | HTML5, CSS3, JavaScript, jQuery               |
| **APIs**       | RESTful endpoints                             |
| **DevOps**     | Git, GitHub                                   |

## 🛠️ Installation Guide

### Prerequisites
- Python 3.8+
- MySQL Server
- Git

### Setup Instructions

1. Clone repository:

```bash
git clone https://github.com/Eklavya-11/CMS.git
cd CMS
```
2. Set up virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```python
pip install -r requirements.txt
```

4. Database setup:

```bash
mysql -u root -p
CREATE DATABASE canteen_db;
EXIT;
```

5. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create superuser:

```bash
python manage.py createsuperuser
```

7. Run development server:

```bash
python manage.py runserver
```

## 🔧 Configuration
Update `settings.py` with your database credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'canteen_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

## 📈 Future Improvements
- Integrate payment gateway (Stripe/Razorpay)
- Mobile app using React Native oR Flutter
- Real-time notifications with WebSockets
- Dockerize application

## 🤝 Contribution
Contributions are welcome! Please fork the repository and create a pull request.

## 📜 License
MIT License - Copyright (c) 2025 Eklavya11
