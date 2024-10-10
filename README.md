# Aspyr-Assignment-4
A React and Django-based web application to dynamically fetch and display clients by age range and gender. The frontend is built using React and styled with custom CSS, while the backend API is powered by Django. This project enables users to filter client data by gender and age, providing a smooth and interactive user experience.  
# Client Filtering Application

This project is a web-based application that allows users to filter and display client data by age range and gender. The frontend is built using **React** for dynamic interaction, and the backend API is developed using **Django**. Users can filter clients based on gender and age, and view the corresponding data in a table format.

## Features
- Dynamic filtering of clients by **gender** and **age range**.
- Responsive UI with styled components like buttons and tables.
- Real-time fetching of client data from the backend API.
- Error handling and loading states for a smooth user experience.

## Technologies Used
- **React** (Frontend)
- **Django** (Backend API)
- **Axios** (For API requests)
- **PostgreSQL** (Database)
- **CSS** (Custom styling for the UI)

## Project Structure
/client-app (React Frontend) - /src - App.js - /components - /services - styles.css

/server (Django Backend) - /api - /views.py - /serializers.py - /models.py - /urls.py - /config - /db.js - /seeds - seed_data.sql

markdown
Copy code

## How to Run the Project

### Prerequisites
- Node.js (for the frontend)
- Python (for the backend)
- PostgreSQL (for the database)

### PostgreSQL Setup

1. Install PostgreSQL and create a new database for the project.

   ```sql
   CREATE DATABASE aspyr_db;
Update the settings.py file in Django to connect to the PostgreSQL database:

python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aspyr_db',
        'USER': 'your_postgres_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Seed Data
We have included some initial seed data in the seeds/seed_data.sql file to populate the opt_party table. You can run the SQL file to add the seed data to your PostgreSQL database:

Run the seed file with the following command:

bash
Copy code
psql -U your_postgres_user -d aspyr_db -f server/seeds/seed_data.sql
This will insert predefined clients into the opt_party table to start with some data.

Backend Setup (Django)
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo.git
cd your-repo/server
Install the required Python dependencies:

bash
Copy code
pip install -r requirements.txt
Run migrations to create the necessary tables in your PostgreSQL database:

bash
Copy code
python manage.py migrate
Start the Django development server:

bash
Copy code
python manage.py runserver
Frontend Setup (React)
Navigate to the frontend directory:

bash
Copy code
cd client-app
Install the required dependencies:

bash
Copy code
npm install
Start the React development server:

bash
Copy code
npm start
The frontend will run on http://localhost:3000 by default.

API Endpoints
GET /api/genders/: Fetches the list of distinct genders.
GET /api/countByGender/
/: Fetches the count of clients by gender.
GET /api/clientsByAge/
/
/
/: Fetches clients filtered by age range and gender.
Credits
This project was developed collaboratively by:

Srikanth
Srithanmai
Kankala Sandeep
Nandhini SRGM
License
This project is licensed under the MIT License.

sql
Copy code

### **Explanation of the Updates**:
1. **PostgreSQL Setup**:
   - Added detailed instructions for setting up the PostgreSQL database.
   - Provided an example of how to update the Django `settings.py` file for PostgreSQL connection.

2. **Seed Data**:
   - Added instructions for seeding the database with initial data using the `seeds/seed_data.sql` file.
   - The SQL file contains sample data that can be used to begin with some clients in the `opt_party` table.

### Example **seed_data.sql** File:

Here is a sample of what the `seed_data.sql` file might look like:

```sql
INSERT INTO opt_party (pty_firstname, pty_lastname, pty_phone, pty_ssn, pty_gender, pty_age)
VALUES
('John', 'Doe', '555-1234', '123-45-6789', 'Male', 30),
('Jane', 'Doe', '555-9876', '987-65-4321', 'Female', 25),
('Charlie', 'Brown', '555-6789', '987-12-3456', 'Male', 40),
('Lisa', 'Smith', '555-4321', '543-21-9876', 'Female', 35),
('Michael', 'Johnson', '555-1212', '123-54-7890', 'Male', 45);
You can add more seed data as necessary.
```
Let me know if you need further adjustments or explanations!
