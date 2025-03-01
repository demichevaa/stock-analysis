import logging
import threading
from typing import Type, Callable, TypeVar

T = TypeVar('T')

def singleton(class_: Type[T]) -> Callable[..., T]:
    """
    Thread-safe Singleton class-decorator.

    If the class defines `on_create`, it will be called on the first instantiation.

    Args:
        class_ (Type[T]): The class to be made a Singleton.

    Returns:
        Callable[..., T]: The Singleton-wrapped class.

    Usage:
        @singleton
        class Foo:
            def __init__(self, value):
                self.value = value

            def on_create(self, *args, **kwargs):
                pass
    """
    class SingletonWrapper(class_):
        _singleton_instance = None
        _singleton_lock = threading.Lock()

        def __new__(cls, *args, **kwargs) -> T:
            with cls._singleton_lock:
                if not cls._singleton_instance:
                    cls._singleton_instance = super(SingletonWrapper, cls).__new__(cls)
                    cls.logger = logging.getLogger(cls.__name__)
                    if hasattr(cls._singleton_instance, 'on_create'):
                        cls._singleton_instance.on_create(*args, **kwargs)
            return cls._singleton_instance

    SingletonWrapper.__name__ = class_.__name__
    SingletonWrapper.__doc__ = class_.__doc__
    SingletonWrapper.__module__ = class_.__module__

    return SingletonWrapper
