import requests
from config import settings
from models import Light
from hue_color import rgb_to_hue_xy, hue_xy_to_rgb

def groups():   
    url = f"{settings.hub_url}/api/{settings.username}"

    def is_group_a_room(group):
        if group[1]['type'] == 'Room':
            return True
        else:
            return False
        
    lights_request = requests.get(f"{url}/lights")
    groups_request = requests.get(f"{url}/groups")
    
    lights = lights_request.json()
    groups = groups_request.json()
    
    for k, v in lights.items():
        state = v['state']
        color = hue_xy_to_rgb(state['xy'][0], state['xy'][1], state['bri'] )
        lights[k] = {'id': k, 'name': v['name'], 'on': v['state']['on'], 'color': color}
        
    groups = dict(filter(is_group_a_room, groups.items()))

    for k, v in groups.items():
        room_lights = []
        for l in v['lights']:
            room_lights.append(lights[l])

        groups[k] = {'id': k, 'name': v['name'], 'lights': room_lights}        
       
    return groups        

def set(light: Light):
    payload = light.model_dump(exclude_unset=True)
    del payload['id']
    
    if (light.color is not None):
        color = rgb_to_hue_xy(light.color)
        payload['xy'] = color['xy']
        payload['bri'] = color['brightness']
        del payload['color']
        
    url = f"{settings.hub_url}/api/{settings.username}/lights/{light.id}/state"
    
    return  requests.put(url, json=payload).json();