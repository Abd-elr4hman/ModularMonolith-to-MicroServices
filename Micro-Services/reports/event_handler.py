import json 

def handler(ch, method, properties, body):
    body = json.loads(body)
    print(f"recieved data {body}")
