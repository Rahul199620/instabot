#import keyword is used for access various files
import requests
from constant import Access_Token,BASE_URL


from post_id import get_post_id
#function decleration for comment on post

userinfo="shivam.walia"

def post_comment(insta_username):
    media_id= get_post_id(insta_username)
    comment=raw_input("enter your comment")
    payload = {"access_token": Access_Token, "text": comment}
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)
    make_comment=requests.post(request_url,payload).json()

    if make_comment['meta']['data'] == 200:
        print('comment succsefully')
    else:
        print("no comment found")









