from ..channels import Channel
from ..reports.event_handler import receive_data_handler

send_data = Channel('reports')

send_data.sub(receive_data_handler)