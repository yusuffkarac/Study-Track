from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from base.models import (
    Products,
    Days,
    Lectures,
    Activity,
    Studies,
    Grades,
    TransferCodes,
    ProfilePhoto,
)


class ProductsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.product = Products.objects.create(
            name="testproduct", price=20, type="testtype", created_by=self.user
        )

    def test_product_str_method(self):
        product = Products.objects.get(name="testproduct")
        self.assertEqual(product.__str__(), "testproduct")


class DaysTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.day = Days.objects.create(name="testday", created_by=self.user)

    def test_day_str_method(self):
        day = Days.objects.get(name="testday")
        self.assertEqual(day.__str__(), "testday")


class LecturesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.day = Days.objects.create(name="testday", created_by=self.user)
        self.lecture = Lectures.objects.create(
            title="testlecture",
            description="testdescription",
            earned_point=20,
            created_by=self.user,
        )
        self.lecture.days_of_lec.add(self.day)

    def test_lecture_str_method(self):
        lecture = Lectures.objects.get(title="testlecture")
        self.assertEqual(lecture.__str__(), "testlecture")


class ActivityTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.day = Days.objects.create(name="testday", created_by=self.user)
        self.lecture = Lectures.objects.create(
            title="testlecture",
            description="testdescription",
            earned_point=20,
            created_by=self.user,
        )
        self.lecture.days_of_lec.add(self.day)
        self.activity = Activity.objects.create(
            title="testactivity",
            description="testdescription",
            date=timezone.now(),
            lecture=self.lecture,
        )

    def test_activity_str_method(self):
        activity = Activity.objects.get(title="testactivity")
        self.assertEqual(activity.__str__(), "testactivity")
