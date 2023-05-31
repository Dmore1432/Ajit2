from django.urls import path,include
from .views import CourseListView,CourseDetailView
from .views import CourseListView1,CourseListDetails
from .views import GenericView,GenericDetails
from .views import PowerGenerics,PowerGenerics1
from .views import  CourseViewSet
from .views import IntructorListView
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet
from  rest_framework.authtoken.views import obtain_auth_token
router= DefaultRouter()
router.register('course',CourseViewSet,basename='course')
urlpatterns=[
    path('course/',CourseListView.as_view()),
    path('course1/<int:pk>',CourseDetailView.as_view()),
    path('coursemixin/',CourseListView1.as_view()),
    path('coursemixin1/<int:pk>',CourseListDetails.as_view()),
    path('GenericView/',GenericView.as_view()),
    path('GenericDetails/<int:pk>',GenericDetails.as_view()),
    path('PowerGenerics/',PowerGenerics.as_view()),
    path('PowerGenerics1/<int:pk>', PowerGenerics1.as_view()),
    path('IntructorListView/',IntructorListView.as_view()),
    path('CourseViewSet/',include(router.urls)),
    path('gettoken/',obtain_auth_token)

]