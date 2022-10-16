import requests
import json

class public_ip:

    def get_ip():
        endpoint = 'https://ipinfo.io/json'
        response = requests.get(endpoint, verify=True)

        if response.status_code != 200:
            return 'Status:', response.status_code, 'Problem with the request. Exiting.'
            exit()

        data = response.json()
        
        ip = data['ip']

        print('--- public IP --- \n '+ ip + '\n ------------------')
        
        return ip


