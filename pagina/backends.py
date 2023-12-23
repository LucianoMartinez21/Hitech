from django.contrib.auth.backends import ModelBackend
from .models import Usuarios, Contrasenas

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            # Get the user based on the email
            user = Usuarios.objects.get(email=email)

            # Get the corresponding password from the Contrasenas table
            contrasena = Contrasenas.objects.get(usuario_id=user.id)

            # Check if the provided password matches the stored password
            if contrasena.contra == password:
                return user
            else:
                print(f"Authentication failed for user with email: {email}")
                return None

        except Usuarios.DoesNotExist:
            print(f"User with email {email} does not exist.")
            return None
        except Contrasenas.DoesNotExist:
            print(f"Password not found for user with email: {email}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None