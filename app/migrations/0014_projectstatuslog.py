# Generated by Django 5.1.6 on 2025-03-05 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectStatusLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_status', models.CharField(choices=[('Planning', 'Planning'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20)),
                ('new_status', models.CharField(choices=[('Planning', 'Planning'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=20)),
                ('changed_at', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.project')),
            ],
        ),
    ]
