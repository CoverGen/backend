# this file contains user basic validation and logic when login or register user
from ticket_app.models import Event
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ticket_app.serializers import EventSerializer


class EventApiView(APIView):
    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Success", "data": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {"message": "Error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
