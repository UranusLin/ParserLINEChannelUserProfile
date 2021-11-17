import csv

import requests as re
import config


def call_line_get_userId():
    url = config.LINE_get_user_url + "?limit=1000"
    headers = {"Authorization": "Bearer " + config.line_access_token}
    user_list = []
    res = re.get(url, headers=headers).json()
    user_list = user_list + res.get("userIds")
    while res.get("next") is not None:
        res = re.get(url + "&start=" + res.get("next"), headers=headers).json()
        user_list = user_list + res.get("userIds")
    return user_list

def call_line_get_user_profile(profile_list, user_id):
    url = config.LINE_get_user_profile + user_id
    headers = {"Authorization": "Bearer " + config.line_access_token}
    res = re.get(url, headers=headers).json()
    profile_list.append(res)

def export_user_profile(profile_list):
    keys = profile_list[0].keys()

    with open('export/user_profile.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(profile_list)