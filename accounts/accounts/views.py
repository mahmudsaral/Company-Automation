from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect
from .models import *
from .forms import OrderForm, CreateUserForm ,FbfForm ,SignupForm ,PostFilterForm  ,AddMemberForm ,EventForm ,KontrolForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
from datetime import datetime  
from datetime import timedelta 
from django.template.loader import get_template
from io import BytesIO 
from django.views import View
from xhtml2pdf import pisa
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import EventForm, AddMemberForm
from django.views import generic
from datetime import date
from datetime import timedelta
import calendar
from django.utils.safestring import mark_safe
from .models import Event ,Denetci_9001
from .utils import Calendar 
from django.db.models import Q
from .filters import SnippetFilter 
from django.views.generic import ListView
from django.http import HttpResponse
from django.utils import timezone
from django.utils.timezone import localtime, get_current_timezone

def render_to_pdf(template_src, context_dict={}): 
    
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.replace(u'\u2013', '-').replace(u'\u0130', 'i').replace(u'\u015f', 's').replace(u'\u0131', 'i').replace(u'\u015e', 'S').replace(u'\u011f', 'g').replace(u'\u015e', '-').replace(u'\u015e', '-').replace(u'\u011e', '-').encode('cp1252')),result)	
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        order = get_object_or_404(firma,pk=pk)	
        order = firma.objects.filter(id=pk)
        data = {'order':order}
        pdf = render_to_pdf('accounts/pdf_template.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):
        
        pdf = render_to_pdf('accounts/pdf_template.html', data)
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response	

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                    login(request, user)
                    return redirect('dashboard')
            else:
                messages.info(request, 'Username OR password is incorrect')
                

        context = {}
        return render(request, 'accounts/login.html',context)
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')

def all(request):
    all = firma.objects.all()
    Kontrol = kontrol.objects.all()
    deneme = Denetci_9001.objects.all()
    context = {'all':all,'deneme':deneme,'Kontrol':Kontrol}
    return render(request, 'accounts/all.html',context)


@login_required(login_url='login')

def home(request):

    orders = Order.objects.all()
    firmas = firma.objects.all().order_by('-CA_Date')
    total_firmas = firmas.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders, 'firmas':firmas,
    'total_firmas':total_firmas,'delivered':delivered,
    'pending':pending }
    return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login')
def firmas(request, pk_test):
    firmas = firma.objects.filter(id=pk_test)
    context = {'firmas':firmas}
    return render(request, 'accounts/firmas.html',context)

@login_required(login_url='login')
def customer(request):
    
    orders = Order.objects.all()
    firmas = firma.objects.all().order_by('-CA_Date')
    total_firmas = firmas.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'firmas':firmas,
    'total_firmas':total_firmas,'delivered':delivered,
    'pending':pending }
    return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def SuspensionOrder(request,pk):
    order = firma.objects.filter(id=pk)
    context = {'order':order}
    return render(request, 'accounts/askı_form.html', context)
    
@login_required(login_url='login')
def updateOrder(request, pk):
    order = firma.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST ,instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)
@login_required(login_url='login')
def deleteOrder(request,pk):
    order = firma.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html', context)
@login_required(login_url='login')
def suspension(request):
    suspension = firma.objects.all()
    context = {'suspension':suspension,'firmas':firmas}
    return render(request,'accounts/suspension.html', context)

@login_required(login_url='login')
def withdrawal(request):
    withdrawal = firma.objects.all()
    context = {'withdrawal':withdrawal,'firmas':firmas}
    return render(request,'accounts/withdrawal.html', context)

@login_required(login_url='login')
def FBF(request):
    FBF = fbf.objects.all()
    context = {'FBF':FBF}
    return render(request, 'accounts/fbf.html', context)

@login_required(login_url='login')
def createFbf(request):
    form = FbfForm()
    if request.method == 'POST':
        form = FbfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/fbf_form.html', context)

@login_required(login_url='login')
def update_fbf(request,pk1):
    FBF = fbf.objects.get(id=pk1)
    form = FbfForm(instance=FBF)
    if request.method == 'POST':
        form = FbfForm(request.POST ,instance=FBF)
        if form.is_valid():
            form.save()
            return redirect('/fbf/')
    context = {'form':form}
    return render(request, 'accounts/fbf_form.html', context)

@login_required(login_url='login')
def FbfOrder(request,pk_fbf):
    FBF = fbf.objects.filter(id=pk_fbf)
    context = {'FBF':FBF}
    return render(request, 'accounts/fbf_form_css.html', context)



