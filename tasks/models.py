from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Thấp', 'Thấp'),
        ('Trung bình', 'Trung bình'),
        ('Cao', 'Cao'),
    ]
    STATUS_CHOICES = [
        ('Đang thực hiện', 'Đang thực hiện'),
        ('Hoàn thành', 'Hoàn thành'),
    ]
    
    users_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=2000)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Trung bình')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Đang thực hiện')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class TaskHistory(models.Model):
    STATUS_CHOICES = [
        ('Đang thực hiện', 'Đang thực hiện'),
        ('Hoàn thành', 'Hoàn thành'),
    ]

    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Đang thực hiện')
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for {self.task_id.title}"

class Collaborator(models.Model):
    ROLE_CHOICES = [
        ('Viewer', 'Viewer'),
        ('Editor', 'Editor'),
    ]
    
    users_id = models.ForeignKey(User, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Editor')
    invited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.users_id.user_name} - {self.task_id.title}"
