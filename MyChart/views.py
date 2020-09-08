from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
# These imports are for django rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model

User = get_user_model()


# Here we are getting data as HTTP Response from django
class Homeview(View):
    def get(self, request, *args):
        return render(request, 'charts.html', {'Customer': 20})


# Let's create a function based view
def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)  # It's also a HTTP Response, but only type JSON


class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['User', 'Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_items = [qs_count, 12562, 15224, 45632, 789, 44565, 5236]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)
