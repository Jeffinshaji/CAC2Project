# Generated by Django 2.1.7 on 2024-02-05 06:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0014_auto_20240205_1211'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('Date', models.DateField()),
                ('Instructor', models.CharField(max_length=100)),
                ('Content', models.IntegerField()),
                ('levelofteaching', models.IntegerField()),
                ('Material', models.IntegerField()),
                ('Rating', models.IntegerField()),
                ('Overallrating', models.IntegerField()),
                ('Comments', models.CharField(max_length=100)),
                ('user', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
