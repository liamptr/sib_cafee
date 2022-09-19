from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('foods', views.FoodViewSet, basename='foods')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
router.register('customers', views.CustomerViewSet)
router.register('orders', views.OrderViewSet, basename='orders')

foods_router = routers.NestedDefaultRouter(
    router, 'foods', lookup='food')
foods_router.register('reviews', views.ReviewViewSet,
                         basename='food-reviews')
foods_router.register(
    'images', views.FoodImageViewSet, basename='food-images')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
carts_router.register('items', views.CartItemViewSet, basename='cart-items')

# URLConf
urlpatterns = router.urls + foods_router.urls + carts_router.urls
