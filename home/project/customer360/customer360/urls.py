from django.contrib import admin
from django.urls import path, include
from customer360 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('create/',views.create_customer,name='create_customer'),
    path('interact/<int:cid>',views.interact,name='interact'),
    path('summary/',views.summary,name='summary'),
    
    # Online Course URLs
    path('courses/', views.course_list, name='course_list'),
    path('course/<int:course_id>/', views.course_details_bootstrap, name='course_details'),
    path('course/<int:course_id>/submit/', views.submit, name='submit'),
    path('submission/<int:submission_id>/result/', views.show_exam_result, name='show_exam_result'),
    
    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),
]
