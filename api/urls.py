from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, NoteViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = router.urls