# Docker Image
 Docker image for Python web server and MySQL database.

Starting image(you need to have docker desktop app):
docker compose up --build

NOTE:
MySQL server needs around 15 seconds to start. Terminal will print error messages, because script is constantly trying to connect to the databse

#### Used Libraries:
* Flask for web server connection with Jinja2 templates
* mysql-connector-python for connecting python with the databaase
