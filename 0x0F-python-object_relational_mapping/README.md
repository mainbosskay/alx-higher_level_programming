# Python - Object-relational mapping
This is a directory that contains projects on Python - Object-relational mapping, which is a programming technique that allows developers to interact with relational databases using Python. In this directory, the ORM framework that will be used is SQLAlchemy.

## Dependencies
The following dependencies will be needed for this python project.
### venv
- $ sudo apt-get install python3.8-venv
- $ python3 -m venv venv
- $ source venv/bin/activate
### MySQLdb module version 2.0.x
- $ sudo apt-get install python3-dev
- $ sudo apt-get install libmysqlclient-dev
- $ sudo apt-get install zlib1g-dev
- $ sudo pip3 install mysqlclient
- ...
- $ python3
- >>> import MySQLdb
- >>> MySQLdb.version_info 
- (2, 0, 3, 'final', 0)
### SQLAlchemy module version 1.4.x
- $ sudo pip3 install SQLAlchemy
- ...
- $ python3
- >>> import sqlalchemy
- >>> sqlalchemy.__version__ 
- '1.4.22'

  **All these dependencies will be isntalled on an Ubuntu 20.04 machine**

## Requirements
The following requriements are needed for this projects.
- Your files will be executed with MySQLdb version 2.0.x
- Your files will be executed with SQLAlchemy version 1.4.x
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.8.x)
- All your files must be executable
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- You are not allowed to use "execute" with sqlalchemy.
