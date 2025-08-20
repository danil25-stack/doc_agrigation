from abc import ABC, abstractmethod


class IStorageService(ABC):
    
    @abstractmethod
    def upload_file(self, file: bytes, bucket_name: str, output_path: str) -> None:
        pass
