from django.contrib import admin
from .models import Ratings

class RatingsAdmin(admin.ModelAdmin):
    list_display = ["rater", "agent", "rating"]

admin.site.register(Ratings, RatingsAdmin)
