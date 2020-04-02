from rest_framework import serializers
from eicapp.models import Slide, Sector, NewsEvent, Incentive, CountryProfile, Service, Email, ChinesePage
from django.contrib.auth.models import User
import json

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']

class SectorSerializer(serializers.ModelSerializer):
    content = serializers.SerializerMethodField()
    class Meta:
        model = Sector
        fields = ['id', 'name','image', 'content']

    def get_content(self, instance):
        if isinstance(instance.content, str):
            return json.decoder.JSONDecoder().decode(instance.content)
        return instance.content

class ChinesePageSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.SerializerMethodField()
    class Meta:
        model = ChinesePage
        fields = ['id', 'image', 'excerpt', 'url', 'name', 'content']
    
    def get_content(self, instance):
        if isinstance(instance.content, str):
            return json.decoder.JSONDecoder().decode(instance.content)
        return instance.content

class NewsEventSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = NewsEvent
        fields = ['id', 'title','url', 'image','content','published']

    def get_content(self, instance):
        if isinstance(instance.content, str):
            return json.decoder.JSONDecoder().decode(instance.content)
        return instance.content

class IncentiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Incentive
        fields = ['id', 'name','description', 'incentive_package','legal_reference','law_section','sector','eligebility','rewarding_authority','implementing_authority','incentive_package']


class CountryProfileSerializer(serializers.HyperlinkedModelSerializer):
    content = serializers.SerializerMethodField()
    class Meta:
        model = CountryProfile
        fields = ['id', 'name', 'content']
    
    def get_content(self, instance):
        if isinstance(instance.content, str):
            return json.decoder.JSONDecoder().decode(instance.content)
        return instance.content

class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'sender', 'subject', 'message']

class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Service
        fields = ['id','ServiceId', 'Name', 'NameEnglish', 'DisplayName','DisplayNameEnglish', 'Abbreviation', 'Requirements']
        
class SlideSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Slide
        fields = ['id','caption', 'url', 'screen_id', 'argument']
        
