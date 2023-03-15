import datetime

from django.core.exceptions import ValidationError

from tracker.models import Habit


class ValidateAward:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('award'):
            if value.get('related_habit'):
                raise ValidationError('Нельзя одновременно выбрать приятную привычку и указание вознаграждения')


class ValidateCompletionTime:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        completion_time = value.get('time_to_complete')
        max_allowed_time = datetime.time(hour=0, minute=2, second=0)
        if completion_time > max_allowed_time:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')


class ValidateAwardRelatedHabitNotNull:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if not value.get('pleasant_or_not'):
            if (value.get('related_habit') is None) and (value.get('award') is None):
                raise ValidationError('Нельзя, чтобы связанная привычка и вознаграждение были одновременно пустые')


class ValidateRelatedHabitIsPleasant:

    def __init__(self, field):
        self.field = field

    requires_context = True

    def __call__(self, value, serializer_field):
        habit_pk = serializer_field.initial_data.get('related_habit')
        pleasant_habit = Habit.objects.filter(pk=habit_pk).first()
        if pleasant_habit:
            if not pleasant_habit.pleasant_or_not:
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной '
                                      'привычки')
            else:
                return True


class ValidatePleasantHasNotRelatedOrAward:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('pleasant_or_not'):
            if value.get('related_habit') is None:
                if value.get('award') is None:
                    return True
                else:
                    raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')
            else:
                raise ValidationError('у приятной привычки не может быть вознаграждения или связанной привычки')


class ValidatePeriodicity:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value.get('frequency'):
            if value.get('frequency') > 7:
                raise ValidationError('Периодичность не может быть более 7 дней, то есть привычку нельзя выполнять '
                                      'больше, чем раз в неделю')
            else:
                return True
        return True
