from flask import Blueprint, redirect, render_template, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from . import login_manager
from .models import User
from .forms import LoginForm
from .helper_role import HelperRole
from . import db_manager as db

# Blueprint
auth_bp = Blueprint(
    "auth_bp", __name__, template_folder="templates", static_folder="static"
)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # Si ja està autenticat, sortim d'aquí
    if current_user.is_authenticated:
        flash("Ja has iniciat sessió anteriorment", "info")
        return redirect(url_for("main_bp.init"))

    form = LoginForm()
    if form.validate_on_submit(): # si s'ha enviat el formulari via POST i és correcte
        email = form.email.data
        plain_text_password = form.password.data

        user = load_user(email)
        if user and user.check_password(plain_text_password):
            # aquí és crea la cookie
            login_user(user)
            # aquí s'actualitzen els rols que té l'usuari
            HelperRole.notify_identity_changed()
            
            flash("Sessió iniciada correctament", "success")
            return redirect(url_for("main_bp.init"))

        # si arriba aquí, és que no s'ha autenticat correctament
        flash("Error d'autenticació", "error")
        return redirect(url_for("auth_bp.login"))
    
    return render_template('login.html', form = form)

@login_manager.user_loader
def load_user(email):
    if email is not None:
        # select amb 1 resultat o cap
        user_or_none = db.session.query(User).filter(User.email == email).one_or_none()
        return user_or_none
    return None

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("auth_bp.login"))

@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Sessió tancada correctament", "success")
    return redirect(url_for("auth_bp.login"))