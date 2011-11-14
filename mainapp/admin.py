from django.contrib import admin
from mainapp.models import *

class AddressDicAdmin(admin.ModelAdmin):
	search_fields = ['district__name', 'address']

admin.site.register(AddressDic, AddressDicAdmin)
admin.site.register(DistrictDic)
admin.site.register(SettlementDic)
admin.site.register(DistrictAdmInfo)
admin.site.register(PrecinctInfo)
admin.site.register(PrecinctDic)
admin.site.register(SenatorsDic)
admin.site.register(PoliceDistrictInfo)
admin.site.register(LocalPolicemenDic)
admin.site.register(LocalPolicemenInfo)
admin.site.register(PoliclinicDic)
admin.site.register(PoliclinicInfo)
admin.site.register(HouseManagementDic)
admin.site.register(HouseManagementInfo)
