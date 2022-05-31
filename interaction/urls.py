from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('classroom_list/', views.classroom_list, name="classroom_list"),
    path('classroom_list/<int:classroom_pk>/', views.student_list, name="student_list"),
    path('checkout/<int:student_pk>', views.checkout, name="checkout"),
    path('checkout/success/', views.success_checkout, name='success_checkout'),
]
