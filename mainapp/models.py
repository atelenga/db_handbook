# encoding: utf-8

from django.db import models

class DistrictDic(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название адм. округа')
    class Meta:
		verbose_name='Список адм. округов'
		verbose_name_plural='Список адм. округов'
		ordering = ['name']
    def __unicode__(self):
		return self.name
	
class SettlementDic(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название нас. пункта')
    class Meta:
		verbose_name='Список нас. пунктов'
		verbose_name_plural='Список нас. пунктов'
		ordering = ['name']
    def __unicode__(self):
		return self.name


class AddressDic(models.Model):
    district = models.ForeignKey(DistrictDic, verbose_name='Адм. округ')    
    settlement = models.ForeignKey(SettlementDic, verbose_name='Населённый пункт')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house = models.CharField(max_length=4, verbose_name='Дом')
    building = models.CharField(max_length=4, verbose_name='Корпус/строение', blank=True, null=True)
    class Meta:
		verbose_name='Список адресов'
		verbose_name_plural='Список адресов'
		ordering = ['street']
    def __unicode__(self):
		return u'%s %s %s %s %s' %(self.district, self.settlement, self.street, self.house, self.building)

class DistrictAdmInfo(models.Model):
    district = models.ForeignKey(DistrictDic, verbose_name='Адм. округ')
    adm_chief_name = models.CharField(max_length=256, verbose_name='Имя главы')
    occupation = models.CharField(max_length=256, verbose_name='Должность')
    address = models.CharField(max_length=600, verbose_name='Адрес')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    class Meta:
		verbose_name='Информация о главах адм. округов'
		verbose_name_plural='Информация о главах адм. округов'
		ordering = ['district']
    def __unicode__(self):
		return u'%s %s %s %s %s' %(self.district, self.adm_chief_name, self.occupation, self.address, self.phone)

class PrecinctInfo(models.Model):
	name = models.CharField(max_length=100, verbose_name='Название избир. округа')
	class Meta:
		verbose_name='Информация об избирательных округах'
		verbose_name_plural='Информация об избирательных округах'
		ordering = ['name']
	def __unicode__(self):
		return u'%s' %(self.name)
		
class PrecinctDic(models.Model):
	address = models.ForeignKey(AddressDic, verbose_name='Адрес')
	precinct = models.ForeignKey(PrecinctInfo, verbose_name='Название избир. округа')
	class Meta:
		verbose_name='Список избирательных округов'
		verbose_name_plural='Список избирательных округов'
		ordering = ['precinct']
	def __unicode__(self):
		return u'%s %s' %(self.address, self.precinct)

class SenatorsDic(models.Model):
    precinct = models.ForeignKey(PrecinctInfo, verbose_name='Название избир. округа')
    senator_name = models.CharField(max_length=256, verbose_name='Имя депутата')
    address = models.CharField(max_length=600, verbose_name='Адрес')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    class Meta:
		verbose_name='Информация о депутатах Гор. Думы'
		verbose_name_plural='Информация о депутатах Гор. Думы'
		ordering = ['senator_name']
    def __unicode__(self):
		return u'%s %s %s %s' %(self.precinct, self.senator_name, self.address, self.phone)

class PoliceDistrictInfo(models.Model):
	name = models.CharField(max_length=100, verbose_name='Название полиц. участка')
	class Meta:
		verbose_name='Информация о полицейских участках'
		verbose_name_plural='Информация о полицейских участках'
		ordering = ['name']
	def __unicode__(self):
		return u'%s' %(self.name)

class LocalPolicemenDic(models.Model):
    address = models.ForeignKey(AddressDic, verbose_name='Адрес')
    name = models.ForeignKey(PoliceDistrictInfo, verbose_name='Название полиц. участка')
    class Meta:
		verbose_name='Список полицейских участков'
		verbose_name_plural='Список полицейских участков'
		ordering = ['name']
    def __unicode__(self):
		return u'%s %s' %(self.address, self.name)

class LocalPolicemenInfo(models.Model):
    district = models.ForeignKey(PoliceDistrictInfo,verbose_name='Полиц. участок')
    name = models.CharField(max_length=256, verbose_name='Имя участкового')
    address = models.CharField(max_length=600, verbose_name='Адрес')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    class Meta:
		verbose_name='Информация об участковых'
		verbose_name_plural='Информация об участковых'
		ordering = ['district']
    def __unicode__(self):
		return u'%s %s %s %s' %(self.district, self.name, self.address, self.phone)
	
class PoliclinicDic(models.Model):    
    name = models.CharField(max_length=256, verbose_name='Название поликлиники')
    p_address = models.CharField(max_length=600, verbose_name='Адрес')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    chief = models.CharField(max_length=100, verbose_name='Имя главврача')
    class Meta:
		verbose_name='Информация о поликлиниках'
		verbose_name_plural='Информация о поликлиниках'
		ordering = ['name']
    def __unicode__(self):
		return u'%s %s %s %s' %(self.name, self.p_address, self.phone, self.chief)
		
class PoliclinicInfo(models.Model):
    address = models.ForeignKey(AddressDic, verbose_name='Адрес')
    policlinic = models.ForeignKey(PoliclinicDic, verbose_name='Поликлиника')
    class Meta:
		verbose_name='Список поликлиник'
		verbose_name_plural='Список поликлиник'
		ordering = ['address']
    def __unicode__(self):
		return u'%s %s' %(self.address, self.policlinic)

class HouseManagementDic(models.Model):    
    name = models.CharField(max_length=256, verbose_name='Название упр. компании')
    h_address = models.CharField(max_length=600, verbose_name='Адрес')
    phone = models.CharField(max_length=12, verbose_name='Телефон')
    chief = models.CharField(max_length=100, verbose_name='Имя руководителя')
    class Meta:
		verbose_name='Информация об управляющих компаниях'
		verbose_name_plural='Информация об управляющих компаниях'
		ordering = ['name']
    def __unicode__(self):
		return u'%s %s %s %s' %(self.name,  self.h_address, self.phone, self.chief)
	
class HouseManagementInfo(models.Model):
    address = models.ForeignKey(AddressDic, verbose_name='Адрес')
    hm = models.ForeignKey(HouseManagementDic, verbose_name='Управляющая компания')
    class Meta:
		verbose_name='Список управляющих компаний'
		verbose_name_plural='Список управляющих компаний'
		ordering = ['address']
    def __unicode__(self):
		return u'%s %s' %(self.address, self.hm)	
