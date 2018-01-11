from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='hci',
    version='0.0.5',
    description='Library for creating and parsing HCI packets.',
    url='https://github.com/acburigo/python-hci',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=['HCI', 'protocol', 'ti', 'texas instruments', 'encode', 'decode',
              'ble', 'bluetooth low energy'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    author='Arthur Crippa Búrigo & Pedro Gyrão',
    author_email='arthurcburigo@gmail.com',
)
