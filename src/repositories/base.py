from abc import ABC, abstractmethod


class BaseRepository(ABC):
    @abstractmethod
    async def fetch(self, *args, **kwargs): ...

    @abstractmethod
    async def query(self, *args, **kwargs): ...
