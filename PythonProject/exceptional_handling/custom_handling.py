class LoginException(Exception):

    def __init__(self,msge):
        super().__init__(msge)

login = input("enter login_id:",)
password = input("enter password:",)

try:
    if login == "harsh" and password == "harsh":
        print("valid user")

    else:
        raise LoginException("invalid user")

except LoginException as e:
    print("exception:",e)