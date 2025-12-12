
from django.urls import path
from .views import SyncResponsableAPIView,LoginAPIView,VerifyOTPAPIViews,VerifyOTPAPIView,ResetPasswordAPIView,ForgotPasswordAPIView,PasswordResetRequestAPIView,LogoutAPIView,PasswordResetConfirmAPIView,ConnexionResponsableAPIView,ResponsableListAPIView,ResponsabletUpdateAPIView,ResponsableDetailView,ResponsableTotalAPIView

urlpatterns = [
    path('post', SyncResponsableAPIView.as_view(), name='sync_utilisateur'),
    path('connexion', ConnexionResponsableAPIView.as_view(), name='sync_utilisateur'),
    path('get', ResponsableListAPIView.as_view(), name='liste_utilisateurs'),
    path('total', ResponsableTotalAPIView.as_view(), name='liste_utilisateurs'),
    path('get/<int:pk>', ResponsableDetailView.as_view(), name='liste_utilisateurs'),
    path('update/<int:responsable_id>', ResponsabletUpdateAPIView.as_view(), name='liste_utilisateurs'),
    path('request-reset', PasswordResetRequestAPIView.as_view(), name='request-password-reset'),
    path('reset-password', PasswordResetConfirmAPIView.as_view(), name='confirm-password-reset'),
    #  path("check-email/", CheckEmailAPIView.as_view(), name="check-email"),
    # path("reset-password/", SimplePasswordResetAPIView.as_view(), name="reset-password"),
    path("logout", LogoutAPIView.as_view(), name="logout"),
    path('verify-otp/', VerifyOTPAPIView.as_view(), name='verify_otp'),
    path('responsable/verify-otp/', VerifyOTPAPIViews.as_view(), name='verify_otp'),
    # path('responsable/connexion/', LoginAPIView.as_view(), name='login'),
    path('responsable/forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot-password'),
    path('responsable/reset-password/', ResetPasswordAPIView.as_view(), name='reset-password'),



    # path('update-password/<int:pk>', UpdateResponsablePasswordView.as_view(), name='update-responsable-password'),

]
