from django.db import models

DJANGO_TYPE_MAPPING = {
    'varchar': models.CharField,
    'bool': models.BooleanField,
    'date': models.DateField,
    'datetime': models.DateTimeField,
    'double precision': models.FloatField,
    'integer': models.IntegerField,
    'bigint': models.BigIntegerField,
    'longtext': models.TextField,
    'time': models.TimeField,
}
