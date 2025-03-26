# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Articles(models.Model):
    author = models.CharField(max_length=1000, blank=True, null=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    urltoimage = models.CharField(db_column='urlToImage', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    publishedat = models.CharField(db_column='publishedAt', max_length=200, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=2000, blank=True, null=True)
    category = models.ForeignKey('Category', models.DO_NOTHING, db_column='category', blank=True, null=True)
    source = models.ForeignKey('Sources', models.DO_NOTHING, db_column='source', blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'articles'


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    memo = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        
        db_table = 'category'


class Sources(models.Model):
    source_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    url = models.CharField(max_length=2000, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    language = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:

        db_table = 'sources'
