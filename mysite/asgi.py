import os

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

application = ProtocolTypeRouter({
  "http": AsgiHandler(),
  # Just HTTP for now. (We can add other protocols later.)
})
