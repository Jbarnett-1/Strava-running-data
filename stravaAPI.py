import json
import urllib3
import config

def get_strava_run_ids(id_num=10):
    auth_url = "https://www.strava.com/oauth/token"
    activites_url = "https://www.strava.com/api/v3/athlete/activities"
    payload = config.STRAVA_PAYLOAD
    # check if there is a new request token and print out
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()["access_token"]
    
    header = {"Authorization": "Bearer " + access_token}

    param = {"per_page": id_num, "page": 1}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()

    id_list = []
    for activity in my_dataset:
        id_list.append(activity.get("id"))
    return id_list

if __name__ == "__main__":
    ids = get_strava_run_ids()
    print(ids)
