from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.user.username
    
    
class AdminReport(models.Model):
    admin = models.ForeignKey(AdminProfile,
                              on_delete=models.CASCADE)
    work_report = models.TextField()
    communication = models.TextField()
    feedback = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('submitted', 'Submitted'),
            ('approved', 'Approved')
        ],
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Report by {self.admin} on {self.created_at.date()}"