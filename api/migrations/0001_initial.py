# Generated by Django 4.1.5 on 2023-01-05 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event', models.TextField(max_length=500, null=True)),
                ('hours', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('visits', models.IntegerField(default=0)),
                ('publications', models.IntegerField(default=0)),
                ('films', models.IntegerField(default=0)),
                ('studies', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HoursResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20, null=True)),
                ('hours', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('visits', models.IntegerField(default=0)),
                ('publications', models.IntegerField(default=0)),
                ('films', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, null=True)),
                ('image', models.ImageField(upload_to='maps')),
            ],
        ),
        migrations.CreateModel(
            name='Months',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=20, null=True)),
                ('hours', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('visits', models.IntegerField(default=0)),
                ('publications', models.IntegerField(default=0)),
                ('films', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EventsHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('event', models.TextField(max_length=500, null=True)),
                ('hours', models.IntegerField(default=0)),
                ('minutes', models.IntegerField(default=0)),
                ('visits', models.IntegerField(default=0)),
                ('publications', models.IntegerField(default=0)),
                ('films', models.IntegerField(default=0)),
                ('studies', models.IntegerField(default=0)),
                ('month', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.months')),
            ],
        ),
    ]
