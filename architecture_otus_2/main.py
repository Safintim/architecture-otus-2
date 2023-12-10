from architecture_otus_2.exception_handler import (
    ExceptionHandler,
    RepeatCommandHandler,
    RepeatCommand,
    WriteLogHandler,
    SecondRepeatCommand,
    repeat_command_maker,
    log_exception_command_maker,
    second_repeat_command_maker,
)

from queue import Queue


def main() -> None:
    queue: Queue = Queue()
    repeat_command_handler: RepeatCommandHandler = RepeatCommandHandler(
        queue, repeat_command_maker
    )
    write_log_handler: WriteLogHandler = WriteLogHandler(
        queue, log_exception_command_maker
    )

    # при первом выбросе исключения повторить команду, при повторном выбросе исключения записать информацию в лог.
    exception_handler1: ExceptionHandler = ExceptionHandler()
    exception_handler1.register_default_handler(repeat_command_handler)
    exception_handler1.register_handler(RepeatCommand, Exception, write_log_handler)

    # повторить два раза, потом записать в лог
    exception_handler2: ExceptionHandler = ExceptionHandler()
    exception_handler2.register_default_handler(repeat_command_handler)
    exception_handler2.register_handler(
        RepeatCommand,
        Exception,
        RepeatCommandHandler(queue, second_repeat_command_maker),
    )
    exception_handler2.register_handler(
        SecondRepeatCommand,
        Exception,
        write_log_handler,
    )
