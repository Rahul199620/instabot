#get user info file is created
#import global variable
from constant import Access_Token , BASE_URL
import requests
def get_user_info(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, Access_Token)
  print 'GET request url : %s' % (request_url)
  user_info = requests.get(request_url).json()