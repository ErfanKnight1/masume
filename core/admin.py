from django.contrib import admin
from core.models import Customer, Messages, Resume
from core.models import Profile
admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Messages)
admin.site.register(Resume)