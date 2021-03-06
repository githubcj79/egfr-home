# Generated by Django 2.0.8 on 2018-08-25 22:37

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import entry.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(blank=True, choices=[('y', 'Yes'), ('n', 'No'), ('u', 'Unknown')], default='n', help_text='Testing state', max_length=1)),
                ('result', models.CharField(blank=True, choices=[('p', 'Positive'), ('n', 'Negative'), ('i', 'Inconclusive'), ('u', 'Unknown')], default='n', help_text='Result state', max_length=1)),
                ('method', models.CharField(blank=True, choices=[('p', 'PCR'), ('n', 'NGS'), ('u', 'Unknown')], default='n', help_text='Method used', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subjectId', models.CharField(help_text='(8 digits)', max_length=8, primary_key=True, serialize=False, validators=[django.core.validators.RegexValidator('\\d{8,8}', 'Enter 8 digits'), entry.models.validate_existence])),
            ],
        ),
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('variation', models.CharField(max_length=16, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='subjectId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.Subject'),
        ),
        migrations.AddField(
            model_name='entry',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='entry',
            name='variation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entry.Variation'),
        ),
        migrations.AlterUniqueTogether(
            name='entry',
            unique_together={('subjectId', 'variation', 'user', 'result'), ('subjectId', 'variation', 'user', 'method'), ('subjectId', 'variation', 'user', 'test')},
        ),
    ]
