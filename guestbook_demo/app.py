from __future__ import absolute_import, unicode_literals

from flask import Flask
app = Flask('guestbook_demo')


@app.route("/")
def root():
    return "Wow this is totally useless so far!"
