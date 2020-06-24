from flask import render_template
from app import db

@app_errorhandler(404)
def nof_found_error(error):
    return render_template('404.html'),404 #Statiscode


@app_errorhandler(500)
def internal_error(error):
    db.session.rollback() # before data commit  errors found while data in processing of storing to data base rollback will undo data to previous to data/session
    return render_template('500.html'),500 #Statiscode
