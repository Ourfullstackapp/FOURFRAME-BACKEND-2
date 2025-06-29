This is the backend for the Movie Web App. It allows users to sign up, log in, see movies, and post reviews. It is built using Python and Flask.


# FOURFRAME-BACKEND-2
# Flask Auth API

A RESTful Flask API for user registration, authentication using JWT, and profile management. Built with SQLite/PostgreSQL, SQLAlchemy, and Flask extensions.

---

##  Tech Stack 

- **Backend:** Flask, Flask SQLAlchemy, Flask-JWT-Extended
- **Database:** SQLite (default), can be configured for PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)

---

##  Project Structure

project/
│
├── app/
│ ├── init.py
│ ├── models.py
│ ├── routes/
│ │ ├── auth_routes.py
│ │ └── profile_routes.py
│ ├── utils.py
│
├── config.py
├── run.py
└── requirements.txt

yaml
Copy
Edit

---

##  Features

###  User Management

- **Register:** `POST /api/register`  
  Create a new user with username, hashed password, and email.

- **Login:** `POST /api/login`  
  Authenticate and receive a JWT access token.

- **Get Profile:** `GET /api/profile` *(Protected)*  
  Retrieve user’s profile information using JWT.

- **Update Profile:** `PUT /api/profile` *(Protected)*  
  Modify name, email, or other profile fields.

---

##  Installation & Setup
To have access to this project:

### 1. Clone the repository

```bash
git clone https://github.com/your-username/flask-auth-api.git
cd flask-auth-api
2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the app
bash
Copy
Edit
python run.py
The app will be available at http://localhost:5000.

 Environment Variables (Optional)
Create a .env file and define:

env
Copy
Edit
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
JWT_SECRET_KEY=your-jwt-secret
DATABASE_URL=sqlite:///db.sqlite3
 API Endpoints
Method	Endpoint	Description	Auth Required
POST	/api/register	Register a new user	
POST	/api/login	Login and get JWT	
GET	/api/profile	Get user profile	
PUT	/api/profile	Update user profile	

 Example Request: Register
http
Copy
Edit
POST /api/register
Content-Type: application/json

{
  "username": "bobby",
  "email": "shmurda@gmail.com",
  "password": "secure123"
}
 JWT Auth Flow
Register or login to receive a JWT token.

For protected routes, include the token in headers:

makefile
Copy
Edit
Authorization: Bearer <token>
 Testing
Use Postman or Curl to test endpoints. Make sure to attach JWT to protected routes.

 Notes
You can easily switch to PostgreSQL by updating the DATABASE_URL in .env.

Passwords are hashed using werkzeug.security.

👨 Author
Built by George. Contributions welcome!