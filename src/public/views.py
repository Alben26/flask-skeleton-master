"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template
from .forms import vstupcards
from ..data.database import db
from ..data.models import LogUser, cards
from sqlalchemy import func
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = vstupcards()
    if form.validate_on_submit():
        cards.create(**form.data)
    return render_template("public/cards.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/vystup',methods=['GET'])
def vystup():
    pole = db.session.query(cards.card_number.label("card_number"),func.strftime('%Y-%m-%d %H:%M', cards.TIME).label("time")).group_by(func.strftime('%Y-%m', cards.TIME)).all()
    return render_template("public/vystup.tmpl",data = pole)