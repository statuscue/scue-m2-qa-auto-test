from __main__ import app

from flask import render_template


@app.route('/HttpServices/api/bluewood_data/', methods=['GET', 'POST'])
def return_some_data():
    return render_template("bluewood_data.json")
