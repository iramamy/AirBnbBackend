from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from . import models
from . import serializers
from . import forms
from useraccount.models import User


@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def properties_list(request):

    # Auth
    try:
        token = request.META["HTTP_AUTHORIZATION"].split("Bearer ")[1]
        token = AccessToken(token=token)
        user_id = token.payload["user_id"]
        user = User.objects.get(pk=user_id)
    except Exception:
        user = None

    favorites = []
    properties = models.Property.objects.all()

    is_favorites = request.GET.get("is_favorites", "")
    landlord_id = request.GET.get("landlord_id", "")

    checkin_date = request.GET.get("checkIn", "")
    checkout_date = request.GET.get("checkOut", "")
    country = request.GET.get("country", "")
    category = request.GET.get("category", "")
    bedrooms = request.GET.get("numBedrooms", "")
    guests = request.GET.get("numGuests", "")

    # filter
    if landlord_id:
        properties = properties.filter(landlord_id=landlord_id)

    if is_favorites:
        properties = properties.filter(favorited__in=[user])

    if checkin_date and checkout_date:
        exact_matches = models.Reservation.objects.filter(
            start_date=checkin_date
        ) | models.Reservation.objects.filter(end_date=checkout_date)

        overlap_matches = models.Reservation.objects.filter(
            start_date__lte=checkin_date, end_date__gte=checkout_date
        )

        all_matches_id = []

        for reservation in exact_matches | overlap_matches:
            all_matches_id.append(reservation.property_id)

        properties = properties.exclude(id__in=all_matches_id)

    if country:
        properties = properties.filter(country=country)

    if category and category != "undefined":
        properties = properties.filter(category=category)

    if bedrooms:
        properties = properties.filter(bedrooms=bedrooms)

    if guests:
        properties = properties.filter(guests=guests)

    serializer = serializers.PropertyListSerializers(
        properties,
        many=True,
    )

    if user:
        for property in properties:
            if user in property.favorited.all():
                favorites.append(property.id)

    return Response(
        {
            "data": serializer.data,
            "favorites": favorites,
        }
    )


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

    except Exception:

        return Response({"success": False})


@api_view(["POST"])
def toggle_favorite(request, pk):
    property = models.Property.objects.get(pk=pk)
    if request.user in property.favorited.all():
        property.favorited.remove(request.user)

        return Response({"is_favorite": False})
    else:
        property.favorited.add(request.user)

        return Response({"is_favorite": True})


@api_view(["POST", "FILES"])
def edit_property(request):

    if request.method == "POST":
        property_id = request.data.get("property_id")
        country = request.data.get("country")
        category = request.data.get("category")
        title = request.data.get("title")
        description = request.data.get("description")
        price_per_night = request.data.get("price_per_night")
        bedrooms = request.data.get("bedrooms")
        guests = request.data.get("guests")
        image = request.FILES.get("image_url")

        property, created = models.Property.objects.get_or_create(
            id=property_id,
            defaults={
                "country": country,
                "category": category,
                "title": title,
                "description": description,
                "price_per_night": price_per_night,
                "bedrooms": bedrooms,
                "guests": guests,
                "image": image,
            },
        )

        if not created:
            property.country = country
            property.category = category
            property.title = title
            property.description = description
            property.price_per_night = price_per_night
            property.bedrooms = bedrooms
            property.guests = guests

            if image:
                property.image = image

            property.save()

        return Response({"success": True})

    else:
        return Response({"success": False})


@api_view(["GET"])
def delete_property(request, pk):
    property = models.Property.objects.get(pk=pk)
    try:
        property.delete()
        return Response({"success": True})

    except property.DoesNotExist:
        return Response({"success": False})


@api_view(["GET"])
def delete_reservation(request, pk):
    reservation = models.Reservation.objects.get(pk=pk)
    try:
        reservation.delete()
        return Response({"success": True})

    except reservation.DoesNotExist:
        return Response({"success": False})
