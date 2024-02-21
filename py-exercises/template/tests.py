class Color:
    SUCC = "\33[92m"
    FAIL = "\033[91m"
    WARNING = "\033[93m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


class Message:
    SUCC_ICON = "✅"
    FAILED_ICON = "❌"
    SUCC = "{}{} Test passed{}."
    FAILED = "=> {}{}{}{} Expects {}{}{} but got {}{}{}"


def assert_equals(fn, param: tuple, expect: tuple) -> bool:
    result = fn(*param)
    # remove `,` at end of param tuple if the tuple has only one element.
    formatted_param = str(param)[:-2] + ")" if len(param) == 1 else param

    if result == expect:
        output = Message.SUCC.format(Message.SUCC_ICON, Color.SUCC, Color.ENDC)
        print(output)
        return True
    output = Message.FAILED.format(
        Color.WARNING,
        fn.__name__,
        formatted_param,
        Color.ENDC,
        Color.SUCC,
        expect,
        Color.ENDC,
        Color.FAIL,
        result,
        Color.ENDC,
    )
    print(f"{Message.FAILED_ICON} Test Failed.")
    print(output)
    return False
