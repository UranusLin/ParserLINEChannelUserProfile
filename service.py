from utils import call_line_get_userId, call_line_get_user_profile, export_user_profile


def get_channel_users():
    # get all user id
    user_list = call_line_get_userId()
    print("get users count: " + str(len(user_list)))
    count = 0
    profile_list = []
    # get all user profile form user id
    for i in user_list:
        call_line_get_user_profile(profile_list, i)
        count += 1
        if count % 100 == 0:
            print("get user count: " + str(count))
    print("total get " + str(len(profile_list)) + " user profile")
    print("export user profile to csv")
    # export user profile to csv
    export_user_profile(profile_list)
    print("All jobs done")