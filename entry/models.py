from django.conf import settings
from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.

def validate_even(value):
    if (int)(value) % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
    )

def validate_existence(value):
    '''
    La idea es validar la existencia del subjectId recibido contra la b.d
    '''
    if not Subject.objects.filter(subjectId=value).exists():
        raise ValidationError(
            _('SubjectId %(value)s does not exist in the Data Base'),
            params={'value': value},
    )

class Subject(models.Model):
    '''
    '''
    subjectId = models.CharField(
        primary_key=True,
        validators=[RegexValidator(r'\d{8,8}','Enter 8 digits'),
                    #validate_even,
                    validate_existence,],
        max_length=8,
        blank=False,
        help_text='(8 digits)',
    )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.subjectId}'

class Variation(models.Model):
    '''
    '''
    variation = models.CharField(max_length=16, primary_key=True,)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.variation}'


class Entry(models.Model):
	'''
	'''
	subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
	variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	T_CHOICES = (
		('y', 'Yes'),
		('n', 'No'),
		('u', 'Unknown'),
	)
	test = models.CharField(
		max_length=1,
		choices=T_CHOICES,
		blank=True,
		default='n',
		help_text='Testing state',
	)

	R_CHOICES = (
		('p', 'Positive'),
		('n', 'Negative'),
		('i', 'Inconclusive'),
		('u', 'Unknown'),
	)
	result = models.CharField(
		max_length=1,
		choices=R_CHOICES,
		blank=True,
		default='n',
		help_text='Result state',
	)

	M_CHOICES = (
		('p', 'PCR'),
		('n', 'NGS'),
		('u', 'Unknown'),
	)
	method = models.CharField(
		max_length=1,
		choices=M_CHOICES,
		blank=True,
		default='n',
		help_text='Method used',
	)

	class Meta:
		unique_together =	(
			#('subjectId', 'variation', 'user',),
			('subjectId', 'variation', 'user', 'test'),
			('subjectId', 'variation', 'user', 'result'),
			('subjectId', 'variation', 'user', 'method'),
		)

	def __str__(self):
		"""String for representing the Model object."""
		return f'{self.subjectId} {self.variation} {self.user}: Test[{self.test}] Result[{self.result}] Method[{self.method}]'