# Uz_RentCar
📘 Introduction and Information

Car Rental API — bu mashinalarni ijaraga olish tizimi uchun backend API loyihasi.
Foydalanuvchilar ro‘yxatdan o‘tishlari, mashinalarni ko‘rishlari va ijaraga olishlari mumkin.
Admin foydalanuvchilari esa mashinalarni, foydalanuvchilarni va buyurtmalarni boshqarishlari mumkin.

🧩 Models
Car
Field	Type	Description
id	int	Primary key
brand	str	Car brand (e.g. Toyota)
model	str	Car model (e.g. Camry)
price_per_day	float	Price per day in USD
engine_type	str	Engine type (e.g. V6, Electric)
fuel_type	str	Fuel type (petrol, diesel, electric, hybrid)
transmission	str	Transmission type (automatic / manual)
shape_type	str	Body type (SUV, sedan, coupe, etc.)
doors	int	Number of doors
seats	int	Number of seats
air_condition	bool	Has air conditioning or not
distance	int	Mileage (km)
equipments	str	List of available equipments/features
year	int	Year of manufacture
available	bool	Is the car available for rent
location	str	Car location
images	List[str]	List of image URLs
User
Field	Type	Description
id	int	Primary key
email	str	User email
password	str	Hashed password
phone	str	Phone number
name	str	Full name
role	str	Role (admin/user)
is_active	bool	Is account active
created_at	datetime	Account created time
updated_at	datetime	Last updated time
Order
Field	Type	Description
id	int	Primary key
car_id	int	Foreign key to Car
user_id	int	Foreign key to User
order_date	date	Rental start date
end_date	date	Rental end date
total_price	float	Total rental price
status	str	Order status (pending, approved, cancelled, completed)
payment_status	str	Payment status (pending, paid, refunded)
returned	bool	Car returned or not
created_at	datetime	Order created time
updated_at	datetime	Last updated time
🌐 API Endpoints
Auth
Method	Endpoint	Description
POST	/auth/register	Register a new user
POST	/auth/login	User login and token generation
Cars
Method	Endpoint	Description
GET	/cars/	Get all cars
GET	/cars/{id}	Get car by ID
POST	/cars/	Create new car (admin only)
PUT	/cars/{id}	Update car info (admin only)
DELETE	/cars/{id}	Delete car (admin only)
Orders
Method	Endpoint	Description
POST	/orders/	Create new order
GET	/orders/	Get user’s orders
GET	/orders/{id}	Get order details
PUT	/orders/{id}/cancel	Cancel order
PUT	/orders/{id}/return	Mark car as returned (admin only)
⚙️ Installation and Setup
# 1. Clone repository
git clone https://github.com/your-username/car-rental-api.git
cd car-rental-api

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # on Windows -> venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the server
uvicorn main:app --reload

🧪 Example Requests

POST /auth/register

{
  "email": "user@example.com",
  "password": "password123",
  "name": "John Doe",
  "phone": "+998901234567"
}


POST /orders/

{
  "car_id": 1,
  "order_date": "2025-10-15",
  "end_date": "2025-10-20"
}

🏗️ Tech Stack

Python 3.11+

FastAPI

SQLAlchemy

PostgreSQL

JWT Authentication

👨‍💻 Roles

Admin: Mashinalar va buyurtmalarni boshqaradi

User: Mashinalarni ko‘rish va ijaraga olish imkoniga ega

📅 Future Plans

Payment API integratsiyasi (Stripe, Payme, Click)

Car rating/review tizimi

Image upload (S3 yoki Cloudinary)

Email/SMS notificationlar