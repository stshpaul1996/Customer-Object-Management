# Customer Object Management Application

This application allows users to log in, manage customer information, and securely log out. The frontend is built with React, and the backend with Djano. JWT is used for secure authentication, and Docker is used for containerizing the app.

## Technologies Used
- **Frontend:** React.js
- **Backend:** Django Rest Framework
- **Database:** SQLite
- **Containerization:** Docker
- **Testing:** unittest, Coverage
- **API Documentation:** Swagger
- **Version Control:** Git and GitHub

## Features
- Secure login and logout using JWT.
- Input customer information (First name, Last name, Date of birth, Phone number).
- Store customer data safely in the database.
- Validate customer information on the frontend.
- Code coverage for the backend APIs.
- Fully containerized using Docker .

## Project Structure
- Customer-Object-Management/ 
- ├── backend/ 
- │ ├── backend/ 
- | ├── customer/  
- │ ├── Dockerfile 
- │ ├── requirements.txt 
- │ └── manage.py 
- ├── frontend/ 
- │ ├── src/ 
- │ ├── Dockerfile 
- │ └── package.json 
- └── docker-compose.yml

## Backend (Django)

### Setup

1. **Clone the Repository:**
   ```bash
   - git clone https://github.com/your-username/customer-management-app.git
   - cd customer-management-app/backend

2. **Set up Virtual Environment:**
    ```bash

    - python3 -m venv venv
    - source venv/bin/activate  #for linux systems
    - venv\Scripts\activate # foe Windows systems 

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

4. **To run server**:
    ```bash 
    python manage.py migrate
    python manage.py runserver
    username:- admin
    password:- admin

5. **Running Tests & Code Coverage**:
    ```bash 
    # Run the Development Server:
    python manage.py runserver
    Running Tests & Code Coverage

    # Run Unit Tests:
    python manage.py test

    # Run Tests with Coverage:
    coverage run --source='.' manage.py test
    coverage report -m
    

## Frontend (React)

### Setup

    ```bash

    cd ../frontend
    Install Dependencies:
    npm install

    Run the Development Server:
    npm start


## Design Patterns

### Backend (Django)

The core of the backend follows the  architecture:
- **Model:** Defines the structure of the customer data .
- **Serializer:** Handle data validation of incoming data.
- **View:** Handle incoming requests and return responses .

### Authentication (JWT)

- **JWT:** Used JWT for identifing the user and secure application.

### Containerization (Docker)

- **Docker:** Each component (frontend and backend) is containerized using Docker.

### Error Handling

- **Backend:** Throws exceptions for invalid input.
- **Frontend:** Displays user-friendly messages for failed login attempts or data validation errors.

## Assumptions and Decisions

### Assumptions
- **JWT for Authentication:** JWT is assumed to be the most secure and scalable method for authentication in this use case, where tokens can be issued and validated on the server.
- **Database:** Used SQLite for development and testing.

### Decisions
- **Frontend and Backend Separation:** Keeping the frontend and backend as separate applications allows for independent development and scaling. 
- **Use of Docker:** Docker was used to ensure that both frontend and backend can run in consistent environments for development .
- **React for UI:** chosen react for build dynamic , responsive application.
- **Error Handling Strategy:** To show error messages for login failures and invalid input.




    

