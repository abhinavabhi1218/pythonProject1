# Generated by Django 3.2.3 on 2021-06-13 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appD', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Sample',
        ),
    ]
