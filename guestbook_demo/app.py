from __future__ import absolute_import, unicode_literals

from guestbook_demo import db

from flask import Flask, render_template
app = Flask('guestbook_demo')


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


@app.route("/")
def root():
    return render_template('index.html')
