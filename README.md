# Kathryn Rowe's Portfolio

Prior to Hackbright, Kate could be found tromping around the woods looking for birds and salmon. Trained as a wildlife biologist, Kate has been working for environmental organizations for the past 10 years. She loves problem solving and found this skill very useful when working for small nonprofits. Her introduction to programming came during her Master's in GIS program when she used Python to solve complex spatial analysis problems. Kate hopes to combine her love of maps and problem solving to software development. Her next step includes further honing her fluency with coding, building her skill base, and pursuing a career as a software developer.

# Tech stack

Frontend: Javascript, jQuery, AJAX, HTML5, CSS, Bootstrap

### Setup/Installation

Install requirements to run locally; customize for own portfolio.

Clone repository:

```sh
$ git clone https://github.com/kathryn-rowe/Tell-Me-About-the-Birds.git
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
 - Add more work sections: invitations, spoon carving, etc.

License
----

MIT


[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


