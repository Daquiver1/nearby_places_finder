"""Config file."""

from starlette.config import Config

config = Config(".env")

GOOGLE_MAPS_API_KEY = config("GOOGLE_MAPS_API_KEY", cast=str)
