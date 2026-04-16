from entities.greeting import Greeting


class GreetingService:
    def build_greeting(self) -> Greeting:
        return Greeting()

    def get_greeting_text(self) -> str:
        return self.build_greeting().as_text()
