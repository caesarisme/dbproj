from django.db import models


class City(models.Model):
    title_eng = models.CharField(max_length=100, default='empty')
    title_ru = models.CharField(max_length=100, default='empty')
    title_kaz = models.CharField(max_length=100, default='empty')
    x = models.IntegerField()
    y = models.IntegerField()

    def __str__(self):
        return self.title_eng


class University(models.Model):
    code = models.IntegerField()

    title_eng = models.CharField(max_length=200, default='empty')
    title_ru = models.CharField(max_length=200, default='empty')
    title_kaz = models.CharField(max_length=200, default='empty')

    specialties = models.ManyToManyField('Speciality', related_name='universities')
    city = models.ForeignKey('City', related_name='universities', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.code) + ' | ' + self.title_eng


class Speciality(models.Model):
    code = models.IntegerField()
    title_eng = models.CharField(max_length=200, default='empty')
    title_ru = models.CharField(max_length=200, default='empty')
    title_kaz = models.CharField(max_length=200, default='empty')

    SUBJECTS_CHOICE = [
        ('biology_geography', 'Biology and Geography'),
        ('biology_chemistry', 'Biology and Chemistry'),
        ('whistory_geography', 'World history and Geography'),
        ('whistory_law', 'World history and Law'),
        ('geography_flanguage', 'Geography and Foreign language'),
        ('geography_math', 'Geography and Math'),
        ('flanguage_whistory', 'Foreign language and World history'),
        ('language_literature', 'Kazakh/Russian language and Kazakh/Russian literature'),
        ('kazlanguage_kazliterature', 'Kazakh language and Kazakh literature'),
        ('math_physics', 'Math and Physics'),
        ('rulanguage_reliterature', 'Russian language and Russian literature'),
        ('creativity_exam', 'Creativity exam'),
        ('chemistry_physics', 'Chemistry and Physics'),
    ]

    subjects = models.CharField(max_length=200, choices=SUBJECTS_CHOICE)

    def __str__(self):
        return str(self.code) + ' | ' + self.title_ru + ' (' + self.title_eng + ')'
