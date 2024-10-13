from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(['GET'])
def test_view(request):
    response = f"This is a test."
    return Response({"result": response})

@api_view(['POST'])
def test_view_post(request):
    name = request.data.get('name')
    response = f"This is a test for {name}."
    return Response({"result": response})

@api_view(['POST'])
def compare_texts(request):
    try:
        data1 = request.data.get('data1')
        data2 = request.data.get('data2')
        
        # Check if inputs are JSON
        try:
            json_data1 = json.loads(data1)
            json_data2 = json.loads(data2)
            is_json = True
        except json.JSONDecodeError:
            json_data1 = json_data2 = None
            is_json = False
        
        # Comparison logic
        if is_json:
            result = json_data1 == json_data2
        else:
            result = data1 == data2
        
        return Response({"result": result})
    except Exception as e:
        return Response({"error": str(e)}, status=400)
