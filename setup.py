from setuptools import setup

setup(
    name='django_validation',
    version='0.0.1',
    author='Shaghayegh Ghorbanpoor',
    author_email='ghorbanpoor.shaghayegh@gmail.com',
    packages=['django_validation'],
    # scripts=['bin/script1', 'bin/script2'],
    # url='http://pypi.python.org/pypi/PackageName/',
    # license='LICENSE.txt',
    description='django model and base validations',
    long_description=open('README.md').read(),
    install_requires=[
        'Django', 'django-role-permissions'
    ],
)
