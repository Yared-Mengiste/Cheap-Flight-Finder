from data_manager import DataManager

print("Welcome to Yared's Flight Club.\nWe find the best flight deals and email you.\n")
reply = input("Would you like to sign up for the club? (y/n): ")
if reply == 'y':
  first_name = input("What is your first name? ")
  last_name = input("What is your last name? ")
  email = input("What is your email? ")
  email_confirm = input("Type your email again: ")
  if email == email_confirm:
    print("You're in the club!")
    data_manager = DataManager(bearer='itsmeyared', url='https://api.sheety.co/6df0a8cb3491ee21315b48dff783f802/flightDeals/users')
    parameter = {
      'user': {
        'fName': first_name,
        'lName': last_name,
        'email': email
      }
    }
    data_manager.post_to_query(parameter)
  else:
    print("Emails do not match. Please try again.")