from constant import Access_Token,BASE_URL
import requests
from post_id import get_user_id




def post_comment(insta_username):
    media_id=get_user_id(insta_username)
    comment=raw_input("enter your comment")
    payload = {"access_token": Access_Token, "text": comment}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)
