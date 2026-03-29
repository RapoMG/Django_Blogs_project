from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()

        # check if form use othar name field
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)

        # empty field
        if username is None or password is None:
            return None
        
        # check with username
        try:
            user = UserModel.objects.get(username=username)

        except UserModel.DoesNotExist:
            # check with email
            try:
                user = UserModel.objects.get(email=username)
            except UserModel.DoesNotExist:
                UserModel().set_password(password)  # separate querry makes timing attacks more difficult
                return None
    
        if self.user_can_authenticate(user)and user.check_password(password):
            return user
        

        

        return None