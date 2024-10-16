# Generated by Django 4.2.3 on 2024-10-15 09:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recognition_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KnownIndividual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('town', models.CharField(max_length=100)),
                ('additional_info', models.TextField(blank=True)),
                ('face_image', models.ImageField(upload_to='known_faces/')),
                ('face_encoding', models.BinaryField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_image', models.ImageField(upload_to='uploads/')),
                ('processed_image', models.ImageField(blank=True, null=True, upload_to='processed/')),
                ('match_found', models.BooleanField(default=False)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('matched_individual', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='recognition_app.knownindividual')),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
