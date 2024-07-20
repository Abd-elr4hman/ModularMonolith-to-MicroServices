from fastapi import FastAPI
from .channels import Channel

app = FastAPI()

@app.get("/report")
def start_report_generation():
    send_data = Channel("reports")

    body = {
        'data_field_1': "blabla",
        'data_field_2': "tratraa"
    }
    
    send_data.pub(sender="aa", body=body)
    
    return {"details": "Report generatio started!"}

