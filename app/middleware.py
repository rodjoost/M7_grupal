from django.conf import settings


class SessionParamMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session_params = {
            'SESSION_COOKIE_AGE': request.session.get_expiry_age(),
            'SESSION_COOKIE_DOMAIN': request.get_host(),
            'SESSION_COOKIE_SECURE': request.is_secure(),
            'SESSION_EXPIRE_AT_BROWSER_CLOSE': request.session.get_expire_at_browser_close(),
            'SESSION_SAVE_EVERY_REQUEST': getattr(settings, 'SESSION_SAVE_EVERY_REQUEST', False),
        }
        print(session_params)
        response = self.get_response(request)
        return response
    

"""
Las Herramientas de desarrollador del navegador, como las de Firefox, pueden analizar ciertos parámetros manejados por django.contrib.sessions en la pestaña de Almacenamiento o Cookies. Aquí puede ver los valores de las cookies de sesión, como sessionid, que es la identificación de la sesión en el servidor.

El módulo django.contrib.sessions tiene varios otros usos interesantes, aparte de manejar cookies y sesiones:

Puede guardar datos a nivel de sesión que son específicos de un usuario en particular, pero que no necesariamente deben guardarse en la base de datos.
Puede ser utilizado para rastrear el comportamiento de los visitantes.
Proporciona una manera de implementar la autenticación de usuario basada en sesiones.
Puede ser utilizado para mostrar mensajes temporales ("flash messages") que se muestran una sola vez y luego se borran.

"""