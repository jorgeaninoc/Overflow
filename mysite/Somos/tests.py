"""
Created by Framework
This file is where you can create tests for the App
Modified by: Abraham Lemus
Date: 26/10/18
"""
# Import libraries that will be used.
from django.contrib.auth.models import User
from django.test import TestCase, Client
from Somos.models import *
from Comunidades.models import Comunidad
from datetime import datetime as dt
from datetime import timedelta as td
import django



# Test for UC: Consult Mission from "Somos" app
class ConsultMissionTest(TestCase):
    # Function that will be tested.
    def testConsultMission(self):
        # Get a client copy.
        self.client = Client()
        # Get the site from /actividades
        response = self.client.get('/quiensomos')
        # Check if the code return is 301 for success.
        self.assertEqual(response.status_code, 301)

    def testConsultMissionFalse(self):
        # Get a client copy.
        self.client = Client()
        # Get the site from /actividades
        response = self.client.get('/quiensomosZ')
        # Check if the code return is 404 for failure
        self.assertEqual(response.status_code, 404)
