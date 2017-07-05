#selfinfo function
import requests
from constant import Access_Token,BASE_URL

def self_info():
  request_url = (BASE_URL + 'users/self/?access_token=%s') % (Access_Token)
  print 'GET request url : %s' % (request_url)
  user_info =requests.get(request_url).json()
  print user_info
  print
