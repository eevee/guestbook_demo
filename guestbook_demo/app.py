from __future__ import absolute_import, unicode_literals

from guestbook_demo import db

from flask import Flask, redirect, render_template, request, url_for
app = Flask('guestbook_demo')


@app.teardown_request
def shutdown_session(exception=None):
    db.session.remove()


@app.route("/")
def root():
    # TODO paginate me!
    entries = db.session.query(db.GuestbookEntry) \
        .order_by(db.GuestbookEntry.timestamp.desc())

    return render_template('index.html', entries=entries)

@app.route("/sign", methods=['POST'])
def signme():
    new_entry = db.GuestbookEntry(
        name=request.form.get('name') or 'Some dummy who forgot to leave a name',
        message=request.form.get('message') or 'WOW THIS IS THE BEST WEBSITE EVER',
    )
    db.session.add(new_entry)
    db.session.commit()

    return redirect(url_for('root'))
