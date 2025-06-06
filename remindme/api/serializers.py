from rest_framework import serializers
from .models import Reminder
from datetime import datetime

class ReminderSerializer(serializers.ModelSerializer):
    date = serializers.DateField(write_only=True)
    time = serializers.TimeField(write_only=True)

    class Meta:
        model = Reminder
        fields = ['id', 'message', 'date', 'time', 'method', 'remind_at']
        read_only_fields = ['remind_at']

    def validate(self, data):
        remind_at = datetime.combine(data['date'], data['time'])
        # check if provided data and time is not less than current date and time
        if remind_at <= datetime.now():
            raise serializers.ValidationError("Remind time must be in the future.")
        # if datetime is correct set the combined date and time to the remind_at field
        data['remind_at'] = remind_at
        return data

    def create(self, validated_data):
        # remove data and time from the validate array since data and time are only used to calculate the remind_at value but they are not part of the model(Reminder)
        validated_data.pop('date')
        validated_data.pop('time')
        return super().create(validated_data)
