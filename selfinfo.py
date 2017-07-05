#import requests library
import requests
#access global variables from constant.py file
from constant import Access_Token,BASE_URL

#selfinfo function
def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (Access_Token)
  print 'GET request url : %s' % (request_url)
  user_info =requests.get(request_url).json()


#access information of dictionary and conditions use
  if user_info['meta']['code'] == 200:
      if len(user_info['data']):
         print 'Username: %s' % (user_info['data']['username'])
         print 'No of followers: %s' % (user_info['data']['counts']['followed_by'])
         print 'No of people you are following: %s' % (user_info['data']['counts']['follows'])
         print 'No of posts: %s' % (user_info['data']['counts']['media'])
      else:
         print 'User does not exist'
  else:
    print 'Status code other than 200 received!'









