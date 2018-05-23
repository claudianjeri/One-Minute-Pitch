from flask import render_template
from . import main

@main.app_errorhandler(404) #this decorator passes in the error received.
def four_Ow_four(error): #this function returns the file
    '''
    function to render the 404 error page
    '''
    return render_template('fourOwfour.html'),404 #404 is the status code that displays the error page.