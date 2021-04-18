"""Apps."""
from django.apps import AppConfig


class AcademyConfig(AppConfig):
    """AcademyConfig_class."""

    name = 'academy'

    def ready(self):
        """Signar function."""
        import academy.signals

