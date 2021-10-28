import json
from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from wagtail.core.models import Page

from liveblog.models import LiveBlogPage


class Command(BaseCommand):
    help = "Create sample data"

    def handle(self, *args, **options):
        # Create a user
        get_user_model().objects.create_superuser('admin', '', 'changeme')

        # Create a Live blog page
        homepage = Page.objects.get(slug="home")
        now = datetime.utcnow().isoformat() + "Z"
        page = LiveBlogPage(
            title="Live blog",
            channel_id="some_channel_id",
            live_posts=json.dumps([
                {
                    "type": "live_post",
                    "value": {
                        "message_id": "1",
                        "created": now,
                        "modified": now,
                        "show": True,
                        "content": [
                            {
                                "type": "text",
                                "value": '<p data-block-key="kekjo">First post</p>',
                                "id": "ae8cd229-9a9d-4b07-a1fa-254fec3fc0ca",
                            }
                        ],
                    },
                    "id": "2c077aac-e53e-4161-8c88-b165cdf581e6",
                }
            ]),
        )
        homepage.add_child(instance=page)
