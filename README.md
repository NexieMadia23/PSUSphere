# PSUSphere

*PSUSphere* is a Django-based web application designed to manage university student organizations, colleges, academic programs, and student memberships. It provides a robust backend structure and a customized administrative interface for efficient data handling.

## Description

This project serves as a centralized platform for tracking student involvement in various campus organizations. It utilizes Django's powerful ORM to maintain relationships between:
* *Colleges* (e.g., College of Computing Studies)
* *Programs* (e.g., BS Computer Science)
* *Organizations* (e.g., Association of Computing Students)
* *Students* and their *Memberships*

The system allows administrators to easily create, read, update, and delete records, as well as generate dummy data for testing purposes.

## Key Features

* *Organization Management:* Track student organizations and their affiliated colleges.
* *Student Database:* Manage student profiles, including ID numbers and degree programs.
* *Membership Tracking:* Record which students belong to which organizations and when they joined.
* *Custom Admin Interface:*
    * *Search:* Quickly find students, organizations, or programs by name or description.
    * *Filters:* Filter lists by College or Join Date.
    * *Optimized Views:* Custom list displays for better readability.
* *Data Automation:* Includes a custom management command (create_initial_data) to populate the database with realistic fake data using the Faker library.

## Technology Stack

* *Python* (Backend Logic)
* *Django* (Web Framework)
* *SQLite* (Database)
* *Faker* (Data Generation)

## Installation & Setup

1.  *Clone the repository:*
    
    git clone [https://github.com/hvnnnn/PSUSphere.git](https://github.com/hvnnnn/PSUSphere.git)
    cd PSUSphere
    

2.  *Create and activate a virtual environment:*
    * Windows: python -m venv psusenv then psusenv\Scripts\activate
    * Mac/Linux: python3 -m venv psusenv then source psusenv/bin/activate

3.  *Install dependencies:*
    
    pip install -r requirements.txt
    

4.  *Apply database migrations:*
    
    cd projectsite
    python manage.py makemigrations
    python manage.py migrate
    

5.  *Create a superuser (Admin):*
    
    python manage.py createsuperuser
    

6.  *(Optional) Load initial data:*
    
    python manage.py create_initial_data
    

7.  *Run the server:*
    
    python manage.py runserver
    

## Usage

1.  Open your browser and navigate to: http://127.0.0.1:8000/admin/
2.  Log in using the superuser credentials you created.
3.  Navigate through the *Studentorg* section to manage Colleges, Organizations, and Students.

## Authors

* *[Norelyn Madia]* - Repository Owner
* *[Princess Heaven Rica]* - Collaborator

---
Rev 01 - August 2025
github.com
