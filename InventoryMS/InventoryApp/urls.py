from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static  # ✅ Import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.product_create_view, name='product_create'),
    path('list/', views.product_list_view, name='product_list'),
    path('update/<int:product_id>/', views.product_update_view, name='product_update'),
    path('delete/<int:product_id>/', views.product_delete_view, name='product_delete'),
]

# ✅ Serve media files in development mode only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
