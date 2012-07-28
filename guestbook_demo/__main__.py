from __future__ import absolute_import
import os

from guestbook_demo.app import app

port = None
if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
app.run(port=port)
