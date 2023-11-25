from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import QuestionSerializers, ChoiceSerializers
from .models import Question, Choice

class Question_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        question = Question.objects.all()
        serializer = QuestionSerializers(question, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Choice_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        choice = Question.objects.all()
        serializer = ChoiceSerializers(question, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChoiceSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
