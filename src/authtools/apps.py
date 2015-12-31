from __future__ import unicode_literals
from django.apps import AppConfig
from actstream import registry

class AuthtoolsConfig(AppConfig):
    name = "authtools"

    def ready(self):
        registry.register(self.get_model('User'))

