# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'News'
        db.create_table('news_news', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('posted_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('news', ['News'])

        # Adding model 'Article'
        db.create_table('news_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('news', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['news.News'])),
            ('views', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('posted_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('news', ['Article'])


    def backwards(self, orm):
        
        # Deleting model 'News'
        db.delete_table('news_news')

        # Deleting model 'Article'
        db.delete_table('news_article')


    models = {
        'news.article': {
            'Meta': {'object_name': 'Article'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'news': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['news.News']"}),
            'posted_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'views': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'news.news': {
            'Meta': {'object_name': 'News'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posted_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'})
        }
    }

    complete_apps = ['news']
