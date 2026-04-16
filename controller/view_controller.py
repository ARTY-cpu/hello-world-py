from services.greeting_service import GreetingService


class GreetingController:
    def __init__(self, service: GreetingService | None = None):
        self._service = service or GreetingService()

    def render_home(self) -> bytes:
        return self._service.get_greeting_text().encode("utf-8")
