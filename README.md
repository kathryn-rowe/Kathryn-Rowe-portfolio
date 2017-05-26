# Kathryn Rowe's Portfolio

Prior to Hackbright, Kate could be found tromping around the woods looking for birds and salmon. Trained as a wildlife biologist, Kate has been working for environmental organizations for the past 10 years. She loves problem solving and found this skill very useful when working for small nonprofits. Her introduction to programming came during her Master's in GIS program when she used Python to solve complex spatial analysis problems. Kate hopes to combine her love of maps and problem solving to software development. Her next step includes further honing her fluency with coding, building her skill base, and pursuing a career as a software developer.

# Tech stack

Python, Flask, PostgreSQL, SQL Alchemy, Javascript, HTML5/CSS

### Setup/Installation

Install requirements to run locally; customize for own portfolio.

Clone repository:

```sh
$ git clone https://github.com/kathryn-rowe/Kathryn-Rowe-portfolio.git
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

Create database:

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


