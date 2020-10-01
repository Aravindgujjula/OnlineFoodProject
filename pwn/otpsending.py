import requests
import json

def sendASMS(contactno = "8897076760",message="Sorry Message not Available"):

    url = "https://www.fast2sms.com/dev/bulk"

    payload = "sender_id=FSTSMS&message="+message+"&language=english&route=p&numbers="+contactno


    headers = {
        'authorization': "ycBYUqgACtsNW2krnVE8mSZPxDboLH6XeMRf7G51J4TKFpjiwvSc8VqCk316orwYbH4OiltBpuZ2xeQP",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    #d1 = response.text
    return json.loads(response.text)
