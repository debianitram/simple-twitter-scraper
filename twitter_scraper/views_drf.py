from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from .models import TwitterProfile, Task
from .serializers import TaskSerializer, TwitterProfileSerializer


class TwitterProfilesAPIView(APIView):
    
    def post(self, request, **kwargs):
        serializer_status_task = TaskSerializer(data=request.data)
        serializer_status_task.is_valid(raise_exception=True)

        tasks = Task.custom.search(serializer_status_task.validated_data['query'])
        
        if not tasks.exists():
            serializer_status_task.save()
            return Response({'data': 'processing request'}, status=HTTP_200_OK)

        else:
            if tasks.pending().exists():
                return Response({'data': 'processing request'}, status=HTTP_200_OK)

            else:
                # Update followers_count, short_description, name.
                # [Task.run(instance=task, form_view=True) for task in tasks.done()]
                Task.run(instance=tasks.first(), from_view=True)
                

        profiles = TwitterProfile.custom.search(tasks.first().query)
        serializer_profiles = TwitterProfileSerializer(profiles, many=True)

        return Response({'data': serializer_profiles.data}, status=HTTP_200_OK)