from abc import ABC,abstractmethod
from typing import List,Optional


class CacheRepository(ABC):
    @abstractmethod
    def get_item_by_id(self,item_id:int) ->Optional[str]:
        pass 

    @abstractmethod
    def set_item(self,item_id:int,item_data:str)-> None:
        pass