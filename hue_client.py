import requests
from config import settings
from models import Light


def groups():   
    url = f"{settings.hub_url}/api/{settings.username}"

    def is_group_a_room(group):
        print(group[1]['type'])
        print(type(group))
        if group[1]['type'] == 'Room':
            return True
        else:
            return False
        
    lights_request = requests.get(f"{url}/lights")
    groups_request = requests.get(f"{url}/groups")
    
    lights = lights_request.json()
    groups = groups_request.json()
    
    for k, v in lights.items():
        lights[k] = {'id': k, 'name': v['name'], 'on': v['state']['on'], 'bri': v['state']['bri'],'sat': v['state']['sat'], 'hue': v['state']['hue']}
        
    groups = dict(filter(is_group_a_room, groups.items()))

    for k, v in groups.items():
        room_lights = []
        for l in v['lights']:
            print(lights[l], type(lights[l]))
            room_lights.append(lights[l])

        groups[k] = {'id': k, 'name': v['name'], 'lights': room_lights}        
       
    return groups        

def set(light: Light):
    payload = light.model_dump(exclude_unset=True)

    url = f"{settings.hub_url}/api/{settings.username}/lights/{light.id}/state"
    
    return  requests.put(url, json=payload).json();