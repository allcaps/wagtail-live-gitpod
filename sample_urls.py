
from wagtail_live import urls as live_urls  # noqa

urlpatterns = [
    path('wagtail_live/', include(live_urls)),
] + urlpatterns
