import requests
# from getpass import getpass

# #Get from the api
# auth_endpoint = "http://127.0.0.1:8000/auth/"
# username = input("Username:")
# password = getpass("Password:")

# auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password})
# print(auth_response.json())


# if auth_response.status_code == 200:
#     token = auth_response.json()['token']
#     headers = {
#         "Authorization": f"Token {token}"
#     }
#     endpoint = "http://127.0.0.1:8000/person/"

#     get_response = requests.get(endpoint, headers=headers)
#     print(get_response.json())


# const got = require("got");

# try {
#     "https://api.flutterwave.com/v3/payments", {
#         headers: {
#             Authorization: `Bearer ${process.env.FLW_SECRET_KEY}`
#         },
#         json: {
#             tx_ref: "hooli-tx-1920bbtytty",
#             amount: "100",
#             currency: "NGN",
#             redirect_url: "https://webhook.site/9d0b00ba-9a69-44fa-a43d-a82c33c36fdc",
#             meta: {
#                 consumer_id: 23,
#                 consumer_mac: "92a3-912ba-1192a"
#             },
#             customer: {
#                 email: "user@gmail.com",
#                 phonenumber: "080****4528",
#                 name: "Yemi Desola"
#             },
#             customizations: {
#                 title: "Pied Piper Payments",
#                 logo: "http://www.piedpiper.com/app/themes/joystick-v27/images/logo.png"
#             }
#         }
#     }).json();
# } catch (err) {
#     console.log(err.code);
#     console.log(err.response.body);
# }
import math
import random
import secrets
import string
redir_url = "https://www.google.com"
user_id = 3
user_contact = "0977230583"
user_name = "Cyprian Tembo"
N=3
st = str(math.floor(100 + random.random()*900)).join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(N))
#Post to the api
headers = {'Authorization': 'Bearer FLWSECK-bf656dbb7dc155aaef42fe57ac29f42c-X'}
endpoint = "https://api.flutterwave.com/v3/payments"
data = {
    "tx_ref": f"{st}",
            "amount": "2",
            "currency": "ZMW",
            "redirect_url": f"{redir_url}",
            "meta": {
                "consumer_id": f"{user_id}",
                "consumer_mac": "92a3-912ba-1192a"
            },
            "customer": {
                "email": "user@gmail.com",
                "phonenumber": f"{user_contact}",
                "name": f"{user_name}"
            },
            "customizations": {
                "title": "K2 Payment",
                "logo": "http://www.piedpiper.com/app/themes/joystick-v27/images/logo.png"
            }

}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())



'''
https://www.google.com/?status=cancelled&tx_ref={str}
'''


'''
{'status': 'success', 'message': 'Hosted Link', 'data': {'link': 'https://checkout.flutterwave.com/v3/hosted/pay/2a427825fd6b35066421'}}
'''


'''
{'status': 'success', 'message': 'Hosted Link', 'data': {'link': 'https://checkout.flutterwave.com/v3/hosted/pay/9f6658273884f92fd5ed'}}
'''


#Post to the api
# headers = {'Authorization': 'Token 83c90aee4be8a7dbbe146599e24aeac1d3ed633a'}
# endpoint = "http://127.0.0.1:8000/person/"
# data = {
#     "name": "Easther",
#     "career" :["Accountant"],
#      "city": "Chipata",
#      "gender": "Female",
#      "date_of_birth": "2000-05-05"

# }

# get_response = requests.post(endpoint, json=data, headers=headers)
# print(get_response.json())

