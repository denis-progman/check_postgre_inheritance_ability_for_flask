class MiddlewareManager:
    def __init__(self):
        self.middlewares = []

    def add_middleware(self, middleware):
        """Register a new middleware."""
        self.middlewares.append(middleware)

    def execute_middlewares(self, rule, request):
        """Execute all registered middlewares."""
        for middleware in self.middlewares:
            response = middleware.process_request(rule, request)
            if response:  # If middleware returns a response, halt further processing
                return response
        return None
