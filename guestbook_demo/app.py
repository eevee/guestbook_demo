from __future__ import absolute_import, unicode_literals

from flask import Flask, render_template
app = Flask('guestbook_demo')


@app.route("/")
def root():
    return render_template('index.html')
