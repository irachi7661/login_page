from flask import Blueprint, render_template

docs_blueprint = Blueprint('docs', __name__, template_folder='../templates')

@docs_blueprint.route('/docs')
def docs():
    return render_template('docs.html')
