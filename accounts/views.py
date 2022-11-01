# from django.shortcuts import render
# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView, GenericAPIView
# from rest_framework.response import Response
# from rest_framework import mixins, status
# from rest_framework.views import APIView
# from rest_framework.exceptions import ValidationError
# from .serializers import UserSerializer
# from .models import User
#
#
#
# class UserListMixinGenericAPIView(GenericAPIView, mixins.ListModelMixin):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#
# class UserListCreateAPIView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def post(self, request, *args, **kwargs):
#         data = request.data
#         serializer = UserSerializer(data=data, context={'nimadir': 'biron_nima'})
#         # print(111, serializer.data)   # bu bor
#         # print(222, serializer.initial_data)   #bu mavjud emas hozir
#         # print(333, serializer.validated_data)    #bu ishlashi uchun is_valid ishlashi kerak avval
#         serializer.is_valid(raise_exception=True)
#         # print(111111, serializer.data)  #bu serializer.save() qilingandan keyin mavjud bo`ladi
#         print(222222, serializer.initial_data)
#         print(333333, serializer.validated_data)
#         user = serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class UserDetailAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def get(self, request, *args, **kwargs):
#         user = self.get_object()
#         serializer = UserSerializer(user, context={'nimadir':'biron_nima'})
#         user_data = serializer.data
#         return Response(user_data, status=status.HTTP_200_OK)
