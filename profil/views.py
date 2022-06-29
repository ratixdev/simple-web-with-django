from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("NIM: 2012014 Nama: Asriani Alim Jurusan: S1 Teknologi Informasi")
