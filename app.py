
from flask import Flask, jsonify, request
from db_utils import lookup_by_gmc_number, lookup_by_name, remove_dr, register_dr, DatabaseError

app = Flask(__name__)

# find by GMC number
@app.route('/find/<gmc_num>', methods = ['GET'])
def lookup_by_gmc_num(gmc_num):
    try:
        res = lookup_by_gmc_number(gmc_num)
        return jsonify(res), 200
    except DatabaseError:
        return jsonify({"status": "Unsuccessful", "message": f"A database error occurred or GMC number could not be found.\n"}), 500
    except Exception:
        return jsonify({"status": "Unsuccessful", "message": f"A routes error occurred.\n"}), 500
    
# look up by names
@app.route('/find/name/<first_name>/<last_name>')
def lookup_by_doc_name(first_name, last_name):
    try:
        res = lookup_by_name(first_name, last_name)
        return jsonify(res), 200
    except DatabaseError:
        return jsonify({"status": "Unsuccessful", "message": f"A database error occurred or name could not be found.\n"}), 500
    except Exception:
        return jsonify({"status": "Unsuccessful", "message": f"A routes error occurred.\n"}), 500
    
# remove doctor
@app.route('/remove/<gmc_num>', methods = ['GET','DELETE'])
def delete_dr(gmc_num):
    try:
        remove_dr(gmc_num)
        return jsonify({"status": "Successful", "message": f"Doctor with GMC number {gmc_num} removed.\n"})
    except DatabaseError:
        return jsonify({"status": "Unsuccessful", "message": f"A database error occurred or GMC number could not be found.\n"})
    except Exception:
        return jsonify({"status": "Unsuccessful", "message": f"A routes error occurred.\n"})

# register doctor
@app.route('/register', methods=['POST'])
def register():
    try:
        reg = request.get_json()
        register_dr(
            gmc_num = reg['gmc_num'],
            first_name = reg['first_name'],
            last_name = reg['last_name'],
            dob = reg['dob'],
            gender = reg['gender'],
            registration_date = reg['registration_date'],
            last_date_of_revalidation = reg['last_date_of_revalidation']
        )
        return jsonify({"status": "Successful", "message": f"Registration completed.\n"})
    except DatabaseError:
        return jsonify({"status": "Unsuccessful", "message": f"A database error occurred.\n"})
    except Exception:
        return jsonify({"status": "Unsuccessful", "message": f"A routes error occurred.\n"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)