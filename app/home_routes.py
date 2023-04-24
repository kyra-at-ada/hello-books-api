from flask import Blueprint

home_page_bp = Blueprint("home_page_bp", __name__, url_prefix="/")

@home_page_bp.route()
def index():
    return {
        "name": "Ada Lovelace",
        "message": "Sample home page!"
    }