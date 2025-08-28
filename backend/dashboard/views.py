from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import requests
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
        })

@api_view(['GET'])
@permission_classes([IsAuthenticated])   # 👈 require login
def hello_view(request):
    return JsonResponse({"message": f"Hello, {request.user.username}!"})
# 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def worldbank_data(request):
    # Get parameters from frontend with defaults
    indicator = request.GET.get('indicator', 'SP.POP.TOTL')  # Population total
    country = request.GET.get('country', 'IN')  # India
    start_year = request.GET.get('start', '2010')
    end_year = request.GET.get('end', '2023')
    
    # Build World Bank API URL
    url = f"http://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json&date={start_year}:{end_year}&per_page=100"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # World Bank returns [metadata, actual_data]
        if isinstance(data, list) and len(data) >= 2:
            actual_data = data[1]
            
            # Process the data for better frontend usage
            processed_data = []
            for item in actual_data:
                if item.get('value') is not None:
                    processed_data.append({
                        'year': item.get('date'),
                        'value': item.get('value'),
                        'country': item.get('country', {}).get('value', ''),
                        'indicator': item.get('indicator', {}).get('value', '')
                    })
            
            # Sort by year
            processed_data.sort(key=lambda x: x['year'])
            
            return JsonResponse(processed_data, safe=False)
        else:
            return JsonResponse({"error": "No data available from World Bank"}, status=404)
            
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": f"World Bank API error: {str(e)}"}, status=500)
    except Exception as e:
        return JsonResponse({"error": f"Server error: {str(e)}"}, status=500)