from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import NoteForm
from .models import Note, db
from flask_login import login_user, logout_user, login_required
from .models import User
from .forms import LoginForm, RegisterForm
#from . import db

main = Blueprint('main', __name__)

"""@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.index'))
        flash("Identifiants incorrects", "danger")
    return render_template("login.html", form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Compte créé avec succès", "success")
        return redirect(url_for('auth.login'))
    return render_template("register.html", form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))"""

@main.route('/')
@login_required
def index():
    notes = Note.query.all()
    return render_template('index.html', notes=notes)

@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_note():
    form = NoteForm()
    if form.validate_on_submit():
        new_note = Note(title=form.title.data, content=form.content.data)
        db.session.add(new_note)
        db.session.commit()
        flash("Note ajoutée avec succès", "success")
        return redirect(url_for('main.index'))

    return render_template("add_note.html", form=form)

"""def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if title and content:
            new_note = Note(title=title, content=content)
            db.session.add(new_note)
            db.session.commit()
            return redirect(url_for('main.index'))
    return render_template('add_note.html')"""

@main.route('/delete/<int:id>')
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('main.index'))

