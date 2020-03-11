from . import views
from .views import router

app_name = 'breweries'

# Router paths handled in views.py
urlpatterns = router.urls
