from django.urls import path
import basket.views as basket

app_name = 'basket'
urlpatterns = [
    path('', basket.view, name='basket'),
    path('add/<int:pk>/', basket.add, name='add'),

]