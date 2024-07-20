from event_handler import handler
from channels import Channel

send_data = Channel('reports')
send_data.sub(handler)