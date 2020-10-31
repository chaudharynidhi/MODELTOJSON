from django.core.management.base import BaseCommand
from datetime import datetime
from JsonConverter.models import Users, ActivityPeriod

def create_data():
    a = Users(user_id="W012A3CDE", real_name = "Egon Spengler", tz="America/Los_Angeles")
    a.save()
    a_start_date = datetime(2020, 2, 1, 13, 33)
    a_end_date = datetime(2020, 2, 1, 13, 54)
    a_address = ActivityPeriod(activity_id=a, 
    start_time=a_start_date.strftime("%b %d %Y %I:%M %p"), 
    end_time=a_end_date.strftime("%b %d %Y %I:%M %p"))
    a_address.save()

    b = Users(user_id="W07QCRPA4", real_name = "Glinda Southgood", tz="Asia/Kolkata")
    b.save()
    b_start_date = datetime(2020, 2, 1, 17, 33)
    b_end_date = datetime(2020, 2, 1, 19, 54)
    b_address = ActivityPeriod(activity_id=b, 
    start_time=b_start_date.strftime("%b %d %Y %I:%M %p"), 
    end_time=b_end_date.strftime("%b %d %Y %I:%M %p"))
    b_address.save()

    c_start_date = datetime(2020, 3, 1, 11, 11)
    c_end_date = datetime(2020, 3, 1, 13, 54)
    c_address = ActivityPeriod(activity_id=b, 
    start_time=c_start_date.strftime("%b %d %Y %I:%M %p"), 
    end_time=c_end_date.strftime("%b %d %Y %I:%M %p"))
    c_address.save()


class Command(BaseCommand):
    def handle(self, **options):
        create_data()