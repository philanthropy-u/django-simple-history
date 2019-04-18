from django.db import models

DJANGO_TYPE_MAPPING = {
    'varchar': models.CharField,
    'bool': models.NullBooleanField,
    'date': models.DateField,
    'datetime': models.DateTimeField,
    'double precision': models.FloatField,
    'integer': models.IntegerField,
    'int': models.IntegerField,
    'tinyint': models.SmallIntegerField,
    'bigint': models.BigIntegerField,
    'longtext': models.TextField,
    'time': models.TimeField,
}
