from __future__ import absolute_import
import os

from guestbook_demo.app import app

app.run(port=os.environ.get('PORT'))
