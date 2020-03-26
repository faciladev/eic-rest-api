from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

class NewsEvent(models.Model):
    image = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    content = ArrayField(models.TextField(blank=True, null=True))
    published = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.title

    class Meta:
        managed = True
        db_table = 'news_events'

class Sector(models.Model):
    image = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    content = JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'sectors'


class Incentive(models.Model):
    name = ArrayField(models.TextField(blank=True, null=True))
    description = ArrayField(models.TextField(blank=True, null=True))
    incentive_package = models.TextField(blank=True, null=True)
    legal_reference = ArrayField(models.TextField(blank=True, null=True))
    law_section = ArrayField(models.TextField(blank=True, null=True))
    sector = ArrayField(models.TextField(blank=True, null=True))
    eligebility = ArrayField(models.TextField(blank=True, null=True))
    rewarding_authority = ArrayField(models.TextField(blank=True, null=True))
    implementing_authority = ArrayField(models.TextField(blank=True, null=True))
    incentive_package = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return "".join(self.name)

    class Meta:
        managed = True
        db_table = 'incentives'

class CountryProfile(models.Model):
    name = models.TextField(blank=True, null=True)
    content = JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'country_profiles'

class Service(models.Model):
    ServiceId = models.TextField(blank=True, null=True)
    Name = models.TextField(blank=True, null=True)
    NameEnglish = models.TextField(blank=True, null=True)
    DisplayName = models.TextField(blank=True, null=True)
    DisplayNameEnglish = models.TextField(blank=True, null=True)
    Abbreviation = models.TextField(blank=True, null=True)
    Requirements = JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.NameEnglish

    class Meta:
        managed = True
        db_table = 'services'

class ChinesePage(models.Model):
    image = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    excerpt = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    content = JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'chinese_page'

class Email(models.Model):
    sender = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.sender} > {self.subject}'

    class Meta:
        managed = True
        db_table = 'emails'