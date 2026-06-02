from typing import Callable, Any
import time

def timer[T: Callable[..., Any]](func: T) -> T:
    def inner(*args: Any, **kwargs: Any) -> Any:
        start = time.time()
        turns = func(*args, **kwargs)
        stop = time.time()
        print(f"Ellapsed time : {(stop - start):.2f} seconds")
        return turns
    return inner