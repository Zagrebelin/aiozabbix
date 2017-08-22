# zabbix
just another zabbix api wrapper

# usage
    import zabbix
    api = zabbix.ZabbixAsync('username', 'password', 'http://zabbix_host/zabbix_url/')
    data = await api('hosts.get')
