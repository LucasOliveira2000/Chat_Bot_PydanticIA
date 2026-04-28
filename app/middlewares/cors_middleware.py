

class CorsMiddleware:
    def __init__(
        self,
        allow_origins: list[str] | str = "*",
        allow_methods: list[str] | str = "*",
        allow_headers: list[str] | str = "*",
        allow_credentials: bool = True,
    ):
        
        self.allow_origins = allow_origins
        self.allow_methods = allow_methods
        self.allow_headers = allow_headers
        self.allow_credentials = allow_credentials

    async def __call__(self, request, call_next):
        response = await call_next(request)
        response.headers["Access-Control-Allow-Origin"] = (
            ", ".join(self.allow_origins) if isinstance(self.allow_origins, list) else self.allow_origins
        )
        response.headers["Access-Control-Allow-Methods"] = (
            ", ".join(self.allow_methods) if isinstance(self.allow_methods, list) else self.allow_methods
        )
        response.headers["Access-Control-Allow-Headers"] = (
            ", ".join(self.allow_headers) if isinstance(self.allow_headers, list) else self.allow_headers
        )
        if self.allow_credentials:
            response.headers["Access-Control-Allow-Credentials"] = "true"
        return response