from . import main
from flask import render_template, request, redirect, url_for
from ..models import Pitch
from .forms import PitchForm



@main.route('/')
def index():
    return render_template('index.html')

@main.route('/')
def create(usname):

    form = PitchForm()
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data
        pitch_data = form.pitch.data
        new_pitch = Pitch(name, category, pitch_data)
        new_pitch.save_pitch()

    pitch = Pitch.get_pitch(usname)

    return render_template('new.html',pitch_form = form,usname = usname)