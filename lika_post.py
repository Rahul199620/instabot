#like a post file is created
import requests
from constant  import  Access_Token,BASE_URL
from post_id import get_post_id
def like_a_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/likes') % (media_id)
    payload = {"access_token": Access_Token}
    print 'POST request url : %s' % (request_url)
    post_a_like = requests.post(request_url, payload).json()

    if  post_a_like['meta']['code'] == 200:
        print 'Like was successful!'
    else:
        print 'Your like was unsuccessful. Try again!'
