from webull import paper_webull,webull
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    wb = loginWebull(True)
    print(wb.get_portfolio())

def loginWebull(paper = True):
    # Determine paper vs real trading
    if paper:
        wb = paper_webull()
    else:
        wb = webull()

    # Get environment variables and log in
    wb._set_did = os.getenv("DID")
    wb._access_token = os.getenv("ACCESS_TOKEN")
    wb.uuid = os.getenv("UUID")
    login_result = wb.login(os.getenv("LOGIN"),os.getenv("PASSWORD"), "Jaydon's Laptop", save_token=True)

    # Check that log in was successful
    if wb.is_logged_in():
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
        return None

    # Attempt to enable trading
    print('-----------------------------------')
    print('>>> Enable trading requested <<<')
    if wb.get_trade_token(os.getenv("PID")):
        print('Trading enabled, authentication passed')
    else:
        if wb.is_logged_in():
            print('Authentication failed, check PID again')
        else:
            print('Authentication failed, please log in again')
        return None
    return wb

if __name__ == "__main__":
    main()
