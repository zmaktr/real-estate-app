from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from apps.common.models import TimeStampUUIDModel
from apps.profiles.models import Profile

User = get_user_model()
class Ratings(TimeStampUUIDModel):

    class Range(models.IntegerChoices):
        """
        Choice class range is defined inside the Ratings class because we strictly
        want to add entry into the DB that is within range
        """
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")
    
    rating_by_user = models.ForeignKey(User, verbose_name=_("Rating by user"), on_delete=models.SET_NULL, null=True)
    agent_rated = models.ForeignKey(Profile, verbose_name=_("Agent rating"), on_delete=models.SET_NULL)
    rating = models.IntegerField(verbose_name=_("Rating"), choices=Range.choices, help_text="1=Poor, 2=Fair, 3=Good, 4=Very good, 5=Excellent")
    comment = models.TextField(verbose_name=_("Comment"))

