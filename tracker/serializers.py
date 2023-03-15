from rest_framework import serializers

from tracker.models import Habit
from tracker.validators import ValidateAward, ValidateCompletionTime, ValidateAwardRelatedHabitNotNull, \
    ValidateRelatedHabitIsPleasant, ValidatePleasantHasNotRelatedOrAward, ValidatePeriodicity


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        exclude = ['user']
        validators = [
            ValidateAward(field=('award', 'related_habit')),
            ValidateCompletionTime(field='time_to_complete'),
            ValidateAwardRelatedHabitNotNull(field=('pleasant_or_not', 'related_habit', 'award')),
            ValidateRelatedHabitIsPleasant(field='pleasant_or_not'),
            ValidatePleasantHasNotRelatedOrAward(field=('pleasant_or_not', 'related_habit', 'award')),
            ValidatePeriodicity(field='frequency')
        ]
