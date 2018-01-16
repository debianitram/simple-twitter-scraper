import os
from setuptools import setup, find_packages

import twitter_scraper


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


REQUIREMENTS = [
    'Django>=2',
    'celery==4.1.0',
    # 'djangorestframework==3.7.7', (optional)
    'python-twitter==3.3',
]

setup(
    name='simple-twitter-scraper',
    version=twitter_scraper.__version__,
    description='Simple Twitter Scraper',
    long_description=read('README.md'),
    url='https://github.com/debianitram/simple-twitter-scraper',
    author='Martín Miranda',
    author_email='debianitram@gmail.com',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    keywords=['django', 'twitter', 'scraper', 'celery',],
    install_requires=REQUIREMENTS,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    zip_safe=False,
)