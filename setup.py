from setuptools import setup, find_packages

setup(
    name='lulzcrypto',
    version='1.0',
    packages=find_packages(),
    install_requires=['lulzcode', 'jwt', 'requests'],
    author='LulzLoL231',
    author_email='lznet@pm.me',
    description='Encrypt cleartext by JWT, encode it with lulzcode, and upload it to pastebin.',
    keywords='encrypt crypto lulz lulzcrypto jwt',
    project_urls={
        'Source Code': 'https://github.com/LulzLoL231/lulzcrypto'
    },
    zip_safe=False
)
