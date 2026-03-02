from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Project, ProjectUser, Task, Note
from .serializers import ProjectSerializer, TaskSerializer, NoteSerializer


# 1 & 2 → Project Create & Update
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # 3 → Add Users to Project
    @action(detail=True, methods=['post'])
    def add_user(self, request, pk=None):
        project = self.get_object()
        user_id = request.data.get("user_id")

        try:
            user = User.objects.get(id=user_id)
            ProjectUser.objects.create(project=project, user=user)
            return Response({"message": "User added to project"})
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)


# 4,5,6 → Task APIs
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # 5 → Assign user to task
    @action(detail=True, methods=['post'])
    def assign_user(self, request, pk=None):
        task = self.get_object()
        user_id = request.data.get('assigned_to')
        user = User.objects.get(id=user_id)
        task.assigned_to = user
        task.save()
        return Response({"message": "User assigned successfully"})

    # 6 → Update task status
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        task = self.get_object()
        task.status = request.data.get("status")
        task.save()
        return Response({"message": "Task status updated"})


# 7 → Note Creation
class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer