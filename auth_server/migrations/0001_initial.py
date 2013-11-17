# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AuthenticationLog'
        db.create_table(u'auth_server_authenticationlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('client_information', self.gf('jsonfield.fields.JSONField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'auth_server', ['AuthenticationLog'])


    def backwards(self, orm):
        # Deleting model 'AuthenticationLog'
        db.delete_table(u'auth_server_authenticationlog')


    models = {
        u'auth_server.authenticationlog': {
            'Meta': {'object_name': 'AuthenticationLog'},
            'client_information': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['auth_server']