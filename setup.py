from setuptools import setup

setup(
    name='aiozabbix',
    version='1.0.0',
    description='Async Zabbix api wrapper',
    long_description=open('README.md', 'rt').read(),
    url='https://github.com/zagrebelin/aiozabbix',
    author='zagrebelin',
    license='MIT',
    py_modules=['aiozabbix'],
    install_requires=['aiohttp']
)
