import os
import asyncio
from unittest import TestCase

from zabbix import ZabbixAsync


def async_test(f):
    def wrapper(*args, **kwargs):
        loop = asyncio.new_event_loop()
        future = f(*args, **kwargs)
        asyncio.set_event_loop(None)
        ret = loop.run_until_complete(future)
        return ret
    return wrapper


class ZabbixTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.username = os.environ.get('ZABBIX_USERNAME', None)
        cls.password = os.environ.get('ZABBIX_PASSWORD', None)
        cls.url = os.environ.get('ZABBIX_URL', None)
        if not cls.username or not cls.password or not cls.url:
            raise Exception('ZABBIX_USERNAME, ZABBIX_PASSWORD and ZABBIX_URL environment must be provided.')

    @async_test
    async def test_apiinfo_version(self):
        api = ZabbixAsync(None, None, self.url)
        ret = await api('apiinfo.version')
        self.assertIsInstance(ret, str)

    @async_test
    async def test_hosts_get(self):
        api = ZabbixAsync(self.username, self.password, self.url)
        ret = await api('host.get')
        self.assertGreater(len(ret), 0)