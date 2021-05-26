# Generated by Django 3.2.3 on 2021-05-26 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('activate', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=255)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]