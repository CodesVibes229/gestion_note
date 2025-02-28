from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from .models import User
from .forms import LoginForm, RegisterForm
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Connexion réussie !", "success")
            return redirect(url_for('main.index'))
        flash("Identifiants incorrects", "danger")
    return render_template("login.html", form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            flash("Ce nom d'utilisateur est déjà pris.", "warning")
        else:
            new_user = User(username=form.username.data)
            new_user.set_password(form.password.data)
            db.session.add(new_user)
            db.session.commit()
            flash("Compte créé avec succès !", "success")
            return redirect(url_for('auth.login'))
    return render_template("register.html", form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Déconnexion réussie.", "info")
    return redirect(url_for('auth.login'))
