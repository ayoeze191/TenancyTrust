TenancyTrust is a simple backend API powering a mobile prototype that connects landlords and tenants in Nigeria. Built for Hack Sultan 2025, it focuses on property listings, mock trust scores (TenantScore), and digital rental agreements — all tailored to the Nigerian market.
🚀 Tech Stack

    Django + Django REST Framework

    Custom User Model (with phone, NIN, BVN, user type)

    Firebase (used by mobile app)

    JWT Authentication via djangorestframework-simplejwt

📦 Features
Feature	Description
🔐 Auth	Signup/login with user type (landlord/tenant), phone number, NIN, BVN
🏠 Listings	Landlords post properties; tenants can browse and filter
📊 TenantScore	Each tenant has a mock credit-like score (300–850)
📝 Agreements	Landlords and tenants store rental agreements in text format
🖼 Pictures	Landlords can attach images to listings
📁 API Structure
🔑 Auth

POST /api/register/   # signup with username, password, user_type, phone, etc.
POST /api/token/      # login (JWT)
POST /api/token/refresh/

🏘 Properties

GET /api/properties/       # list all
POST /api/properties/      # landlord only

📉 TenantScore

GET /api/tenant-score/<user_id>/   # get mock score

📜 Agreements

POST /api/agreements/   # landlord or tenant posts agreement
GET /api/agreements/    # view existing agreements

🛠️ Setup (Local)

# Clone and CD
git clone https://github.com/ayoeze191/tenancytrust-backend.git
cd tenancytrust-backend

# Create and activate virtualenv
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser

# Run server
python manage.py runserver

