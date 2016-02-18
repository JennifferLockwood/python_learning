from python_crash_course.chapter_9.user_admin_privileges_module import Admin

admin_user = Admin('michael', 'clooney', 'administrator', 'canada', 'quebec')
admin_user.greeter_user()
admin_user.describe_user()
admin_user.privileges.describe_privileges()