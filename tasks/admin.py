from django.contrib import admin
from .models import User, Task, TaskHistory, Collaborator

class UsersAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'name', 'created_at')  # Hiển thị các cột này trong bảng quản trị
    search_fields = ('user_name', 'name')  # Thêm chức năng tìm kiếm theo user_name và name

class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_user', 'status', 'priority', 'start_time', 'end_time')
    list_filter = ('status', 'priority')  # Thêm bộ lọc theo trạng thái và độ ưu tiên
    search_fields = ('title', 'description')

    def get_user(self, obj):
        return obj.users_id.name  # Hiển thị tên người dùng
    get_user.short_description = 'User'  # Đặt tiêu đề cột trong admin

class TaskHistoryAdmin(admin.ModelAdmin):
    list_display = ('get_task', 'status', 'updated_at')

    def get_task(self, obj):
        return obj.task_id.title  # Hiển thị tiêu đề công việc
    get_task.short_description = 'Task'

class CollaboratorsAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_task', 'role', 'invited_at')

    def get_user(self, obj):
        return obj.users_id.user_name  # Hiển thị tên đăng nhập người dùng
    get_user.short_description = 'User'

    def get_task(self, obj):
        return obj.task_id.title  # Hiển thị tiêu đề công việc
    get_task.short_description = 'Task'

# Đăng ký các model vào Django admin với các tùy chỉnh
admin.site.register(User, UsersAdmin)
admin.site.register(Task, TasksAdmin)
admin.site.register(TaskHistory, TaskHistoryAdmin)
admin.site.register(Collaborator, CollaboratorsAdmin)



