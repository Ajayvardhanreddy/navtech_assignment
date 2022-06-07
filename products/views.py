import json
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pandas as pd
from .models import Products


@api_view(['POST'])
def user_create_order(request):
    """
    (FOR USERS)
    This view method takes POST request, extracts orders from it and store in the database.
    :param request:
    :return:
    """
    product_orders = json.loads(json.dumps(request.data))
    if product_orders:
        for each_order in product_orders['orders']:
            each_order_obj = Products(
                product_name=each_order['product_name'],
                price=each_order['price'],
                ordered_quantity=each_order['ordered_quantity'],
                total_amount=each_order['total_amount']
            )
            each_order_obj.save()
        return Response({
            'status': 'CREATED 201',
            'message': "Successfully added!"
        })
    return Response({
            'status': '404',
            'message': "POST request is Empty!"
        })


@api_view(['POST'])
def admin_create_order(request):
    """
    (ONLY FOR ADMIN)
    This view method takes CSV file as a POST request, extracts orders from it and store in the database or if order exists, then updates the price.
    :param request:
    :return:
    """
    print(request.data['orders'])
    if request.data['orders']:
        product_orders = pd.read_csv(request.data['orders'])
        is_data_exists = False
        for each_row in product_orders.itertuples():
            is_data_exists = True
            try:
                product_exists = Products.objects.get(product_name=each_row[2])
            except ObjectDoesNotExist:
                product_exists = None
            print(product_exists)
            if product_exists:
                product_exists.price = each_row[3]
                product_exists.total_amount = product_exists.ordered_quantity*each_row[4]
                product_exists.save()
                continue
            each_order_obj = Products(
                product_name=each_row[2],
                price=each_row[3],
                ordered_quantity=each_row[4],
                total_amount=each_row[5]
            )
            each_order_obj.save()

        if not is_data_exists:
            return Response({
                'status': '404',
                'message': "CSV file is empty!"
            })
        return Response({
            'status': 'CREATED 201',
            'message': "Successfully added multiple orders from CSV file!"
        })
    return Response({
        'status': '404',
        'message': "No csv file found!"
    })


@api_view(['GET'])
def admin_get_orders(request):
    products_list = Products.objects.all()
    if products_list:
        orders = []
        for each_prod in products_list:
            orders.append({
                "product_name": each_prod.product_name,
                "price": each_prod.price,
                "ordered_quantity": each_prod.ordered_quantity,
                "total_amount": each_prod.total_amount
            })
        return Response({'orders': orders})
    return Response({
        'status': '404',
        'message': "Database is empty!"
    })
