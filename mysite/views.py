from django.shortcuts import render
from .models import Work, Official_Bio, Nodanews_Description, Agency, Meeting

def work(request):
    works = Work.objects.all().order_by('-date_finished')
    offbios = Official_Bio.objects.all()
    nodas = Nodanews_Description.objects.all()
    mtcs = Meeting.objects.filter( agency=1 ).order_by("-date")[0:5]
    baaqmds = Meeting.objects.filter( agency=2 ).order_by("-date")[0:5]
    abags = Meeting.objects.filter( agency=3 ).order_by("-date")[0:5]
    casas = Meeting.objects.filter( agency=4 ).order_by("-date")[0:5]
    barcs = Meeting.objects.filter( agency=5 ).order_by("-date")[0:5]
    return render(request, 'index.html', {'works': works, 'offbios': offbios, 'nodas': nodas, 'mtcs': mtcs, 'baaqmds': baaqmds, 'abags': abags, 'casas': casas, 'barcs': barcs})
