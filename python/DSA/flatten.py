import json

# data = "/Users/yogeshkannan/Desktop/SysEng/python/ec2.json"
def flatten():
    new = {}
    file_open = open("/Users/yogeshkannan/Desktop/SysEng/python/ec2.txt")
    file_read = file_open.read()
    load_data = json.loads(file_read)
    print(type(load_data ['Reservations'][0]))
    # print(load_data['Reservations'][0]['Instances'][0]['Monitoring'])

    for x,y in load_data.items():
        if isinstance(y, dict):
            print(y) 
        else:
            flatten


flatten()