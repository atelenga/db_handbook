# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DistrictDic'
        db.create_table('mainapp_districtdic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mainapp', ['DistrictDic'])

        # Adding model 'AddressDic'
        db.create_table('mainapp_addressdic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.DistrictDic'])),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=600)),
        ))
        db.send_create_signal('mainapp', ['AddressDic'])

        # Adding model 'DistrictAdmInfo'
        db.create_table('mainapp_districtadminfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.DistrictDic'])),
            ('adm_chief_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('occupation', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal('mainapp', ['DistrictAdmInfo'])

        # Adding model 'PrecinctDic'
        db.create_table('mainapp_precinctdic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.AddressDic'])),
            ('precinct', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mainapp', ['PrecinctDic'])

        # Adding model 'SenatorsDic'
        db.create_table('mainapp_senatorsdic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('precinct', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.PrecinctDic'])),
            ('senator_name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal('mainapp', ['SenatorsDic'])

        # Adding model 'LocalPolicemenDic'
        db.create_table('mainapp_localpolicemendic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.AddressDic'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mainapp', ['LocalPolicemenDic'])

        # Adding model 'LocalPolicemenInfo'
        db.create_table('mainapp_localpolicemeninfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.LocalPolicemenDic'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
        ))
        db.send_create_signal('mainapp', ['LocalPolicemenInfo'])

        # Adding model 'PoliclinicDic'
        db.create_table('mainapp_policlinicdic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('p_address', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('chief', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mainapp', ['PoliclinicDic'])

        # Adding model 'PoliclinicInfo'
        db.create_table('mainapp_policlinicinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.AddressDic'])),
            ('policlinic', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.PoliclinicDic'])),
        ))
        db.send_create_signal('mainapp', ['PoliclinicInfo'])

        # Adding model 'HouseManagementDic'
        db.create_table('mainapp_housemanagementdic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('h_address', self.gf('django.db.models.fields.CharField')(max_length=600)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('chief', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('mainapp', ['HouseManagementDic'])

        # Adding model 'HouseManagementInfo'
        db.create_table('mainapp_housemanagementinfo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.AddressDic'])),
            ('hm', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mainapp.HouseManagementDic'])),
        ))
        db.send_create_signal('mainapp', ['HouseManagementInfo'])

    def backwards(self, orm):
        # Deleting model 'DistrictDic'
        db.delete_table('mainapp_districtdic')

        # Deleting model 'AddressDic'
        db.delete_table('mainapp_addressdic')

        # Deleting model 'DistrictAdmInfo'
        db.delete_table('mainapp_districtadminfo')

        # Deleting model 'PrecinctDic'
        db.delete_table('mainapp_precinctdic')

        # Deleting model 'SenatorsDic'
        db.delete_table('mainapp_senatorsdic')

        # Deleting model 'LocalPolicemenDic'
        db.delete_table('mainapp_localpolicemendic')

        # Deleting model 'LocalPolicemenInfo'
        db.delete_table('mainapp_localpolicemeninfo')

        # Deleting model 'PoliclinicDic'
        db.delete_table('mainapp_policlinicdic')

        # Deleting model 'PoliclinicInfo'
        db.delete_table('mainapp_policlinicinfo')

        # Deleting model 'HouseManagementDic'
        db.delete_table('mainapp_housemanagementdic')

        # Deleting model 'HouseManagementInfo'
        db.delete_table('mainapp_housemanagementinfo')

    models = {
        'mainapp.addressdic': {
            'Meta': {'object_name': 'AddressDic'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.DistrictDic']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mainapp.districtadminfo': {
            'Meta': {'object_name': 'DistrictAdmInfo'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'adm_chief_name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.DistrictDic']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'mainapp.districtdic': {
            'Meta': {'object_name': 'DistrictDic'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mainapp.housemanagementdic': {
            'Meta': {'object_name': 'HouseManagementDic'},
            'chief': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'h_address': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'mainapp.housemanagementinfo': {
            'Meta': {'object_name': 'HouseManagementInfo'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.AddressDic']"}),
            'hm': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.HouseManagementDic']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'mainapp.localpolicemendic': {
            'Meta': {'object_name': 'LocalPolicemenDic'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.AddressDic']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mainapp.localpolicemeninfo': {
            'Meta': {'object_name': 'LocalPolicemenInfo'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.LocalPolicemenDic']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'mainapp.policlinicdic': {
            'Meta': {'object_name': 'PoliclinicDic'},
            'chief': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'p_address': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'mainapp.policlinicinfo': {
            'Meta': {'object_name': 'PoliclinicInfo'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.AddressDic']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'policlinic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.PoliclinicDic']"})
        },
        'mainapp.precinctdic': {
            'Meta': {'object_name': 'PrecinctDic'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.AddressDic']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precinct': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mainapp.senatorsdic': {
            'Meta': {'object_name': 'SenatorsDic'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '600'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'precinct': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mainapp.PrecinctDic']"}),
            'senator_name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['mainapp']