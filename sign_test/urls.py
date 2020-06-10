from django.urls import path
from .views  import MainView,SignUpView,CommentView

urlpatterns = [
    path('', MainView.as_view()),
    path('sign_in',SignUpView.as_view()),
    path('comment_input',CommentView.as_view()),
]