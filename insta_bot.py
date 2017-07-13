
from delete_cmnt import delete_negative_comment
from selfinfo import self_info
from getuser_id import get_user_id
from get_userinfo import get_user_info
from post_id import get_post_id
from lika_post import like_a_post
from get_ownpost import get_own_post
from get_user_post import get_user_post
from comment_post import post_comment
from objective import get_hash_tag
import wordcloud
def init_bot():
    #this list cotain users options
    option_list = ['\t\t\t\t*************************Welcome to instabot*****************************',
                   'A.Get your own details', 'B..Get details of user by username', 'C..get your own recent post',
                   'D..get recent post of user by username ', 'E..Like most recent user post',
                   'F..make comment on user recent post ', 'G..Delete negative comment from recent post',
                   'H..Create a word cloud of user activity from users posts','\t\t........write exit to leave instabot']

    instabot = True

    while instabot:

        for x in range(0,len(option_list)):
            print option_list[x]+'\n'




        select_option = raw_input("Enter your choice::")

        try:


            select_option=select_option.upper()
            if select_option == 'A':
                self_info()

            elif select_option == 'B':
                insta_username = raw_input("Enter username: ")
                get_user_info(insta_username)

            elif select_option == 'C':
                get_own_post()

            elif select_option == 'D':
                insta_username = raw_input("Enter username::")
                get_user_post(insta_username)

            elif select_option == 'E':
                insta_username = raw_input("Enter username::")
                like_a_post(insta_username)

            elif select_option == 'F':
                insta_username = raw_input("Enter username::")
                post_comment(insta_username)

            elif select_option == 'G':
                insta_username = raw_input("Enter Username::")
                delete_negative_comment(insta_username)

            elif select_option == 'H':

                insta_username='shivam.walia'
                get_hash_tag(insta_username)


            elif select_option =='EXIT':
                 instabot=False


        except:
            print ("This is not valid option")



#calling insta bot function
init_bot()

