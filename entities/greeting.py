from dataclasses import dataclass


@dataclass(frozen=True)
class Greeting:
    message: str = "Hello World"

    def as_text(self) -> str:
        text = self.message.strip()
        return text if text else "Hello World"
