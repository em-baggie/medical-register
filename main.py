import json
import requests
from tabulate import tabulate
from datetime import datetime

# functions for sending HTTP requests, creating table and validating user input

def make_table(headers, entries):
    table = tabulate(entries, headers, tablefmt="psql") + "\n"
    return table

def lookup_by_gmc(gmc_num):
    json_response = requests.get(f'http://127.0.0.1:5001/find/{gmc_num}')
    result = json_response.json()
    if json_response.status_code == 200:
        headers = ["GMC number", "First name", "Last name", "Date of birth", "Gender", "Registration date", "Last date of revalidation"]
        result[0][3] = (datetime.strptime(result[0][3], "%a, %d %b %Y %H:%M:%S %Z")).strftime('%Y-%m-%d')
        result[0][5] = (datetime.strptime(result[0][5], "%a, %d %b %Y %H:%M:%S %Z")).strftime('%Y-%m-%d')
        result[0][6] = (datetime.strptime(result[0][6], "%a, %d %b %Y %H:%M:%S %Z")).strftime('%Y-%m-%d')
        table = make_table(headers, result)
        return f"\nResults:\n{table}"
    else:
        return f"{result["status"]}: {result["message"]}"

def lookup_by_name(first_name, last_name):
    json_response = requests.get(f'http://127.0.0.1:5001/find/name/{first_name}/{last_name}')
    result = json_response.json()
    if json_response.status_code == 200:
        headers = ["GMC number", "First name", "Last name", "Date of birth", "Gender", "Registration date", "Last date of revalidation"]
        result[0][3] = (datetime.strptime(result[0][3], "%a, %d %b %Y %H:%M:%S %Z")).strftime('%Y-%m-%d')
        result[0][5] = (datetime.strptime(result[0][5], "%a, %d %b %Y %H:%M:%S %Z")).strftime('%Y-%m-%d')
        result[0][6] = (datetime.strptime(result[0][6], "%a, %d %b %Y %H:%M:%S %Z")).strftime('%Y-%m-%d')
        table = make_table(headers, result)
        return f"\nResults:\n{table}"
    else:
        return f"{result["status"]}: {result["message"]}"
    
def register(gmc_num, first_name, last_name, dob, gender, registration_date, last_date_of_revalidation):
        new_dr = {
            'gmc_num': gmc_num,
            'first_name': first_name,
            'last_name': last_name,
            'dob': dob,
            'gender': gender,
            'registration_date': registration_date,
            'last_date_of_revalidation': last_date_of_revalidation
        }
        headers = {'content-type': 'application/json'}
        json_response = requests.post(
            'http://127.0.0.1:5001/register', headers=headers, data=json.dumps(new_dr)
        )
        return json_response.json()

def delete(gmc_num):
    headers = {'content-type': 'application/json'}
    json_response = requests.delete(
        f'http://127.0.0.1:5001/remove/{gmc_num}', headers=headers
    )
    return json_response.json()

def is_valid_gmc_num(gmc_num):
    return len(gmc_num) == 8 and gmc_num.isdigit()

def is_valid_first_name(first_name):
    return first_name.isalpha()

def is_valid_last_name(last_name):
    return last_name.isalpha()

def is_valid_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def is_valid_gender(gender):
    return 'M' or 'F'

# Client side function for running the app

def run():
    print("--------------------------------")
    print("Welcome to the medical register")
    print("--------------------------------")
    while True:
        print("Enter the corresponding letter to select an option in the menu.\n")
        print("Menu:")
        user_input = (input("a) Look up doctor by GMC number\nb) Look up doctor by name\nc) Register new doctor\nd) Remove doctor from the register\ne) Exit\n\n")).lower()

        if user_input == 'a':

            while True:
                gmc_num = input("\nPlease enter 8-digit GMC number:\n")
                if is_valid_gmc_num(gmc_num):
                    break
                else:
                    print("Error: invalid GMC number. GMC number must be 8 digits. Please try again.")
            response = lookup_by_gmc(gmc_num)
            print(response)

        elif user_input == 'b':

            while True:
                first_name = (input("\nPlease enter first name:\n")).lower()
                if is_valid_first_name(first_name):
                    break
                else:
                    print("Error: invalid name. Please try again.")

            while True:
                last_name = (input("\nPlease enter last name:\n")).lower()
                if is_valid_last_name(last_name):
                    break
                else:
                    print("Error: invalid name. Please try again.")

            response = lookup_by_name(first_name, last_name)
            print(response)
        
        elif user_input == 'c':

            while True:
                gmc_num = (input("\nPlease enter 8-digit GMC number:\n"))
                if is_valid_gmc_num(gmc_num):
                    break
                else:
                    print("Error: invalid GMC number. GMC number must be 8 digits. Please try again. Please try again.")

            while True:
                first_name = (input("\nPlease enter first name:\n")).lower()
                if is_valid_first_name(first_name):
                    break
                else:
                    print("Error: invalid name. Please try again.")

            while True:
                last_name = (input("\nPlease enter last name:\n")).lower()
                if is_valid_last_name(last_name):
                    break
                else:
                    print("Error: invalid name. Please try again.")

            while True:
                dob = (input("\nPlease enter date of birth in the format YYYY-MM-DD:\n"))
                if is_valid_date(dob):
                    break
                else:
                    print("Error: invalid date. Please enter date in the format YYYY-MM-DD.")
            
            while True:
                gender = (input("\nPlease enter gender (M/F)\n")).upper()
                if is_valid_gender(gender):
                    break
                else:
                    print("Error: invalid gender. Please enter M or F.")

            while True:
                registration_date = (input("\nPlease enter the date of registration in the format YYYY-MM-DD\n"))
                if is_valid_date(registration_date):
                    break
                else:
                    print("Error: invalid date. Please enter date in the format YYYY-MM-DD.")

            while True:
                last_date_of_revalidation = (input("\nPlease enter the date of revalidation in the format YYYY-MM-DD\n"))
                if is_valid_date(last_date_of_revalidation):
                    break
                else:
                    print("Error: invalid date. Please enter date in the format YYYY-MM-DD.")

            result = register(gmc_num, first_name, last_name, dob, gender, registration_date, last_date_of_revalidation)
            print(f"\n{result["status"]}: {result["message"]}")

        elif user_input == 'd':
            while True:
                gmc_num = (input("\nPlease enter 8-digit GMC number:\n"))
                if is_valid_gmc_num(gmc_num):
                    break
                else:
                    print("Error: invalid GMC number. GMC number must be 8 digits. Please try again.")
            
            result = delete(gmc_num)
            print(f"{result["status"]}: {result["message"]}")

        elif user_input =='e':
            break

        else:
            print("\nInvalid input. Please try again.\n")

if __name__ == '__main__':
    run()

