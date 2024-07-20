
def receive_data_handler(sender, **kw):
    print(f"Caught signal from {sender!r}, data {kw!r}")
    return 'received!'
