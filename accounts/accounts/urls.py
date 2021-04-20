from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name ='dashboard'),
    path('all/', views.all, name = 'all'),
    path('firmas/<str:pk_test>', views.firmas, name = 'firmas'),
    path('create_order/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('suspension_order/<str:pk>/', views.SuspensionOrder, name="suspension_order"),
    path('suspension/', views.suspension, name="suspension"),
    path('withdrawal/', views.withdrawal, name="withdrawal"),
    path('pdf_view/<str:pk>/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
    path('fbf/', views.FBF, name="fbf"),
    path('create_fbf/', views.createFbf, name="create_fbf"),
    path('update_fbf/<str:pk1>/', views.update_fbf, name="update_fbf"),
    path('fbf_form_css/<str:pk_fbf>/', views.FbfOrder, name="fbf_form_css"),
    path('pdf_fbf/<str:pk_fbf>/', views.Viewpdf.as_view(), name="pdf_fbf"),
    path('dp/<str:pk1>/', views.DenetimProgram, name="dp"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.create_event, name='event_new'),
    path('event/edit/<int:pk>/', views.EventEdit.as_view(), name='event_edit'),
    path('event/<int:event_id>/details/', views.event_details, name='event-detail'),
    path('add_eventmember/<int:event_id>', views.add_eventmember, name='add_eventmember'),
    path('event/<int:pk>/remove', views.EventMemberDeleteView.as_view(), name="remove_event"),
    path('kapsam/', views.Kapsam, name="kapsam"),
    path('9001/<str:pk2>/', views.Denetci_list_9001, name="9001"),
    
]

