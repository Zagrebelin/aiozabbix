import urllib.parse

import aiohttp


class ZabbixAsync():
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = urllib.parse.urljoin(url, 'api_jsonrpc.php')
        self.token = None

    async def login(self):
        if not self.token and self.username and self.password:
            self.token = await self._exec('user.login', user=self.username, password=self.password)

    async def __call__(self, method, *args, **kwargs):
        await self.login()
        return await self._exec(method, *args, **kwargs)

    async def _exec(self, method, send_auth=True, *args, **kwargs):
        data = {
            'jsonrpc': '2.0',
            'method': method,
            'id': '_',
            'params': args or kwargs
        }
        if self.token and send_auth:
            data['auth'] = self.token
        headers = {
            'Content-Type': 'application/json-rpc; charset=UTF-8'
        }
        async with aiohttp.ClientSession() as sess:
            async with sess.post(self.url, json=data, proxy=None, headers=headers) as resp:
                j = await resp.json()
                if 'error' in j:
                    raise Exception(j['error'])
                return j['result']

