from django.test import SimpleTestCase
from django.urls import reverse, resolve
from base.views import (
    lectures,
    harcamalarım,
    add_activity,
    add_lecture,
    add_study,
    add_transfercode,
    pomodoro,
    calendar,
    add_product,
    delete_item,
    update_item,
    add_like,
    add_heart,
    add_haha,
    add_wow,
    add_cry,
    add_angry,
    get_details,
    get_lectures_byday,
    set_done,
    add_activity_def,
    add_lecture_def,
    add_study_def,
    add_transfercode_def,
    edit_activity,
    delete_activity,
)


class TestUrls(SimpleTestCase):
    def test_lectures_url_is_resolved(self):
        url = reverse("index")
        self.assertEquals(resolve(url).func, lectures)

    def test_add_activity_url_is_resolved(self):
        url = reverse("add_activity")
        self.assertEquals(resolve(url).func, add_activity)

    def test_add_lecture_url_is_resolved(self):
        url = reverse("add_lecture")
        self.assertEquals(resolve(url).func, add_lecture)

    def test_add_study_url_is_resolved(self):
        url = reverse("add_study")
        self.assertEquals(resolve(url).func, add_study)

    def test_add_transfercode_url_is_resolved(self):
        url = reverse("add_transfercode")
        self.assertEquals(resolve(url).func, add_transfercode)

    def test_pomodoro_url_is_resolved(self):
        url = reverse("pomodoro")
        self.assertEquals(resolve(url).func, pomodoro)

    def test_calendar_url_is_resolved(self):
        url = reverse("calendar")
        self.assertEquals(resolve(url).func, calendar)

    def test_add_product_url_is_resolved(self):
        url = reverse("add_product")
        self.assertEquals(resolve(url).func, add_product)

    def test_delete_item_url_is_resolved(self):
        url = reverse("delete_item", args=[1])
        self.assertEquals(resolve(url).func, delete_item)

    def test_update_item_url_is_resolved(self):
        url = reverse("update_item", args=[1])
        self.assertEquals(resolve(url).func, update_item)

    def test_add_like_url_is_resolved(self):
        url = reverse("add_like", args=[1])
        self.assertEquals(resolve(url).func, add_like)

    def test_add_heart_url_is_resolved(self):
        url = reverse("add_heart", args=[1])
        self.assertEquals(resolve(url).func, add_heart)

    def test_add_haha_url_is_resolved(self):
        url = reverse("add_haha", args=[1])
        self.assertEquals(resolve(url).func, add_haha)

    def test_add_wow_url_is_resolved(self):
        url = reverse("add_wow", args=[1])
        self.assertEquals(resolve(url).func, add_wow)

    def test_add_cry_url_is_resolved(self):
        url = reverse("add_cry", args=[1])
        self.assertEquals(resolve(url).func, add_cry)

    def test_add_angry_url_is_resolved(self):
        url = reverse("add_angry", args=[1])
        self.assertEquals(resolve(url).func, add_angry)

    def test_get_details_url_is_resolved(self):
        url = reverse("get_details", args=[1])
        self.assertEquals(resolve(url).func, get_details)

    def test_get_lectures_byday_url_is_resolved(self):
        url = reverse("get_lectures_byday", args=[1])
        self.assertEquals(resolve(url).func, get_lectures_byday)

    def test_set_done_url_is_resolved(self):
        url = reverse("set_done", args=[1])
        self.assertEquals(resolve(url).func, set_done)

    def test_add_activity_def_url_is_resolved(self):
        url = reverse("add_activity_def")
        self.assertEquals(resolve(url).func, add_activity_def)

    def test_add_lecture_def_url_is_resolved(self):
        url = reverse("add_lecture_def")
        self.assertEquals(resolve(url).func, add_lecture_def)

    def test_add_study_def_url_is_resolved(self):
        url = reverse("add_study_def")
        self.assertEquals(resolve(url).func, add_study_def)

    def test_add_transfercode_def_url_is_resolved(self):
        url = reverse("add_transfercode_def")
        self.assertEquals(resolve(url).func, add_transfercode_def)

    def test_edit_activity_url_is_resolved(self):
        url = reverse("edit_activity", args=[1])
        self.assertEquals(resolve(url).func, edit_activity)

    def test_delete_activity_url_is_resolved(self):
        url = reverse("delete_activity", args=[1])
        self.assertEquals(resolve(url).func, delete_activity)
