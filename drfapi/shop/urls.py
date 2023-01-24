from django.urls import path
from .views import ProductsAPIList, CatalogAPIList, get_img


urlpatterns = [

    path('api/v1/products', ProductsAPIList.as_view()),
    path('api/v1/catalogs', CatalogAPIList.as_view()),
    path('product_pictures/<img_url>', get_img),
    # path('api/v1/auth/', include('rest_framework.urls')),
    # path('api/v1/cabinet/', CabinetAPI.as_view()),
    # path('api/v1/cabinet/<int:pk>/', CabinetUserAPI.as_view()),
]
