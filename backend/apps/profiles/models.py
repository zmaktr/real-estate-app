from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from apps.common.models import TimeStampUUIDModel

User = get_user_model()


class Gender(models.TextChoices):
    """
    Gender class is used as a choice in Profile.gender but defined outside the Profile
    class because this way user is not restricted to only choose from the provided 
    choices strictly but can add any entry.
    """
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")

class Profile(TimeStampUUIDModel):
    user                = models.OneToOneField(User, verbose_name=_("profile"), on_delete=models.CASCADE)
    phone_number        = PhoneNumberField(verbose_name=_("Phone Number"), max_length=30, blank=False, null=False)
    about_me            = models.TextField(verbose_name=_("About me"), default=_("Say something about your self"))
    license_number      = models.CharField(verbose_name=_("Realestate license"), max_length=20, blank=True, null=True)
    profile_photo       = models.ImageField(verbose_name =_("Profile Photo"), upload_to='profile_photo', default='/profile_photo/default.png')
    gender              = models.CharField(verbose_name=_("Gender name"), max_length=6, choices=Gender.choices)
    country             = CountryField(verbose_name=_("Country"), blank=False, null=False)
    city                = models.CharField(verbose_name=_("City"), blank=False, null=False, max_length=180)
    is_buyer            = models.BooleanField(verbose_name=_("Buyer"), default=False, help_text=_("Are you looking to buy a property"))
    is_seller           = models.BooleanField(verbose_name=_("Seller"), default=False, help_text=_("Are you looking to sell a property"))
    is_agent            = models.BooleanField(verbose_name=_("Agent"), default=False, help_text=_("Are you an agent"))
    top_agent           = models.BooleanField(verbose_name=_("Top Agent"), default=False)
    rating              = models.DecimalField(verbose_name=_("Rating"), null=True, blank=True, decimal_places=2, max_digits=4)
    num_reviews         = models.IntegerField(verbose_name=_("Number of Reviews"), null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.user.username}'s Profile"