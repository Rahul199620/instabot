#get_own_post is intialized

from constant import Access_Token,BASE_URL
import requests

#function is declared
def get_own_post():
  request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (Access_Token)
  print 'GET request url : %s' % (request_url)
  own_media = requests.get(request_url).json()

  if own_media['meta']['code']== 200:
      if len(own_media['data']):
          return own_media['data'][0]['id']
      else:
          print "no post is found"

  else:
      print"error 404 found"



