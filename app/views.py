from flask import Blueprint, render_template, request, redirect, url_for
from .models import db, Note

main = Blueprint('main', _name_)

@main.route('/')
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@main.route('/add', methods=['POST'])
def add_note():
    note_content = request.form.get('note')
    if note_content:
        new_note = Note(content=note_content)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('main.index'))
