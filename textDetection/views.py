from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# import tensorflow as tf
# import numpy as np
# import PIL
# model = tf.keras.models.load_model('C:/Users/Admin/PycharmProjects/DjangoRESTpractice/AIDetectionProject/AiDetect/textDetection/model')

# Create your views here.
@api_view(['POST'])
def postText(request):
    file = request.data['text']

    return Response(f"your text was {file}")