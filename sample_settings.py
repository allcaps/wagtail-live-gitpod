
INSTALLED_APPS = [
    "liveblog",
    "wagtail_live",
] + INSTALLED_APPS

WAGTAIL_LIVE_PAGE_MODEL = "liveblog.models.LiveBlogPage"
WAGTAIL_LIVE_PUBLISHER = "wagtail_live.publishers.polling.LongPollingPublisher"
