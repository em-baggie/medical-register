import mysql.connector
from config import HOST, USER, PASSWORD

# functions for interacting with mySQL database

# create custom DatabaseError class
class DatabaseError(Exception):
    pass

# connect to mySQL database
def connect_to_db(db_name):
    cnx = None
    try:
        cnx = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
        )
        return cnx
    except Exception:
        raise DatabaseError

# find doctor by GMC number
def lookup_by_gmc_number(gmc_num):
    try:
        db_name = 'medical_register'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        query = f"""
        SELECT gmc_number, first_name, last_name, dob, gender, registration_date, last_date_of_revalidation
        FROM doctors doc
        JOIN dates d ON doc.gmc_number = d.doctor_gmc_number
        WHERE gmc_number = '{gmc_num}';
        """
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            raise DatabaseError
        cur.close()
        return result
    except Exception:
        raise DatabaseError

    finally:
        if db_connection:
            db_connection.close()

# find doctor by name
def lookup_by_name(first_name, last_name):
    try:
        db_name = 'medical_register'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        query = f"""
        SELECT gmc_number, first_name, last_name, dob, gender, registration_date, last_date_of_revalidation
        FROM doctors doc
        JOIN dates d ON doc.gmc_number = d.doctor_gmc_number
        WHERE first_name = '{first_name}' AND last_name = '{last_name}';
        """
        cur.execute(query)
        result = cur.fetchall()
        if not result:
            raise DatabaseError
        cur.close()
        return result
    except Exception:
        raise DatabaseError
    finally:
        if db_connection:
            db_connection.close()

# register new doctor
def register_dr(gmc_num, first_name, last_name, dob, gender, registration_date, last_date_of_revalidation):
    try:
        db_name = 'medical_register'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        queries = [(f"""INSERT INTO doctors
                        (gmc_number, first_name, last_name, dob, gender)
                        VALUES
                        ('{gmc_num}', '{first_name}', '{last_name}', '{dob}', '{gender}');;"""),
                   (f"""INSERT INTO dates
                        (doctor_gmc_number, registration_date, last_date_of_revalidation)
                        VALUES
                        ('{gmc_num}', '{registration_date}', '{last_date_of_revalidation}');""")]
        rows_affected = 0
        for query in queries:
            cur.execute(query)
            rows_affected += cur.rowcount
        db_connection.commit()
        cur.close()
        if not rows_affected == 2:
            raise Exception
    except Exception:
        raise DatabaseError
    finally:
        if db_connection:
            db_connection.close()

# remove doctor from the register
def remove_dr(gmc_num):
    try:
        db_name = 'medical_register'
        db_connection = connect_to_db(db_name)
        cur = db_connection.cursor()
        queries = [(f"DELETE FROM dates WHERE doctor_gmc_number = '{gmc_num}';"), (f"DELETE FROM doctors WHERE gmc_number = '{gmc_num}';")]
        rows_affected = 0
        for query in queries:
            cur.execute(query)
            rows_affected += cur.rowcount
        db_connection.commit()
        cur.close()
        if not rows_affected == 2:
            raise Exception
    except Exception:
        raise DatabaseError
    finally:
        if db_connection:
            db_connection.close()