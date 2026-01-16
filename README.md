Employee CRUD API with JWT authentication

A RESTful API built with Django REST Framework to manage employees in a company.  
Developed as part of the Habot Hiring Project for the Python Backend Developer role.

---

🚀 Features
- Full CRUD operations for employees
- JWT authentication for secure access
- Validation (unique email, non-empty name)
- Error handling with proper HTTP status codes
- Pagination (10 employees per page)
- Filtering by department and role
- Unit tests for endpoints
- Clear documentation for setup and usage

---
## 📂 Project Structure

employee-crud-api/
├── employee_app/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── tests.py
│   └── urls.py
├── habotproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md

---
## 🛠 Tech Stack
- Python 3.10+
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt (JWT authentication)
- SQLite (default DB, can be swapped for MySQL/PostgreSQL)
- PyCharm / VS Code (development environment)
- Postman (API testing)
---

⚙️ Setup Instructions

1. Clone the repository
`bash
git clone https://github.com/PrajnaPradhan07/employee-crud-api.git
cd employee-crud-api
`

2. Create and activate virtual environment
`bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
`

3. Install dependencies
`bash
pip install -r requirements.txt
`

4. Apply migrations
`bash
python manage.py makemigrations
python manage.py migrate
`

5. Run the server
`bash
python manage.py runserver
`

---

🔑 Authentication

1. Obtain JWT token:
`http
POST /api/token/
{
  "username": "yourusername",
  "password": "yourpassword"
}
`

2. Add the token to Postman Authorization header:
`
Authorization: Bearer <your_token>
`

---

📌 API Endpoints

Create Employee
`http
POST /api/employees/
{
  "name": "John Doe",
  "email": "john@example.com",
  "department": "HR",
  "role": "Manager"
}
`
Response: 201 Created

---

List Employees
`http
GET /api/employees/
`
Supports:
- Pagination → ?page=2
- Filtering → ?department=HR or ?role=Developer

---

Retrieve Employee
`http
GET /api/employees/{id}/
`
Response: 200 OK or 404 Not Found

---

Update Employee
`http
PUT /api/employees/{id}/
{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "department": "Engineering",
  "role": "Developer"
}
`
Response: 200 OK

---

Delete Employee
`http
DELETE /api/employees/{id}/
`
Response: 204 No Content

---

⚠️ Error Handling

- 400 Bad Request → Validation errors (duplicate email, empty name)
- 404 Not Found → Invalid employee ID
- 201 Created → Successful creation
- 204 No Content → Successful deletion

---

🧪 Testing

Run unit tests:
`bash
python manage.py test employees
`

Covers:
- Create employee (201)
- Duplicate email (400)
- List employees (200 + pagination)
- Retrieve employee (200 / 404)
- Update employee (200)
- Delete employee (204)

---

✅ Conclusion
This project demonstrates RESTful principles, authentication, validation, error handling, pagination, filtering, testing, and documentation — fulfilling all Habot Hiring Project requirements.
`

---