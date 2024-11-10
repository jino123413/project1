from flask import Flask
from app.core.logger import setup_logging
from app.config.default import Config

def create_app(config_class=Config):
    app = Flask(__name__, 
                static_folder='../static',
                template_folder='../templates')
    
    app.config.from_object(config_class)
    setup_logging()
    
    from app.trading.routes import trading_bp
    app.register_blueprint(trading_bp)
    
    return app
