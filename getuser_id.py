#get user id file is created
#import global variable
from constant import BASE_URL,Access_Token
import requests

def get_userid(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username,Access_Token)
    print( 'get request_url %s')%(request_url)
    user_info=requests.get(request_url).json()


