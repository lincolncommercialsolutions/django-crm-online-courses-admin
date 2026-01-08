# Customer 360 - CRM Platform

A modern Customer Relationship Management (CRM) platform built with Django and Bootstrap 5.

## Features

✅ **Customer Management**
- Add, view, and manage customer information
- Store customer details (name, email, phone, address)
- View all customers in an organized table

✅ **Interaction Tracking**
- Record customer interactions across multiple channels
- Track interaction direction (inbound/outbound)
- Supported channels: Email, Phone, Chat, Social Media, In Person
- View interaction summaries and analytics

✅ **Analytics Dashboard**
- View interaction statistics for the last 30 days
- Breakdown by channel and direction
- Total interaction count

✅ **Modern UI/UX**
- Responsive Bootstrap 5 design
- Clean and intuitive interface
- Gradient backgrounds and smooth animations
- Mobile-friendly layout

## Fixed Issues

1. ✅ Created missing `models.py` with Customer and Interaction models
2. ✅ Reorganized project structure correctly
3. ✅ Fixed import errors in views.py
4. ✅ Created proper Django project files (wsgi.py, asgi.py, urls.py)
5. ✅ Updated templates with modern Bootstrap 5 design
6. ✅ Enhanced CSS with gradient backgrounds and animations
7. ✅ Added admin panel configuration
8. ✅ Created and applied database migrations
9. ✅ Added proper navigation with icons

## Project Structure

```
customer360/
├── customer360/              # Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML templates
│   │   ├── base.html       # Base template
│   │   ├── index.html      # Customer list
│   │   ├── add.html        # Add customer
│   │   ├── interact.html   # Record interaction
│   │   └── summary.html    # Analytics
│   ├── models.py           # Data models
│   ├── views.py            # View functions
│   ├── admin.py            # Admin configuration
│   ├── urls.py             # URL routing
│   └── settings.py         # Django settings
├── static/                  # Static files
│   └── css/
│       └── main.css        # Custom styles
└── manage.py               # Django management script
```

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Django 4.2+

### Running the Application

The application is already set up and running! It's accessible at:

**🌐 http://127.0.0.1:8000/**

### Admin Panel Access

Access the Django admin panel at **http://127.0.0.1:8000/admin**

- **Username:** admin
- **Password:** admin123

### Available URLs

- **Home (Customer List):** http://127.0.0.1:8000/
- **Add Customer:** http://127.0.0.1:8000/create
- **Interaction Summary:** http://127.0.0.1:8000/summary
- **Admin Panel:** http://127.0.0.1:8000/admin

## Usage Guide

### Adding a Customer

1. Click "New Customer" in the navigation or the green button
2. Fill in the customer details:
   - Name
   - Email
   - Phone
   - Address
3. Click "Add Customer"

### Recording an Interaction

1. From the customer list, click "Interact" button next to a customer
2. Select the communication channel
3. Select the direction (Inbound/Outbound)
4. Enter a summary of the interaction
5. Click "Save Interaction"

### Viewing Analytics

1. Click "Summary" in the navigation
2. View interaction breakdown by channel and direction
3. See total interaction count for the last 30 days

## Technology Stack

- **Backend:** Django 6.0.1
- **Frontend:** Bootstrap 5.3, Bootstrap Icons
- **Database:** SQLite3
- **Python:** 3.12.3

## UI/UX Improvements

- Modern gradient background (purple to blue)
- Card-based layout with hover effects
- Smooth animations and transitions
- Bootstrap Icons for visual clarity
- Responsive design for all devices
- Clean and professional color scheme
- Improved form layouts with better spacing
- Alert messages for user feedback

## Development

To stop the server, press `CONTROL-C` in the terminal.

To restart the server:
```bash
cd /home/linkl0n/cert-projects/imbdevproject/home/project/customer360
/home/linkl0n/cert-projects/imbdevproject/.venv/bin/python manage.py runserver
```

## Database Models

### Customer
- id (auto-generated)
- name (CharField)
- email (EmailField)
- phone (CharField)
- address (TextField)
- created_at (DateTimeField)
- updated_at (DateTimeField)

### Interaction
- id (auto-generated)
- customer (ForeignKey to Customer)
- channel (CharField with choices)
- direction (CharField with choices)
- summary (TextField)
- interaction_date (DateTimeField)

---

**Project Status:** ✅ Ready for use!
**Server Status:** 🟢 Running at http://127.0.0.1:8000/
