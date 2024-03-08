from django.urls import path
from . import views  
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('categories', views.CategoryViewSet)
urlpatterns = router.urls
    


# urlpatterns = [
#    path('ProductList', views.ApiProducts.as_view(), name='ProductList'),
#    path('Productdetail/<str:pk>/', views.ApiProductDetail.as_view(), name='Productdetail'),
#    path('categories', views.ApiCategories.as_view(), name='categories'),
#    path('categorydetail/<str:pk>/', views.ApiCategroydetail.as_view(), name='categorydetail')
# ]
