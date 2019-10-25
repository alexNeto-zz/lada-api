import os


class AboutService:

    def get_version(self):
        return {
            "api_version": self.api_version()
        }

    def api_version(self):
        return os.environ.get('API_VERSION', '0.0.0')
