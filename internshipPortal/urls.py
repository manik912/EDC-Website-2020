from django.urls import path
from . import views


urlpatterns = [

    path('internships/', 						views.Internships,                      name='internships'),
    path('internships/create/',					views.InternshipCreateView,),
    path('internships/<int:pk>/', 				views.InternshipDetailView,             name='internship-detail'),
    path('internships/<int:pk>/application/', 	views.InternshipApplicationView,        name='internship-application'),
    path('internships/<int:pk>/update/', 		views.InternshipUpdateView.as_view(),   name='internship-update'),
    path('internships/<int:pk>/delete/', 		views.InternshipDeleteView.as_view(),   name='internship-delete'),
    path('venture-capitalist/', 				views.VenCapitalist,                    name='venture-capitalist'), 
    path('venture-capitalist/create/', 			views.VenCapCreateView,                 name='vencap-create'),
    path('venture-capitalist/<int:pk>/update/', views.VenCapUpdateView,                 name='vencap-update'),
    path('venture-capitalist/<int:pk>/delete/', views.VenCapDeleteView.as_view(),       name='vencap-delete'),

    
]