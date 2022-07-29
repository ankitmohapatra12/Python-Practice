
org_str = input("Enter a String : ")

if(org_str.lower() == org_str.lower()[::-1]):
    print(org_str,"--> is palindrone")
else:
    print(org_str,"--> is not palindrone")