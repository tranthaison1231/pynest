from fastapi import FastAPI

from nest.core import Module, PyNestFactory

from .modules.user.user_module import UserModule


@Module(imports=[UserModule])
class AppModule:
    pass


app = PyNestFactory.create(
    AppModule,
    description="This is my FastAPI app.",
    title="My App",
    version="1.0.0",
    debug=True,
)

http_server: FastAPI = app.get_server()
