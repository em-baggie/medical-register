<h1 align="center">Assignment 4: Medical Register Flask App</h1>

# Overview
The General Medical Council (GMC) holds a full register of qualified doctors. Each registered doctor holds a unique GMC number. This project is a simplified version consisting of a number of files creating a Flask app with client side and server side functionality, allowing the client to search for doctor by name/GMC number, register a doctor and remove a doctor from the register.<br>
- `/database/medical_register_db.sql` contains files with all the SQL code required to create a simple medical register database.
- `main.py` contains the client side functionality.
- `app.py` contains the core set up and routing of the app.
- `db_utils.py` contains the functions for interacting with the MySQL databse.

# How to run
1. Clone the CFG-Assignments repository by typing:
`git clone https://github.com/em-baggie/CFG-Assignments.git`.
2. Create a virtual environment in `/assignment-4` and install the app dependencies using `pip install -r requirements.txt`.
3. Open `/assignment-4/config.py` and set the values for the **"host"**, **"user"**, and **"password"** variables with your personal database connection information. 
4. Create the database by running `/assignment-4/database/medical_register_db.sql` in MySQLWorkbench.
5. Open a terminal and navigate to `/assignment-4`. Run the command `python3 app.py` to start an instance of the Flask application.
6. Open a separate terminal and navigate to `/assignment-4`. Run the command `python3 main.py` to run the app.
7. Follow the simple instructions on screen to navigate through the app.