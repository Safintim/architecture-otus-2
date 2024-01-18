import inspect
from inspect import Signature
from typing import Any, Callable, Final
from ioc import Ioc

from architecture_otus_2.commands.interfaces import Movable


class AdapterGenerator:
    def __init__(self, protocol: type, obj: object) -> None:
        self.protocol: Final[type] = protocol
        self.obj: Final[object] = obj

    def generate_adapter_class(self) -> type:
        adapter_class_name: str = f"AutoGenerated{Movable.__name__}Adapter"
        adapter_class_methods: dict[str, Callable] = {
            name: self.create_function(function)
            for name, function in inspect.getmembers(
                self.protocol, predicate=inspect.isfunction
            )
            if not name.startswith("__") and not name.endswith("__")
        }
        adapter_class_methods["__init__"] = self.create_init()

        return type(
            adapter_class_name,
            (object,),
            adapter_class_methods,
        )

    def create_init(self) -> Callable:
        def __init__(self, obj):
            self.obj = obj

        return __init__

    def create_function(self, protocol_function: Callable) -> Callable:
        signature: Signature = inspect.signature(protocol_function)

        method_parameters: str = ", ".join(
            [param.name for param in signature.parameters.values()]
        )
        dependecy_parameters: str = ", ".join(
            ["self.obj"]
            + [
                param.name
                for param in signature.parameters.values()
                if param.name != "self"
            ]
        )

        function_name: str = protocol_function.__name__
        function_name_parts: list[str] = function_name.split("_")

        dependecy_name: str = ""
        if len(function_name_parts) == 2:
            action, attribute = function_name_parts
            dependecy_name = f"{self.protocol.__name__}:{attribute}.{action}"
        else:
            dependecy_name = f"{self.protocol.__name__}:{function_name}"

        template: str = f"""def {function_name}({method_parameters}):\n\t print('{function_name}', {method_parameters}) \n\t return Ioc.resolve('{dependecy_name}', {dependecy_parameters})"""

        locs: dict[str, Callable] = {}
        exec(template, {"Ioc": Ioc}, locs)
        return locs[function_name]

    def create_adapter_instance(self) -> Any:
        return self.generate_adapter_class()(self.obj)
