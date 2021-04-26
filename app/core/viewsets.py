import csv
import io
import json
from typing import Dict

import requests
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from core.utils import handle_pagination

page_number_param = openapi.Parameter(
    "pageNumber",
    openapi.IN_QUERY,
    description="The page number to return",
    type=openapi.TYPE_STRING,
)
page_size_param = openapi.Parameter(
    "pageSize",
    openapi.IN_QUERY,
    description="The number of items to return",
    type=openapi.TYPE_STRING,
)
region_param = openapi.Parameter(
    "region",
    openapi.IN_QUERY,
    description="Region to which the user belongs",
    type=openapi.TYPE_STRING,
)
type_param = openapi.Parameter(
    "type",
    openapi.IN_QUERY,
    description="User type",
    type=openapi.TYPE_STRING,
)
users_response = openapi.Response(description="The eligible users")


def params(query_params: Dict):

    page_number = query_params.get("pageNumber", "1")
    if page_number == "":
        page_number = 1
    page_size = query_params.get("pageSize", "10")
    if page_size == "":
        page_size = 10
    type = query_params.get("type", None)
    region = query_params.get("region", None)
    return page_number, page_size, type, region


class CoreViewSet(viewsets.ViewSet):
    @swagger_auto_schema(
        method="get",
        manual_parameters=[
            page_number_param,
            page_size_param,
            region_param,
            type_param,
        ],
        responses={200: users_response},
    )
    @action(detail=False)
    def json(self, request):
        page_number, page_size, type, region = params(request.query_params)
        req = requests.get(
            "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json"
        )
        results = req.json().get("results")
        data = handle_pagination(
            results, int(page_number), int(page_size), type, region
        )
        return Response(data, status.HTTP_200_OK)

    @swagger_auto_schema(
        method="get",
        manual_parameters=[
            page_number_param,
            page_size_param,
            region_param,
            type_param,
        ],
        responses={200: users_response},
    )
    @action(detail=False)
    def csv(self, request):
        page_number, page_size, type, region = params(request.query_params)
        req = requests.get(
            "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv"
        )
        req.encoding = "utf-8"
        reader = csv.DictReader(io.StringIO(req.text))
        json_data = json.dumps(list(reader))
        results = json.loads(json_data)
        data = handle_pagination(
            results, int(page_number), int(page_size), type, region
        )
        return Response(data, status.HTTP_200_OK)
