from django.urls import path
from .apiviews import ChoiceList, CreateVote, UserCreate, LoginView
# PollList, PollDetail,
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet

from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Polls API')

from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

# path("polls/", PollList.as_view(), name="polls_list"),
#     path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path('swagger-docs/', schema_view),
    path('docs/', include_docs_urls(title='Polls API 2')),
]

urlpatterns += router.urls



