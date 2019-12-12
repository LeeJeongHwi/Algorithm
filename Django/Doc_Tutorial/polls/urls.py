from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path("<int:pk>/",views.DetailView.as_view(),name='detail'),
    path("<int:pk>/results/",views.ResultsView.as_view(),name='results'),
    path("<int:question_id>/vote/",views.vote,name='vote'),
]
    #
    # #polls/
    # path('', views.index,name='index'),
    # #polls/숫자
    # #<>는 변수를 의미함 < 이부분에 해당하는 값을 뷰에 인자로 전달
    # path("<int:question_id>/",views.detail,name='details'),
    # #polls/숫자/results/
    # path("<int:question_id>/results",views.results,name='results'),
    # #polls/숫자/vote/
    # path("<int:question_id>/vote/",views.vote,name='vote'),

