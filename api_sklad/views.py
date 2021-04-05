from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import ResourcesSerializer, PostResourcesSerializer
from .models import Resources


# Create your views here.


class ResourcesApi(APIView):
    # пермишн можно сделать IsAuthenticated
    permission_classes = [AllowAny]

    def get(self, request, format='json'):
        """
        [get]-запрос. Собираем все записи со склада, добавляем поле общей стоимости для кажой позиции
        формируем json, добавляем количество записей
        отдаем ответ
        :param request:
        :param format:
        :return:
        """
        obj_set = Resources.objects.all()
        content = ResourcesSerializer(obj_set, many=True)
        count = obj_set.count()

        for elem in content.data:
            elem['cost'] = elem['amount'] * elem['price']

        json = {
            'resources': content.data,
            'total_count': count,
        }

        return Response(json, status=status.HTTP_200_OK)

    def post(self, request, format='json'):
        """
        [post]-зарос, принимаем json вида:
        {
            "title": "res_3",
            "amount": 1000,
            "unit":  "kg",
            "price": 12,
            "date": "2021-03-20"
        }
        Сериализируем данные, если валидны, то сохраняем и отдаем 201
                            , если не валидны отдаем 400

        :param request:
        :param format:
        :return:
        """
        try:
            serializer = PostResourcesSerializer(data=request.data)
        except Exception as e:
            return Response(data=e, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format='json'):
        """
        [put]-запрос обновления полей, прнимаем json вида
        {
            "id": 4,
            "title": "res_3",
            "amount": 1000,
            "unit":  "kg",
            "price": 12,
            "date": "2021-03-20"
        }
        ищем объект по id из request.data
        проверяем наличие название полей в request.data
        присваиваем соотв полям, сохраняем, отдаем 201

        если объект не найден - отдаем 400


        :param request:
        :param format:
        :return:
        """
        try:
            obj = Resources.objects.get(id=request.data['id'])
            if 'amount' in request.data:
                obj.amount = request.data['amount']
            if 'price' in request.data:
                obj.price = request.data['price']
            if 'date' in request.data:
                obj.date = request.data['date']
            if 'title' in request.data:
                obj.title = request.data['title']
            obj.save()
            return Response(status=status.HTTP_201_CREATED)
        except Resources.DoesNotExist:
            return Response(data='Object does not exist.', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format='json'):
        """
        [delete]-запрос
        принимаем Json вида:
        {
            "id": 4
        }
        ищем объект по id
        удаляем, отдаем 200
        если объекта нет отдаем 400

        :param request:
        :param format:
        :return:
        """
        try:
            obj = Resources.objects.get(id=request.data['id'])
            obj.delete()
            return Response(status=status.HTTP_200_OK)
        except Resources.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TotalView(APIView):
    # пермишн
    permission_classes = [AllowAny]

    def get(self, request, format='json'):
        """
        [get]-запрос собиарем все объекты
        формируем json и отдаем его с 200
        :param request:
        :param format:
        :return:
        """
        all_obj = Resources.objects.all()
        total_cost = 0

        for elem in all_obj:
            total_cost += elem.amount * elem.price

        json = {
            "total_cost": total_cost
        }

        return Response(json, status=status.HTTP_200_OK)