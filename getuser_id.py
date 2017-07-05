#get user id file is created
#import global variable
from constant import BASE_URL ,Access_Token
#import requests library
import requests



#declaring function get user id
def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, Access_Token)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return own_media['data'][0]['id']

        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()






