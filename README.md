**SkillStack – Backend**

The backend of SkillStack is a RESTful API built with FastAPI and SQLAlchemy. It manages skill data, providing endpoints for creating, reading, updating, and deleting learning goals.

**Features**

- CRUD operations for skills:
  - Create new skill/learning goal
  - Retrieve all skills or a specific skill
  - Update an existing skill
  - Delete a skill
- Data persistence using SQLite
- CORS enabled to allow frontend communication
- Simple, self-contained API with Pydantic models for validation

**Setup Instructions**

Prerequisites

- Python ≥ 3.10
- pip (Python package manager)
- Optional: virtual environment (recommended)

**Steps**

1. Clone the repository

```bash
git clone <your-backend-repo-url>
cd skill-stack-backend
```


2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```


3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the development server
```bash
uvicorn main:app --reload
```

- The backend will be available at http://127.0.0.1:8000/
- Swagger UI docs: http://127.0.0.1:8000/docs

**API Endpoints**
| Method | Endpoint       | Description                  |
|--------|----------------|------------------------------|
| GET    | `/`            | Test endpoint, returns API status |
| POST   | `/skills`      | Create a new skill           |
| GET    | `/skills`      | Retrieve all skills          |
| GET    | `/skills/{id}` | Retrieve a skill by ID       |
| PUT    | `/skills/{id}` | Update a skill by ID         |
| DELETE | `/skills/{id}` | Delete a skill by ID         |

Skill Data Schema:
```json
{
  "id": 1,
  "skill_name": "React",
  "resource_type": "course",
  "platform": "Udemy",
  "status": "in-progress",
  "hours": 10,
  "notes": "Learning React basics",
  "difficulty": 3
}
```

**Tech Stack**

- Framework: FastAPI
- Database: SQLite
- ORM: SQLAlchemy
- Validation: Pydantic
- Server: Uvicorn
- CORS: FastAPI Middleware

**Frontend Connection**

The frontend connects to the backend API via axios in src/api.js:

```javascript
const API = axios.create({
  baseURL: "https://skill-stack-backend-production.up.railway.app",
});
```


Ensure the backend is running and accessible from the frontend.

📄 **License**

MIT License
