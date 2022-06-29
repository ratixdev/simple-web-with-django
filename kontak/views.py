from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Alamat: Jl.teratai merah blok I.A no.18 RT 31,Kec.Balikpapan selatan Kel.Sepinggan kota Balikpapan Kode pos: 76115")
