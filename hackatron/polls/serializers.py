from rest_framework import serializers
from polls.models import Question, Choice

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question,
        fields = '__all__'
        exclude = ['is_removed']
        #fields = ('question_text', 'pub_date')
        #exclude = ['is_removed', 'created', 'modified']

class ChoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Choice,
        fields = '__all__'
        #fields = ('fields','choice_text','votes')
        #exclude = ['is_removed', 'created', 'modified']
