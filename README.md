# Project Setup

## Prerequisites
Before you begin, make sure you have the following installed on your system:
- Python: Required for the virtual environment and project dependencies.
- PostgreSQL: The project database.
- Chocolatey: Required to install make.
- Docker:

---

## Setup Instructions

To set up and run the project, follow these steps:




Configure Database Credentials
Update your PostgreSQL credentials in the following files:

    /alembic.ini: Replace the placeholders with your admin username and password.
    /settings.py: Ensure the database connection settings are accurate.

Install and Start Docker
Install make using Chocolatey. This step may require admin privileges:

choco install make

Once installed, start the Docker containers with:

make up



  

Notes and Troubleshooting

    If the make command is not found, ensure Chocolatey and make are correctly installed and added to your system PATH.
    Verify your PostgreSQL configuration if you encounter database connection issues.
    For any issues with migrations, double-check the settings in /alembic.ini and /settings.py.

    You will need to update cors in main.py if you run locally 
   
   
Feel free to reach out for support if you encounter any problems during setup.


    


