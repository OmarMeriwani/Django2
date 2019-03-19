from django.db import models
from elasticsearch import Elasticsearch
import datetime
import os
from django.utils import timezone

#root - 12345 MariaD
class TextService(models.Model):
    Requestor =  models.IntegerField()
    Provider = models.IntegerField()
    Req_Date = models.DateField('Request date')
    def __str__(self):
        return self.Req_Title

class Requestor(models.Model):
    ID = models.IntegerField()
