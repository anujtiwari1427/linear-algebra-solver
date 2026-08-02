from flask import Flask, render_template, jsonify
from config import Config
from routes.main_routes import main_bp
from routes.api_matrix import matrix_api
from routes.api_vector import vector_api
from routes.api_system import system_api
from routes.api_eigen import eigen_api
from routes.api_decomposition import decomposition_api
from routes.api_advanced import advanced_api

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(matrix_api)
    app.register_blueprint(vector_api)
    app.register_blueprint(system_api)
    app.register_blueprint(eigen_api)
    app.register_blueprint(decomposition_api)
    app.register_blueprint(advanced_api)

    # Global Error Handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('base.html', title="Page Not Found", content="<div class='container py-5 text-center'><h2>404 - Page Not Found</h2><a href='/' class='btn btn-primary mt-3'>Back to Home</a></div>"), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"success": False, "error": "Internal server error occurred."}), 500

    return app

# Top-level WSGI entry point for Flask, Gunicorn, and Vercel
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
