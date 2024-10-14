from rest_framework import routers
from teste.viewsets import ProductViewSet, ClientViewSet, EmployeeViewSet, SaleViewSet

router = routers.DefaultRouter()

router.register('client', ClientViewSet)
router.register('product', ProductViewSet)
router.register('employee', EmployeeViewSet)
router.register('sale', SaleViewSet)

urlpatterns = router.urls