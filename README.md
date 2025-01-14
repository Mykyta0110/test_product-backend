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

1. Create a Virtual Environment  
   Create a Python virtual environment by running:
   ```bash
   python -m venv .venv

Activate the virtual environment before proceeding.

    Install Project Dependencies
    With the virtual environment activated, install the required Python packages:

pip install -r requirements.txt

Configure Database Credentials
Update your PostgreSQL credentials in the following files:

    /alembic.ini: Replace the placeholders with your admin username and password.
    /settings.py: Ensure the database connection settings are accurate.

Install and Start Docker
Install make using Chocolatey. This step may require admin privileges:

choco install make

Once installed, start the Docker containers with:

make up

Apply Migrations
Set up the database schema by applying migrations:

    alembic upgrade head

Notes and Troubleshooting

    If the make command is not found, ensure Chocolatey and make are correctly installed and added to your system PATH.
    Verify your PostgreSQL configuration if you encounter database connection issues.
    For any issues with migrations, double-check the settings in /alembic.ini and /settings.py.

Feel free to reach out for support if you encounter any problems during setup.

Add sql script with data
INSERT INTO products (id, name, price)
VALUES
    (1, 'Laptop', 1200),
    (2, 'Headphones', 80),
    (3, 'Keyboard', 45),
    (4, 'Mouse', 25),
    (5, 'Monitor', 200);



