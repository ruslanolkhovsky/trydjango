from django.urls import path

from .views import (
    CourseView,
    CourseListView,
    # CourseListViewFiltered,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)

app_name = "courses"

urlpatterns = [
    # path('', CourseListViewFiltered.as_view(), name='course-list'),
    path('', CourseListView.as_view(), name='course-list'),
    # path('', CourseView.as_view(template_name='contact.html'), name='course-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail'),
    path('create/', CourseCreateView.as_view(), name='course-create'),
    path('<int:id>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('<int:id>/delete/', CourseDeleteView.as_view(), name='article-delete'),

]
