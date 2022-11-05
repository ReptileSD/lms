from django.urls import path, include
from users import another_user_login as as_another_user_views

urlpatterns = [
    # path('login/', views.user_login, name='account_login'),
    path('api/anotheruserlogin', as_another_user_views.another_user_login, name='another_user_login'),
    path('api/anotheruserlogout', as_another_user_views.another_user_logout, name='another_user_logout'),
    path('api/sessionuser', as_another_user_views.session_user, name='session_user'),
    path('api/issuperuser', as_another_user_views.is_super_user, name='is_super_user'),
    # path('api/change-password/', views.change_password, name='change_password'),
    # path('api/change-avatar/', views.change_avatar, name='change_avatar'),
    # path('api/edit-profile/', views.edit_profile, name='edit_profile'),
    # path('api/teachersbymail/<int:course_id>/<str:email>/', views.find_teacher_by_email, name='find_teacher'),
    # path('api/assignteacher/<int:course_id>/', views.assign_teacher, name='assign_teacher'),

    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
]
