from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todos', views.TodoViewSet, basename='todo')

urlpatterns = [
]

urlpatterns += router.urls