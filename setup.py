from setuptools import setup

setup(
    name='liqui',
    version='1.0.0',
    description='Async Zabbix api wrapper',
    long_description=open('README.md', 'rt').read(),
    url='https://github.com/banteg/liqui',
    author='banteg',
    license='MIT',
    py_modules=['liqui'],
    install_requires=['aiohttp']
)