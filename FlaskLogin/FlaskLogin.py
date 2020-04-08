from app import app, mydb, mycol


@app.shell_context_processor
def make_shell_context():
    return {'mydb': mydb, 'mycol': mycol}
