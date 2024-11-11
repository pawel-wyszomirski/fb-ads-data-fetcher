import json
from http.client import HTTPSConnection
from urllib.parse import urlencode

class HTTPClient:
    def __init__(self, base_host):
        self.base_host = base_host
        self.conn = HTTPSConnection(base_host)
        
    def request(self, method, path, headers=None, params=None):
        if params:
            path = f"{path}?{urlencode(params)}"
            
        self.conn.request(method, path, headers=headers or {})
        response = self.conn.getresponse()
        data = response.read().decode('utf-8')
        
        if response.status >= 400:
            raise Exception(f"HTTP {response.status}: {data}")
            
        return json.loads(data)
        
    def close(self):
        self.conn.close()