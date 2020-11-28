from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Table






def  Tables(request):
	tables=Table.objects.all()
	context={"tables":tables}
	return render(request,"JsonTables/Tables.html",context)


def XMLTable(request):
	tables=Table.objects.all()
	context={"tables":tables}
	return render(request,"xmlTables/Tables.html",context)