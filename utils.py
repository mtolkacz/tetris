def get_char():
    # figure out which function to use once, and store it in _func
    if "_func" not in get_char.__dict__:
        try:
            # for Windows-based systems
            import msvcrt  # If successful, we are on Windows
            get_char._func = msvcrt.getch

        except ImportError:
            # for POSIX-based systems (with termios & tty support)
            import tty, sys, termios  # raises ImportError if unsupported

            def _ttyRead():
                fd = sys.stdin.fileno()
                oldSettings = termios.tcgetattr(fd)

                try:
                    tty.setcbreak(fd)
                    answer = sys.stdin.read(1)
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, oldSettings)

                return answer

            get_char._func = _ttyRead
    try:
        result = get_char._func().decode('ASCII')
    except UnicodeDecodeError:
        pass
    else:
        return result

