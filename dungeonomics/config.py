# dungeonomics/config.py
import os

settings = {
    "db_name": os.getenv("DB_NAME", "dungeonomics"),
    "db_user": os.getenv("DB_USER", "dungeonomics"),
    "db_password": os.getenv("DB_PASSWORD", "dungeonomics"),
    "db_host": os.getenv("DB_HOST", "db"),
    "db_port": int(os.getenv("DB_PORT", 5432)),
    "secret_key": os.getenv("DJANGO_SECRET_KEY", "change-me-in-prod"),
    "debug": os.getenv("DJANGO_DEBUG", "True").lower() == "true",
    "admin": os.getenv("DJANGO_ADMIN_PATH", "admin"),
    "allowed_hosts": os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(","),
    "ga": os.getenv("USE_GA", "false").lower() == "true",
    "email_backend": os.getenv(
        "EMAIL_BACKEND",
        "django.core.mail.backends.console.EmailBackend"
    ),
    "email_user": os.getenv("EMAIL_HOST_USER", ""),
    "email_password": os.getenv("EMAIL_HOST_PASSWORD", ""),
    "email_from": os.getenv("DEFAULT_FROM_EMAIL", "noreply@localhost"),
}