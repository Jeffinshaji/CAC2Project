from django.contrib import admin
from .models import user_details, interests, improvements,teching

admin.site.register(user_details)
admin.site.register(interests)
admin.site.register(improvements)
admin.site.register(teching)

