# Generated by Django 2.2.7 on 2019-11-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191125_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speciality',
            name='subjects',
            field=models.CharField(choices=[('biology_geography', 'Biology and Geography'), ('biology_chemistry', 'Biology and Chemistry'), ('whistory_geography', 'World history and Geography'), ('whistory_law', 'World history and Law'), ('geography_flanguage', 'Geography and Foreign language'), ('geography_math', 'Geography and Math'), ('flanguage_whistory', 'Foreign language and World history'), ('language_literature', 'Kazakh/Russian language and Kazakh/Russian literature'), ('kazlanguage_kazliterature', 'Kazakh language and Kazakh literature'), ('math_physics', 'Math and Physics'), ('rulanguage_reliterature', 'Russian language and Russian literature'), ('creativity_exam', 'Creativity exam'), ('chemistry_physics', 'Chemistry and Physics')], max_length=200),
        ),
    ]
