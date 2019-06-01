# Generated by Django 2.2.1 on 2019-06-01 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='TeeBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('BLACK', 'Black'), ('BLUE', 'Blue'), ('WHITE', 'White'), ('GOLD', 'Gold')], default='BLUE', max_length=5)),
                ('rating', models.FloatField()),
                ('slope', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teeboxes', related_query_name='teebox', to='courses.Course')),
            ],
            options={
                'verbose_name_plural': 'Tee Boxes',
            },
        ),
        migrations.CreateModel(
            name='Hole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField()),
                ('par', models.PositiveSmallIntegerField()),
                ('handicap', models.PositiveSmallIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holes', related_query_name='hole', to='courses.Course')),
            ],
        ),
    ]