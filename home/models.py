from django.db import models
from django.contrib.auth import get_user_model



User = get_user_model

APP_TYPE = (
    ('Web', 'Web'),
    ('Mobile', 'Mobile')
)

FRAME_WORK = (
    ('Django', 'Django'),
    ('React Native', 'React Native'),
)

class App(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    type = models.CharField(max_length=10, choices=APP_TYPE)
    framework = models.CharField(max_length=20, choices=FRAME_WORK)
    domain_name = models.CharField(max_length=50)
    screenshot = models.URLField()
    subscription = models.ForeignKey('Subscription', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Plan(models.Model):
    name = models.CharField(max_length=20, min=1)
    description = models.TextField()
    price = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
class Subscription(models.Model):
    user = models.ForeignKey(User, related_name='subscriber', on_delete=models.PROTECT)
    plan = models.ForeignKey(Plan, on_delete=models.PROTECT)
    app = models.ForeignKey(App, on_delete=models.PROTECT)
    active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.app.subscription
    
    