from setuptools import setup

setup(
    name='zabbix',
    version='1.0.0',
    description='Async Zabbix api wrapper',
    long_description=open('README.md', 'rt').read(),
    url='https://github.com/zagrebelin/zabbix',
    author='zagrebelin',
    license='MIT',
    py_modules=['zabbix'],
    install_requires=['aiohttp']
)