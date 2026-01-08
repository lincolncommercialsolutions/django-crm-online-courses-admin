from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Interaction(models.Model):
    CHANNEL_CHOICES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
        ('chat', 'Chat'),
        ('social', 'Social Media'),
        ('in_person', 'In Person'),
    ]
    
    DIRECTION_CHOICES = [
        ('inbound', 'Inbound'),
        ('outbound', 'Outbound'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    channel = models.CharField(max_length=20, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=20, choices=DIRECTION_CHOICES)
    summary = models.TextField()
    interaction_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer.name} - {self.channel} - {self.interaction_date}"
    
    class Meta:
        ordering = ['-interaction_date']


# Online Course Models
class Instructor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_time = models.BooleanField(default=True)
    total_learners = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username


class Learner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=200, default='Developer')
    social_link = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.user.username


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    instructors = models.ManyToManyField(Instructor)
    
    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    content = models.TextField()
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='questions')
    question_text = models.TextField()
    grade = models.IntegerField(default=1)
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)
    submit_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.course.name}"
