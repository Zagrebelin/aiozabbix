# zabbix
Async zabbix api wrapper

# usage
    from aiozabbix import ZabbixAsync
    api = ZabbixAsync('username', 'password', 'http://zabbix_host/zabbix_url/')
    data = await api('hosts.get')
