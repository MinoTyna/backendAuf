from django.urls import path
from .views import ClientCreateAPIView,ClientActivateAPIView,VerifyClientOTPAPIViews,ForgotPasswordClientAPIView,ResetPasswordClientAPIView,UploadImageView,ResetClientPasswordAPIView,VerifyClientOTPAPIView,ClientListAPIView,ClientDeleteAPIView,ClientDetailAPIView,GeocodeAPIView,ClientTotalAPIView,ConnexionClientAPIView
from . import views

urlpatterns = [
    path('post', ClientCreateAPIView.as_view(), name='enregistrer-client'),
    path('get', ClientListAPIView.as_view(), name='liste-client'),
    path('total', ClientTotalAPIView.as_view(), name='total-client'),
    path('get/<int:id>', ClientDetailAPIView.as_view(), name='detail-client'),
    path('desactive/<int:client_id>', ClientDeleteAPIView.as_view(), name='delete-client'),
    path('active/<int:client_id>', ClientActivateAPIView.as_view(), name='delete-client'),
    # path('update/<int:pk>', ClientUpdateAPIView.as_view(), name='update-client'),
    path('api/geocode/', GeocodeAPIView.as_view(), name='geocode'),
    path('connexion', ConnexionClientAPIView.as_view(), name='sync_utilisateur'),
    path("upload-image/", UploadImageView.as_view()),
    path("update/<int:id>", views.update_client, name="update_client"),
    #   path('client/login/', ConnexionClientAPIView.as_view(), name='client-login'),
    path('verify-otp/', VerifyClientOTPAPIView.as_view(), name='client-verify-otp'),
    path("reset-password/", ResetClientPasswordAPIView.as_view(), name="reset-client-password"),
    path('client/verify-otp/', VerifyClientOTPAPIViews.as_view(), name='verify_otp'),
    path('client/forgot-password/', ForgotPasswordClientAPIView.as_view(), name='forgot-password'),
    path('client/reset-password/', ResetPasswordClientAPIView.as_view(), name='reset-password'),


]

