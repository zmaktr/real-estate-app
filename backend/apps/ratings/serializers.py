from rest_framework import serializers
from .models import Ratings


class RatingSerializer(serializers.ModelSerializer):
    rater = serializers.SerializerMethodField()
    agent = serializers.SerializerMethodField()

    class Meta:
        model = Ratings
        exclude =["updated_at", "pkid"]
    
    #other than set get_<name of field> method takes in the object that is being serialized
    def get_rater(self, object):
        return object.rater.username
    def get_agent(self, object):
        return object.agent.user.username
