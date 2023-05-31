# Generated by Django 4.2 on 2023-04-28 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CBVapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Course1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('intructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='CBVapp.intructor')),
            ],
        ),
    ]