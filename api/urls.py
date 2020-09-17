from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword
from .views.teacher_views import Teachers, TeacherDetail

urlpatterns = [
  	# Restful routing
    path('teachers/', Teachers.as_view(), name='teachers'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher_detail'),
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
