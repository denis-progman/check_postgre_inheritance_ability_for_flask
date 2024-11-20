from flask import jsonify, make_response

class MainController:
    def __call__(self, func):
        """
        Automatically wrap responses returned by controller methods.
        :param func: The controller method.
        """
        def wrapped_method(*args, **kwargs):
            # Call the original method and get the result
            raw_response = func(*args, **kwargs)

            # Format the result into a standard response
            response_body = {
                "status": "success",
                "data": raw_response
            }

            # Return the Flask response object
            response = make_response(jsonify(response_body), 200)
            response.headers["Content-Type"] = "application/json"
            response.headers["X-Custom-Header"] = "MyCustomHeaderValue"
            return response

        return wrapped_method
