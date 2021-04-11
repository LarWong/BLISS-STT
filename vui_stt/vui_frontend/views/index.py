"""
BLiSS VUI frontend index (main) view.

URLs include:
/
"""

from flask import (request, session, url_for, abort,
                   redirect, render_template)
import vui_frontend

@vui_frontend.app.route('/', methods=['GET', 'POST'])
def show_index():
    return render_template("index.html")