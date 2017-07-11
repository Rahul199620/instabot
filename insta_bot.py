
from delete_cmnt import delete_negative_comment
from selfinfo import self_info
from getuser_id import get_user_id
from get_userinfo import get_user_info
from post_id import get_post_id
from lika_post import like_a_post
from get_ownpost import get_own_post
from get_user_post import get_user_post
from comment_post import post_comment
from objective import wordcloud
def init_bot():
    #this list cotain users options
    option_list = ['\t\t\t\t*************************Welcome to instabot*****************************',
                   '1.Get your own details', '2..Get details of user by username', '3..get your own recent post',
                   '4..get recent post of user by username ', '5..Like most recent user post',
                   '6..make comment on user recent post ', '7..Delete negative comment from recent post',
                   '8..Create a word cloud of user activity from users posts','\t\t........write exit to leave instabot']

    instabot = True

    while instabot:



        select_option = int(raw_input("Enter your choice::"))

        try:


            select_option=select_option.upper()
            if select_option == 1:
                self_info()

            elif select_option == 2:
                insta_username = raw_input("Enter username: ")
                get_user_info(insta_username)

            elif select_option == 3:
                get_own_post()

            elif select_option == 4:
                insta_username = raw_input("Enter username::")
                get_user_post(insta_username)

            elif select_option == 5:
                insta_username = raw_input("Enter username::")
                like_a_post(insta_username)

            elif select_option == 6:
                insta_username = raw_input("Enter username::")
                post_comment(insta_username)

            elif select_option == 7:
                insta_username = raw_input("Enter Username::")
                delete_negative_comment(insta_username)

            elif select_option == 8:

                insta_username='shivam.walia'
                get_hash_tag(insta_username)


            elif select_option =='EXIT':
                 instabot=False


        except:
            print ("This is not valid option")



#calling insta bot function
init_bot()

