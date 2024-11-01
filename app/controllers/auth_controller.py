from services import AppService, UserService, GoogleAuthService
from configs import Config

from flask import request

class AuthController:
    # def auth_controller():          
    #     data = request.get_json()
    #     headers = dict(request.headers)        

    #     if AppService.is_valide(headers["X-Requested-With"]):
    #         if Config.GOOGLE_SIGN_IN_ACCOUNT in data.keys():
    #             user_data = data.get('google_sign_in_account')
    #             return AppService.create_response(
    #                         UserService.is_user_exist(GoogleAuthService.get_google_data(auth_code=user_data['server_auth_code'])))
            
    #         elif 'apple_id' in data.keys():
    #             pass

    #         elif 'facebook_id' in data.keys():
    #             pass
    #         else:
    #             return 'Unknown service'

    #     else:
    #         return 'Hashed Token is not valid'

        def auth_controller():
            data = request.get_json()
            headers = dict(request.headers)
            
            @AppService.is_token_valid(headers["X-Requested-With"])
            def service_auth_controller():
                if Config.GOOGLE_SIGN_IN_ACCOUNT in data.keys():
                    user_data = data.get('google_sign_in_account')
                    print(f"first request: {user_data}")
                    user_google_data = GoogleAuthService.get_google_data(auth_code=user_data['server_auth_code'])
                    print(f"google data is: {user_google_data}")
                    response_body, status_code = UserService.is_user_exist(user_google_data)
                    
                    return AppService.create_response(
                                body = response_body,
                                status=status_code)
                
                elif 'apple_id' in data.keys():
                    pass

                elif 'facebook_id' in data.keys():
                    pass
                else:
                    return 'Unknown service'
            return service_auth_controller()