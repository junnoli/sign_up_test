from django.urls import path
from .views  import SignInView,SignUpView,CommentView,LikesView,FollowView

urlpatterns = [
    path('', SignUpView.as_view()),
    path('sign_in',SignInView.as_view()),
    path('comment_input',CommentView.as_view()),
    path('follow_check',FollowView.as_view()),
    path('like_check',LikesView.as_view())
]