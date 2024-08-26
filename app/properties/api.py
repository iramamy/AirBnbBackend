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
    serializer = serializers.PropertyListSerializers(
        properties,
        many=True,
    )

    return Response({"data": serializer.data})


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def properties_detail(request, pk):
    property = models.Property.objects.get(pk=pk)
    serializer = serializers.PropertyDetailSerializers(
        property,
        many=False,
    )

    return Response(serializer.data)


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


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def property_reservation(request, pk):
    property = models.Property.objects.get(pk=pk)
    reservations = property.reservations.all()
    serializer = serializers.ReservationListSerializer(reservations, many=True)

    return Response(serializer.data)


@api_view(["POST"])
def book_property(request, pk):
    try:

        start_date = request.POST.get("start_date", "")
        end_date = request.POST.get("end_date", "")
        number_of_nights = request.POST.get("number_of_nights", "")
        total_price = request.POST.get("total_price", "")
        guests = request.POST.get("guests", "")

        property = models.Property.objects.get(pk=pk)

        models.Reservation.objects.create(
            property=property,
            start_date=start_date,
            end_date=end_date,
            number_of_nights=number_of_nights,
            total_price=total_price,
            guests=guests,
            created_by=request.user,
        )

        return Response({"success": True})

    except Exception as e:
        print("Error", e)

        return Response({"success": False})
