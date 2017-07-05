import requests
from constant import Access_Token,BASE_URL
from getuser_id import get_user_id


def get_user_post(insta_username):
  user_id = get_user_id(insta_username)
  if user_id == None:
    print 'User does not exist!'
    exit()
  request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, Access_Token)
  print 'GET request url : %s' % (request_url)
  user_media = requests.get(request_url).json()

  if user_media['meta']['code'] == 200:
      if len(user_media['data']):
          return user_media['data'][0]['id']
      else:
          print "There is no recent post!"
  else:
      print "Status code other than 200 received!"
  return None