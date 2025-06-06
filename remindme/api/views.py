from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Import the serializer that validates and saves Reminder data
from .serializers import ReminderSerializer

class ReminderCreateView(APIView):
    
    # POST /api/reminders/
    def post(self, request):
        # Deserialize and validate the incoming JSON data using the serializer
        serializer = ReminderSerializer(data=request.data)
        
        # If the data is valid according to the serializer rules
        if serializer.is_valid():
            # Save the data to the database and get the created Reminder object
            reminder = serializer.save()
            
            # Return a success response with the reminder ID
            return Response(
                {"id": reminder.id, "status": "created"},
                status=status.HTTP_201_CREATED
            )
        
        # If validation fails, return the error details with a 400 status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
