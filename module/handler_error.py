from flask import render_template, Flask

# general error handlers

def genericErrorHandler(error):
    return render_template("error_message.html", error_name=error.name, error_message=error.description, error_code=error.code), error.code



