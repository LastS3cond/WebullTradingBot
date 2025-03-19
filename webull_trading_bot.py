from webull import paper_webull
from dotenv import load_dotenv
import os

load_dotenv()
wb = paper_webull()
wb._set_did = os.getenv("DID")
wb._access_token = os.getenv("ACCESS_TOKEN")
wb.uuid = os.getenv("UUID")
login_result = wb.login(os.getenv("LOGIN"),os.getenv("PASSWORD"), "Jaydon's Laptop", save_token=True)
response = wb.is_logged_in()
if response:
    account_id = wb.get_account_id()
    account_type = wb.get_account_type(os.getenv("LOGIN"))
    print('-----------------------------------')
    print('>>>>>>   Log in successful   <<<<<<')
    print(f'>>>   Your login ID: {account_id}   <<<')
    print(f'>>>   Your account type ID: {account_type}   <<<')
else:
    print('-----------------------------------')
    print('>>> Log in failed, authentication failed, check info below: ')
    print(login_result)

response = wb.get_trade_token(os.getenv("PID"))
print('-----------------------------------')
print('>>> Enable trading requested <<<')
if response:
    print('Trading enabled, authentication passed')
else:
    if wb.is_logged_in():
        print('Authentication failed, check PID again')
    else:
        print('Authentication failed, please log in again')
