# Kathryn Rowe's Portfolio

### Setup/Installation

Customize for own portfolio; install requirements to run locally.

Clone repository:

```sh
$ git clone https://github.com/kathryn-rowe/Kathryn-Rowe-portfolio.git
```
Move into folder and create vagrant machine.

```sh
$ cd Kathryn-Rowe-portfolio
$ vagrant up
$ vagrant ssh
```
Create virtual environment:

```sh
$ virtualenv env
```
Activate virtual environment:
```sh
$ source env/bin/activate
```
Install dependencies:
```sh
$ pip install -r requirements.txt
```
Gather necessary secret keys from Flask. Save to your secrets file. Link to server.py.

Create database if you want to password protect your portfolio:

```sh
$ createdb users
```
```sh
$ python -i model.py
```
```sh
>>>db.create_all() 
```
```sh
$ psql users
```
```sh
users=# INSERT INTO users (password) VALUES (password);
```
### Todos

 - Write more tests

License
----

Copyright 2017 Kathryn Rowe

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


