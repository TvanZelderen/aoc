def parse_int(data):
    return [int(x) for x in data.split('\n') if x.strip()]

def parse_str(data):
    return [str(x) for x in data.split('\n') if x.strip()]
