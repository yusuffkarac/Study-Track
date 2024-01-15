from django.urls import path
from . import views

urlpatterns = [
    path('', views.lectures, name='index'),
    path('harcamalarım', views.harcamalarım, name='harcamalarım'),
    path('add_activity', views.add_activity, name='add_activity'),
    path('add_lecture', views.add_lecture, name='add_lecture'),
    path('add_study', views.add_study, name='add_study'),
    path('add_transfercode', views.add_transfercode, name='add_transfercode'),
    path('pomodoro', views.pomodoro, name='pomodoro'),

    path('calendar', views.calendar, name='calendar'),
    path('add_product/', views.add_product, name='add_product'),
    path('delete_item/<int:id>', views.delete_item, name='delete_item'),
    path('update_item/<int:id>', views.update_item, name='update_item'),
    path('add_like/<int:id>',views.add_like, name='add_like'),
    path('add_heart/<int:id>',views.add_heart, name='add_heart'),
    path('add_haha/<int:id>',views.add_haha, name='add_haha'),
    path('add_wow/<int:id>',views.add_wow, name='add_wow'),
    path('add_cry/<int:id>',views.add_cry, name='add_cry'),
    path('add_angry/<int:id>',views.add_angry, name='add_angry'),

    path('get_details/<int:id>',views.get_details, name='get_details'),
    path('get_lectures_byday/<int:id>',views.get_lectures_byday, name='get_lectures_byday'),

    path('set_done/<int:id>',views.set_done, name='set_done'),
    path('add_activity_def',views.add_activity_def, name='add_activity_def'),
    path('add_lecture_def/',views.add_lecture_def, name='add_lecture_def'),
    path('add_study_def',views.add_study_def, name='add_study_def'),
    path('add_transfercode_def',views.add_transfercode_def, name='add_transfercode_def'),


    path('edit_activity/<int:id>',views.edit_activity, name='edit_activity'),
    path('delete_activity/<int:id>',views.delete_activity, name='delete_activity'),
    ]