class Viewpdf(View):
    def get(self, request, *args, **kwargs):
        pk_fbf = kwargs.get('pk_fbf')
        FBF = get_object_or_404(fbf,pk=pk_fbf)	
        FBF= fbf.objects.filter(id=pk_fbf)
        data = {'FBF':FBF}
        pdf = render_to_pdf('accounts/pdf_fbf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def set_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


@login_required(login_url='login')
def Denetci_list_9001(request,pk2):
    listsend = request.POST.get('listsend', '') == 'on'
    noww = timezone.localtime(timezone.now())
    event = Event.objects.filter(id=pk2)
    d = set_date(request.GET.get('month', None))
    today =  datetime.now()
    Kontrol = kontrol.objects.filter(id=pk2)
    Denetci_list_9001 = Denetci_9001.objects.filter(id=pk2)
    D9 = Denetci_9001.objects.all()
    FBF = fbf.objects.all()
    myFilter = SnippetFilter(request.GET, queryset=D9)
    model = Event
    context_object_name = 'event'
    D9 = myFilter.qs
    if request.method == "POST":
        request.POST.getlist('listsend')    
    context = {'Denetci_list_9001':Denetci_list_9001 ,'FBF':FBF ,'D9':D9 ,'myFilter':myFilter,'Kontrol':Kontrol,'event':event, 'today':today,'noww':noww}
    return render(request, 'accounts/9001.html',context)

    @property
    def is_past_due(self):
        return timezone.now()
    


@login_required(login_url='login')
def DenetimProgram(request,pk1):

    dp= fbf.objects.filter(id=pk1)
    Denetci_list_9001 = Denetci_9001.objects.all()
    context = {'dp':dp,'Denetci_list_9001':Denetci_list_9001}
    return render(request, 'accounts/dp.html', context)


def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

class CalendarView( generic.ListView):
    
    model = Event
    template_name = 'accounts/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        D9 = Denetci_9001.objects.all()
        context = {'D9':D9}
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context


def create_event(request):
    form = EventForm(request.POST or None)
    if request.POST and form.is_valid():
        Personel_Adı = form.cleaned_data['Personel_Adı']
        description = form.cleaned_data['description']
        Scope = form.cleaned_data['Scope']
        start_time = form.cleaned_data['start_time']
        end_time = form.cleaned_data['end_time']

        Event.objects.get_or_create(
            user=request.user,
            Personel_Adı=Personel_Adı,
            description=description,
            Scope=Scope,
            start_time=start_time,
            end_time=end_time,
            
        )
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'accounts/event.html', {'form': form})
class EventEdit(generic.UpdateView):
    model = Event
    fields = ['Personel_Adı', 'description','Scope' ,'start_time', 'end_time']
    template_name = 'accounts/event.html'

@login_required(login_url='signup')
def event_details(request, event_id):
    event = Event.objects.get(id=event_id)
    eventmember = EventMember.objects.filter(event=event)
    context = {
        'event': event,
        'eventmember': eventmember
    }
    return render(request, 'accounts/event-details.html', context)


def add_eventmember(request, event_id):
    forms = AddMemberForm()
    if request.method == 'POST':
        forms = AddMemberForm(request.POST)
        if forms.is_valid():
            member = EventMember.objects.filter(event=event_id)
            event = Event.objects.get(id=event_id)
            if member.count() <= 9:
                user = forms.cleaned_data['user']
                EventMember.objects.create(
                    event=event,
                    user=user
                )
                return redirect('calendar')
            else:
                print('--------------User limit exceed!-----------------')
    context = {
        'form': forms
    }
    return render(request, 'accounts/add_member.html', context)



class EventMemberDeleteView(generic.DeleteView):

    model = EventMember 
    template_name = 'accounts/event_delete.html'
    success_url = reverse_lazy('calendar')

@login_required(login_url='login')
def Kapsam(request):
   Denetci_list_9001 = Denetci_9001.objects.all()
   context = {'Denetci_list_9001':Denetci_list_9001}
   filter_form = PostFilterForm(request.GET or None)
   if filter_form.is_valid():
        secme = filter_form.cleaned_data['secme']
        if secme == '1':
                return render(request,'accounts/9001.html',context) 
        if secme == '2':
                return render(request,'accounts/dashboard.html')
        if secme == '3':
                return render(request,'accounts/dashboard.html') 
        if secme == '4':
                return render(request,'accounts/dashboard.html') 
       
      
   return render(request,'accounts/kapsam.html' ,context={'filter_form':filter_form} )

def Kontrol(request):
    form = KontrolForm(request.POST or None)
    if request.POST and form.is_valid():
        end_time = form.cleaned_data['end_time']
