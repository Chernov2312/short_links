__all__ = ('Link',)
from pydantic import BaseModel, model_validator


class Link(BaseModel):
    link: str

    @model_validator(mode='after')
    def validate_and_clean_fields(self):
        if 'http' not in self.link:
            raise ValueError('Некорректная ссылка')
        return self
