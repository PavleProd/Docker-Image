from flask import Flask, render_template
from mysql import connector
import time

app = Flask("python web server", template_folder="./templates")  # template_folder -> folder where html file is


@app.route('/')  # root page
def helloWorld():
    cursor.execute("select * from users")  # gets all data from table users
    res = cursor.fetchall()
    cursor.execute("describe users")  # gets column names
    header = [column[0] for column in cursor.fetchall()]
    res.insert(0, header)
    return render_template("users.html", result=res)  # template using jinja2




if __name__ == "__main__":
    while True:
        try:
            wgdb = connector.connect(
                host="db",
                user="root",
                password="wgforge",
                database="wgdb"
            )
            print("connected")
            break
        except connector.Error as err:
            print(f"Failed to connect to MySQL server: {err}")
            time.sleep(1)

    cursor = wgdb.cursor()
    app.run(host='0.0.0.0', port=5000)
    cursor.close()
    wgdb.close()
