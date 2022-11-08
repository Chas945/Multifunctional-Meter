from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.gentella_html, name='gentella'),

    # The home page
    path('', views.index, name='index'),

    #path('',views.showdata)

    path('energy/add/', views.add_meter_data, name='add-meter-data'),
    path('control/add/',  views.add_control_data, name='add-control-data'),

    path('control/<int:control_id>/delete/',  views.delete_control_data, name='delete-control-data'),

    path('energy/delete/', views.delete_meter, name='delete-meter')
]
