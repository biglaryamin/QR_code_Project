import datetime
from datetime import date
from django.shortcuts import render
from qr_code.qrcode.utils import MeCard, VCard, EpcData, VEvent, EventClass, EventTransparency, EventStatus, WifiConfig, Coordinates, QRCodeOptions


def application_qr_code_demo(request):
    # Use a MeCard instance to encapsulate the detail of the contact.
    mecard_contact = MeCard(
        name='Doe, John',
        phone='+41769998877',
        email='j.doe@company.com',
        url='http://www.company.com',
        birthday=date(year=1985, month=10, day=2),
        memo='Development Manager',
        org='Company Ltd'
    )

#     # Use a VCard instance to encapsulate the detail of the contact.
#     vcard_contact = VCard(
#         name='Doe; John',
#         phone='+41769998877',
#         email='j.doe@company.com',
#         url='http://www.company.com',
#         birthday=date(year=1985, month=10, day=2),
#         street='Cras des Fourches 987',
#         city='Delémont',
#         zipcode=2800,
#         region='Jura',
#         country='Switzerland',
#         memo='Development Manager',
#         org='Company Ltd'
#     )

#     # Use a WifiConfig instance to encapsulate the configuration of the connexion.
#     wifi_config = WifiConfig(
#         ssid='my-wifi',
#         authentication=WifiConfig.AUTHENTICATION.WPA,
#         password='wifi-password'
#     )

#     # Use a EpcData instance to encapsulate the data of the European Payments Council Quick Response Code.
#     epc_data = EpcData(
#         name='Wikimedia Foerdergesellschaft',
#         iban='DE33100205000001194700',
#         amount=50.0,
#         text='To Wikipedia'
#     )

#     # Build coordinates instances.
#     google_maps_coordinates = Coordinates(latitude=586000.32, longitude=250954.19)
#     geolocation_coordinates = Coordinates(latitude=586000.32, longitude=250954.19, altitude=500)

#     # Build event data (VEVENT properties)
#     # NB for start and end of event:
#     #   - Naive date and time is rendered as floating time.
#     #   - Aware date and time is rendered as UTC converted time.
#     event = VEvent(
#         uid="some-event-id",
#         summary="Vacations",
#         start=datetime.datetime(2022, 8, 6, hour=8, minute=30),
#         end=datetime.datetime(2022, 8, 17, hour=12),
#         location="New-York, Statue de la Liberté",
#         geo=(40.69216097988203, -74.04460073403436),
#         categories=["PERSO", "holidays"],
#         status=EventStatus.CONFIRMED,
#         event_class=EventClass.PRIVATE,
#         transparency=EventTransparency.OPAQUE,
#         organizer="foo@bar.com",
#         url="https://bar.com",
#         description="""Fake description. Meeting to provide technical review for "Phoenix" design. Happy Face Conference Room.

# Phoenix design team MUST attend this meeting.

# RSVP to team leader."""
#     )
    
    # Build context for rendering QR codes.
    context = dict(
        mecard_contact=mecard_contact,
        # vcard_contact=vcard_contact,
        # wifi_config=wifi_config,
        # epc_data=epc_data,
        # event=event,
        # video_id='J9go2nj6b3M',
        # google_maps_coordinates=google_maps_coordinates,
        # geolocation_coordinates=geolocation_coordinates,
        # options_example=QRCodeOptions(size='t', border=6, error_correction='L'),
    )

    # Render the index page.
    return render(request, 'index.html', context=context)
