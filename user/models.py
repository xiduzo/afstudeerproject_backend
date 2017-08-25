from django.db import models
from libs.models import UUIDModel

# Create your models here.
class User(UUIDModel):
    MALE = 0
    FEMALE = 1

    GENDERS = (
        (MALE, ('male')),
        (FEMALE, ('female'))
    )

    uid            = models.CharField(max_length = 20, blank=True, null=True)
    student_number = models.IntegerField(blank=True, null=True)
    email          = models.EmailField()
    initials       = models.CharField(max_length = 15, blank=True, null=True)
    first_name     = models.CharField(max_length = 50, blank=True, null=True)
    surname_prefix = models.CharField(blank=True, null=True,max_length = 50)
    surname        = models.CharField(max_length = 50, blank=True, null=True)
    gender         = models.PositiveIntegerField(
        choices    = GENDERS
    )
    is_superuser   = models.BooleanField(
        default    = False,
    )
    is_staff       = models.BooleanField(
        default    = False,
    )
    is_active      = models.BooleanField(
        default    = True,
    )

    def get_full_name():
        return '{} {} {}'.format(
            self.first_name,
            self.surname_prefix,
            self.surname,
        )

    def __str__(self):
        return '{} {}'.format(
            # self.first_name,
            self.surname_prefix,
            self.surname,
        )
