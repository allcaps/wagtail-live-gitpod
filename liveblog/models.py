from wagtail.core.models import Page

from wagtail_live.models import LivePageMixin

class LiveBlogPage(Page, LivePageMixin):
    content_panels = Page.content_panels + LivePageMixin.panels
