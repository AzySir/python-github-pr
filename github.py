import os
import requests
import json

PULL_REQUEST_NUMBER = os.environ["SYSTEM_PULLREQUEST_PULLREQUESTNUMBER"]
REPO_NAME = os.environ["BUILD_REPOSITORY_NAME"]
OWNER = os.environ["OWNER"]
TOKEN = os.environ["TOKEN"]
URL = f'https://api.github.com/repos/{OWNER}/{REPO_NAME}/pulls/${PULL_REQUEST_NUMBER}/comments




def post():
    global URL
    payload = { "body": "Testing" }
    headers = { "Accept": "application/vnd.github+json" }
    # r = requests.post(URL, data=json.dumps(payload), headers=headers)
    r = requests.post(URL, json.dumps(payload), headers=headers)
    print(r)


# curl \
#   -X POST \
#   -H "Accept: application/vnd.github+json" \ 
#   -H "Authorization: token <TOKEN>" \
#   https://api.github.com/repos/OWNER/REPO/pulls/PULL_NUMBER/comments \
#   -d '{"body":"Great stuff!","commit_id":"6dcb09b5b57875f334f61aebed695e2e4193db5e","path":"file1.txt","start_line":1,"start_side":"RIGHT","line":2,"side":"RIGHT"}'

if __name__ == "__main__":
    post()