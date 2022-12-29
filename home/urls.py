from django.urls import path
from . import views

urlpatterns = [
      path('show/',views.Show.as_view(),name='show'),
      path('edit/',views.Edit.as_view(),name='edit'),
      path('form/',views.Form.as_view(),name='form'),
      path('delete/',views.Delete.as_view(),name='delete'),
      path('home/',views.Home.as_view(),name='home'),
      path('enquery/',views.Enquery.as_view(),name='enquery'),
      path('profile/',views.Profile.as_view(),name='profile'),
      path('editprofile/',views.Editprofile.as_view(),name='editprofile'),
      path('staff/',views.Staffs.as_view(),name='staff'),

 ]
 