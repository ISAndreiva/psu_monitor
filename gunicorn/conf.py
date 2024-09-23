wsgi_app = "psu_monitor.wsgi"
loglevel = "info"
workers = "1"
bind = "0.0.0.0:8080"
accesslog = "/var/log/gunicorn/access.log"
errorlog = "/var/log/gunicorn/error.log"
capture_output = True
daemon = True
