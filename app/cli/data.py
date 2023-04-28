import base64
import jsonwebtoken as jwt
import hashlib
import json

import httpx
from time import time

from prettytable import PrettyTable

class Data():
    def __init__(self, parameter: object):
        config = open('config.json')
        data = json.load(config)
        self.__base_url = data['base_url']
        self.__app_id = data['application_id']
        self.__api_key = data['api_key']
        self.__product_agent_api_path = data['product_agent_api_path']
        self.headers = parameter['headers'] if 'headers' in parameter else ''
        self.query = parameter['query'] if 'query' in parameter else ''
        self.body = parameter['body'] if 'body' in parameter else ''
        self.http_method = parameter['http_method'] if 'http_method' in parameter else 'GET'
        
    @property
    def raw_url(self):
        return self.__product_agent_api_path + self.query
    
    @property
    def url(self):
        return self.__base_url + self.raw_url
    
    def __create_checksum(self, http_method: str):
        string_to_hash = f"{http_method.upper()}|{self.raw_url.lower()}|{self.headers}|{self.body}"
        hash_object = hashlib.sha256(str.encode(string_to_hash))
        base64_string = base64.b64encode(hash_object.digest()).decode('utf-8')
        return base64_string

    def __create_jwt_token(self, http_method: str, iat=time(), algorithm='HS256', version='V1'):
        checksum = self.__create_checksum(http_method)
        payload = {
        'appid': self.__app_id,
        'iat': iat,
        'version': version,
        'checksum': checksum
        }
        token = jwt.encode(payload, self.__api_key, algorithm=algorithm)
        return token
    
    def fetch_data(self):
        jwt_token = self.__create_jwt_token(http_method=self.http_method)
        headers = {'Authorization': f"Bearer {jwt_token}"}
        client = httpx.Client(headers=headers, verify=False)
        r = client.get(self.url)
        content = r.json()['result_content']
        return content
    
    def get_all_data(self):
        res = self.fetch_data()
        if isinstance(res, list) and res:
            table = PrettyTable(['Host Name', 'IP Address', 'Registration Time'])
            for data in res:
                host = data['host_name']
                ip = data['ip_address_list']
                registration_time = data['last_registration_time']
                table.add_row([host, ip, registration_time])
                
            tbl = table.get_string(title="All Data")
            print(tbl)
            
    def get_all_host(self):
        res = self.fetch_data()
        if isinstance(res, list) and res:
            datas = [];
            for data in res:
                datas.append(data['host_name'])
                
            return datas
    
    def check_if_data_exists(self, host: str):
        data = self.fetch_data()
        if isinstance(data, list) and data:
            if data and isinstance(data, list):
                data_found = next((d for d in data if d["host_name"].casefold() == host.casefold()), None)
                # Equivalent to
                # data_found = None
                # for d in data:
                #     if d['host_name'].casefold() == host.casefold():
                #         data_found = d
                #         break
                if data_found is not None:
                    table = PrettyTable(["Type", "Result"])
                    for key, value in data_found.items():
                        if key == 'ip_address_list':
                            table.add_row(['IP Address', value])
                        elif key == 'connection_status':
                            table.add_row(['Connection Status', value])
                        elif key == 'entity_id':
                            table.add_row(['Entity ID', value])
                        elif key == 'last_registration_time':
                            table.add_row(['Last Registration Time', value])
                    tbl = table.get_string(title=data_found['host_name'])
                    print(tbl)
                else:
                    print("""  ____        _          _   _       _     _____                     _ 
    |  _ \  __ _| |_ __ _  | \ | | ___ | |_  |  ___|__  _   _ _ __   __| |
    | | | |/ _` | __/ _` | |  \| |/ _ \| __| | |_ / _ \| | | | '_ \ / _` |
    | |_| | (_| | || (_| | | |\  | (_) | |_  |  _| (_) | |_| | | | | (_| |
    |____/ \__,_|\__\__,_| |_| \_|\___/ \__| |_|  \___/ \__,_|_| |_|\__,_|""")