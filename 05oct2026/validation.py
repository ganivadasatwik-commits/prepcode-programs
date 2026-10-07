blocked=["raju","siddu","satwik"]
username=input("enter the username:")
if username not in blocked:
    print("username allowed")
else:
    print("username blocked")