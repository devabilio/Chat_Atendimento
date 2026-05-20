Chat Service API 🚀

A RESTful API built with FastAPI + PostgreSQL + SQLAlchemy, focused on managing customer support conversations and messages.

This project was developed using a professional backend architecture based on:

MVC
Service Layer
Repository Pattern
JWT Authentication
SQLAlchemy ORM
PostgreSQL
✨ Features
👤 Users
User registration
JWT authentication
Password hashing with bcrypt
Secure token generation
📇 Contacts
Create contact
List contacts
Get contact by ID
Update contact
Delete contact
💬 Conversations
Create conversations
Update conversation status
List conversations
Contact relationship support
📨 Messages
Send messages
Retrieve messages by conversation
Conversation relationship support
📊 Dashboard Metrics

Application statistics:

Total contacts
Total conversations
Open conversations
Closed conversations
Total messages
🏗️ Project Structure
app/
│
├── auth/
│   ├── jwt_handler.py
│   └── security.py
│
├── config/
│   └── database.py
│
├── models/
│
├── repositories/
│
├── routes/
│
├── schemas/
│
├── services/
│
└── main.py
🛠️ Technologies Used
Backend
Python 3.12
FastAPI
SQLAlchemy
PostgreSQL
Pydantic
Security
JWT Authentication
Passlib
Bcrypt
Tools
Uvicorn
Swagger UI
Git & GitHub
🔐 JWT Authentication

The API uses JWT authentication to protect private routes.

Authentication flow:

Login → Token Generation → Authorized Access

Example response:

{
  "access_token": "eyJhbGciOi...",
  "token_type": "bearer"
}
⚙️ Installation
1. Clone the repository
git clone <YOUR_REPOSITORY_URL>
2. Navigate to the project folder
cd Chat_Atendimento
3. Create a virtual environment
python3 -m venv venv
4. Activate the virtual environment
Linux / macOS
source venv/bin/activate
Windows
venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
🐘 PostgreSQL Configuration

Configure your database connection inside:

app/config/database.py

Example:

DATABASE_URL = "postgresql://postgres:password@localhost/chat_service"
▶️ Running the Project
uvicorn app.main:app --reload
📚 Swagger Documentation

After starting the server:

http://127.0.0.1:8000/docs
📌 Main Endpoints
Users
Method	Endpoint
POST	/users/register
POST	/users/login
Contacts
Method	Endpoint
GET	/contacts
POST	/contacts
PUT	/contacts/{id}
DELETE	/contacts/{id}
Conversations
Method	Endpoint
GET	/conversations
POST	/conversations
PATCH	/conversations/{id}/status
Messages
Method	Endpoint
POST	/messages
GET	/messages/{conversation_id}
Dashboard
Method	Endpoint
GET	/dashboard/metrics
📈 Concepts Applied
Clean Architecture
SOLID Principles
Repository Pattern
Service Layer
REST API Design
ORM Relationships
JWT Security
Full CRUD Operations
Modular Architecture
Git Version Control
🚀 Future Improvements
Docker support
Alembic migrations
Automated tests
Deployment
WebSocket integration
Refresh tokens
Rate limiting
File upload support
👨‍💻 Author

Developed by Abilio Lopes Fachetti 🚀

⭐ Project Goal

This project was created to practice and improve:

professional backend development
scalable architecture
modern REST APIs
real-world backend concepts
Python backend portfolio development.