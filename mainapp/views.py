# Create your views here.
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response
from mainapp.models import *

def search(request):
	error = False	
	if 'q0' and 'q1' and 'q2' in request.GET:
		q3 = request.GET['q3']
		if q3:			
			q0 = request.GET['q0']
			q1 = request.GET['q1']
			q2 = request.GET['q2']
			q3 = request.GET['q3']
			q = q0 + ', ' + q1 + ', ' + q2 + '/' + q3
			a0 = AddressDic.objects.filter(settlement__name__icontains=q0)
			a1 = a0.filter(street__icontains=q1)
			a2 = a1.filter(house__icontains=q2)
			a = a2.get(building__icontains=q3)
						
		else:
			q0 = request.GET['q0']
			q1 = request.GET['q1']
			q2 = request.GET['q2']			
			a0 = AddressDic.objects.filter(settlement__name__icontains=q0)
			a1 = a0.filter(street__icontains=q1)
			a = a1.get(house__icontains=q2)
			q = q0 + ', ' + q1 + ', ' + q2
		if not q:
			error = True
		else:			
			d = DistrictAdmInfo.objects.get(district=a.district)			
			p = PrecinctDic.objects.get(address=a.id)
			s = SenatorsDic.objects.get(precinct=p.precinct)			
			lpd = LocalPolicemenDic.objects.get(address=a.id)			
			lpi = LocalPolicemenInfo.objects.get(district=lpd.name)			
			pd = PoliclinicInfo.objects.get(address=a.id)
			pi = pd.policlinic
			hmd = HouseManagementInfo.objects.get(address=a.id)
			hmi = hmd.hm			
			return render_to_response('search_result.html', 
			{'address':a,
			'query':q, 
			'district':d,
			'senator':s,
			'police':lpi,
			'policlinic':pi,
			'hm':hmi
			})
	return render_to_response('search_form.html',{'error':error})
