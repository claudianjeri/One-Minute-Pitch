from . import main
from flask import render_template, request, redirect, url_for
from ..models import Pitch
from .forms import PitchForm
# Pitch = pitch.Pitch


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/new-pitch/', methods = ['GET' ,'POST'])
# @login_required
def create():

    form = PitchForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        pitch_data = form.pitch.data
        new_pitch = Pitch(name, category, pitch_data)
        new_pitch.save_pitch()

    pitch = Pitch.save_pitch()

    return render_template('new.html', pitch = pitch, pitch_form = form)