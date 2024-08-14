from .routes import app

# generator = __init__.create_app()

if __name__ == '__main__':
    app.run(debug=True)