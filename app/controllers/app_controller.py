from services import AppService

class AppController:

    def password_verify(password_to_verify):
        return AppService.is_valide(password_to_verify = password_to_verify)
    
    def get_hashed_password():
        return AppService.hash_code_to_send()