from . import main
from flask import render_template 
from ..models import Pitch
from .forms import PitchForm


@main.route('/')
def index():
    return render_template('index.html')