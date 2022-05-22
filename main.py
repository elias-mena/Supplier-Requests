from flask import (
    Flask,
    redirect,
    url_for,
    request,
    make_response
)
from flask_login import current_user
from apps import create_app

app: Flask = create_app()


@app.route('/')
def main():
    # Request the ip of the user (just to practice the use of cookies)
    user_ip = request.remote_addr
    make_response().set_cookie('user_ip', user_ip)

    # Render the main page
    if current_user is not None and current_user.is_authenticated:
        if current_user.rol == 1:
            return redirect(url_for('admin.index'))
        if current_user.rol == 2:
            return redirect(url_for('customers.index'))
        else:
            return redirect(url_for('approvers.index'))
    else:
        return redirect(url_for('auth.login'))


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
