# from django.db import models
# from django.contrib.auth.models import AbstractUser

# # Create your models here.

# class Person(AbstractUser):
#     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
#     bio = models.TextField(max_length=500, blank=True)
#     is_teacher = models.BooleanField(default=False)
#     education_level = models.CharField(max_length=50, choices=[
#         ('primary', 'Primary School'),
#         ('secondary', 'Secondary School'),
#         ('high_school', 'High School'),
#         ('undergraduate', 'Undergraduate'),
#         ('postgraduate', 'Postgraduate'),
#     ], default='secondary')
#     interests = models.CharField(max_length=255, blank=True)
#     preferred_language = models.CharField(max_length=10, choices=[
#         ('en', 'English'),
#         ('fr', 'French'),
#         ('es', 'Spanish'),
#         # Add more languages as needed
#     ], default='en')

#     def __str__(self):
#         return self.username

# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     teacher = models.ForeignKey(Person, related_name='courses_taught', on_delete=models.CASCADE)
#     students = models.ManyToManyField(Person, related_name='courses_enrolled')

#     def __str__(self):
#         return self.name

# class Progress(models.Model):
#     user = models.ForeignKey(Person, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     progress_percentage = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.user.username} - {self.course.name} - {self.progress_percentage}%"
