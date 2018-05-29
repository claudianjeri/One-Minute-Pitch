from . import main
from flask import render_template, request, redirect, url_for
from ..models import Pitch
from .forms import PitchForm
# Pitch = pitch.Pitch
from flask_login import login_required


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/new-pitch/', methods = ['GET' ,'POST'])
@login_required
def create():

    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        name = pitch_form.name.data
        category = pitch_form.category.data
        pitch_data = pitch_form.pitch.data
        new_pitch = Pitch(name, category, pitch_data)
        new_pitch.save_pitch()



    return render_template('new.html', pitch_form = pitch_form)