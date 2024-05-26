import requests

def check_internet():

    url='http://www.google.com/'

    timeout=5
    
    try:
        a = requests.get(url, timeout=timeout)
        print("We are Connected to the internet.")
        return True
    
    except requests.ConnectionError:
    
        print("İnternet Not Connected.")
    
    return False

check_internet()    