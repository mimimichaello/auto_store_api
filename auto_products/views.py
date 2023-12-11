from rest_framework.decorators import action
from rest_framework.response import Response
from auto_products.models import Car, Accessory, Category, Basket
from auto_products.serializers import CarSerializer, AccessorySerializer, CategorySerializer, BasketSerializer
from rest_framework import viewsets, filters
from auto_products.permissions import IsAdminOrReadOnly, IsOwnerOfBasket
from rest_framework import permissions
from rest_framework import status


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAdminOrReadOnly, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'model', 'price']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class AccessoryViewSet(viewsets.ModelViewSet):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    permission_classes = (IsAdminOrReadOnly, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'price']


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly, )

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOfBasket)

    @action(detail=True, methods=['post'])
    def add_product(self, request, pk=None):
        basket = self.get_object()
        if basket.user == request.user:
            product_type = request.data.get('product_type')
            product_id = request.data.get('product_id')
            if product_type == 'car':
                product = Car.objects.get(pk=product_id)
                basket.cars.add(product)
            elif product_type == 'accessory':
                product = Accessory.objects.get(pk=product_id)
                basket.accessories.add(product)
            else:
                return Response({"error": "Недопустимый тип продукта"}, status=status.HTTP_400_BAD_REQUEST)
            basket.save()
            serializer = BasketSerializer(basket)
            return Response(serializer.data)
        else:
            return Response({"error": "Вы не имеете доступ к данной корзине"}, status=status.HTTP_403_FORBIDDEN)

    @action(detail=True, methods=['post'])
    def remove_product(self, request, pk=None):
        basket = self.get_object()
        if basket.user == request.user:
            product_type = request.data.get('product_type')
            product_id = request.data.get('product_id')
            if product_type == 'car':
                product = Car.objects.get(pk=product_id)
                basket.cars.remove(product)
            elif product_type == 'accessory':
                product = Accessory.objects.get(pk=product_id)
                basket.accessories.remove(product)
            else:
                return Response({"error": "Недопустимый тип продукта"}, status=status.HTTP_400_BAD_REQUEST)
            basket.save()
            serializer = BasketSerializer(basket)
            return Response(serializer.data)
        else:
            return Response({"error": "Вы не имеете доступ к данной корзине"}, status=status.HTTP_403_FORBIDDEN)

