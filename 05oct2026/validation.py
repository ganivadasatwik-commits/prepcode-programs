blocked_usernames=["raju","siddu","satwik"]
username=input("enter the username:")
if username not in blocked_usernames:
    print("valid username")
else:
    print("invalid username")