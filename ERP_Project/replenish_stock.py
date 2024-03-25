from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.admin.views.decorators import staff_member_required
from ERP_Project.models.manager2 import warehouse_product
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view


@api_view(['POST'])
@swagger_auto_schema(operation_description="Admin replenishes stock for a product")
def admin_replenish_stock(request, warehouse_product_id, count):
    try:
        product = warehouse_product.objects.get(id=warehouse_product_id)
        product.increase_stock(count)

        return JsonResponse({'status':'success', 'message': f'Successfully replenished stock by {count}'})

    except warehouse_product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product does not exist'}, status=400)

    except ValueError:
        return HttpResponseBadRequest('Invalid input')

