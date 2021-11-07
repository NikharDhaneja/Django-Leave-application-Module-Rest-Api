# Generated by Django 3.2.7 on 2021-09-26 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('request_id', models.AutoField(primary_key=True, serialize=False)),
                ('worker_id', models.IntegerField()),
                ('manager_id', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('days', models.IntegerField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=8)),
            ],
        ),
    ]