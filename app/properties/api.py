from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from . import models
from . import serializers
from . import forms


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def properties_list(request):
    properties = models.Property.objects.all()
    serializer = serializers.PropertySerializers(
        properties,
        many=True,
    )

    return Response({"data": serializer.data})


@api_view(["POST", "FILES"])
def create_property(request):
    form = forms.PropertyForm(request.POST, request.FILES)

    if form.is_valid():
        new_property = form.save(commit=False)
        new_property.landlord = request.user
        new_property.save()

        return Response({"success": True})
    else:
        print("Form errors", form.errors, form.non_field_errors)
        return Response(
            {"errros": form.errors.as_json()},
            status=status.HTTP_400_BAD_REQUEST,
        )
