# Django Portfolio

Welcome to my Django Portfolio! This project showcases my skills and projects using Django, a high-level Python web framework.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [API Testing](#api-testing)

## Features

- Responsive design
- User authentication
- Project showcase
- Blog section
- Contact form

## Installation

To get a local copy up and running, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/apitongcm/Django-portfolio.git

2. Navigate to the project directory:
    ```bash
   cd Django-portfolio
    
3. Create virtual environment:
     ```bash
   python -m venv venv
     
4. Activate the virtual environment (On Windows):
     ```bash
   venv\Scripts\activate
     
5. Install the required packages:
     ```bash
   pip install -r requirements.txt
     
6. Run the migrations:
     ```bash
   python manage.py migrate
     
7. Start the development server:
     ```bash
   python manage.py runserver
     
8. Start the development server:
    Open your browser and go to http://127.0.0.1:8000/

##api-testing
Performing API testing
since I've set that anyone can view the data or set it in public it doesn't require any authentication.
<img width="1378" height="332" alt="image" src="https://github.com/user-attachments/assets/814908a5-dacd-40b2-8d12-24ef989f6dda" />

For POST, I've set that only the me can alter and post data so it requires a token for authentication 
<img width="1405" height="445" alt="image" src="https://github.com/user-attachments/assets/280e2a07-cb44-4764-9383-10f04f25b026" />


