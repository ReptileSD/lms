from django.urls import path

from cathie import views


urlpatterns = [
    path('api/cats-problems/<int:course_id>/', views.ListCatsProblems.as_view(), name='cats-problems'),
    path('api/cats-problem-description/<int:problem_id>/', views.ProblemDescription.as_view(),
         name='cats-problem-description'),
    path('admin/cats/', views.cats_admin, name='cats-admin'),
]
