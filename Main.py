import PhoneBook


def adv_print(*args, **kwargs):
    """

    Function execute advanced variant of usual function print
    print(value, ..., start='', max_line=infinity, in_file=None, sep=' ', end='\n', file=sys.stdout, flush=False)

    Prints the values to a stream and to sys.stdout by default.
    Optional keyword arguments:
    start:   Begin output
    max_line:max length string in one string of output
    in_file: a file-like object (stream).
    sep:     string inserted between values, default a space.
    end:     string appended after the last value, default a newline.
    file:    a file-like object (stream); defaults to the current sys.stdout.
    flush:   whether to forcibly flush the stream.

    """

    # Detect argument "start"
    start = kwargs.get("start")
    if not start:
        start = ""

    max_line = kwargs.get("max_line")
    in_file = kwargs.get("in_file")
    sep = kwargs.get("sep")
    if sep is None:
        sep = ' '
    end_ = kwargs.get("end")
    if end_ is None:
        end_ = '\n'
    file_ = kwargs.get("file")
    flush = kwargs.get("flush")
    if flush is None:
        flush = False

    if max_line is not None:
        args_ = []
        for s in args:
            args_split = [s[x:x + max_line] for x in range(0, len(s), max_line)]
            args_.extend(args_split)
    else:
        args_ = list(args)

    # Print begin string (also depends of max_line)
    if len(start) > 0:
        # Split caption on parts which length = max_length_
        if max_line is not None:
            start_ = [start[x:x + max_line] for x in range(0, len(start), max_line)]
        else:
            start_ = [start, ]
        print(*start_, sep=sep, file=file_, flush=flush)
        if in_file:
            print(*start_, sep=sep, end=end_, file=in_file, flush=flush)

    print(*args_, sep=sep, end=end_, file=file_, flush=flush)

    # Write to file the same information if was define variable in_file
    if in_file:
        print(*args_, sep=sep, end=end_, file=in_file, flush=flush)


if __name__ == "__main__":
    phone_book = PhoneBook.PhoneBook("Фирма")

    # Fill begin information
    phone_book.add_contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    phone_book.add_contact('Haruka', 'Goto', '+81232567001', True, telegram='@haruka', email='goto_h@gmail.com')

    # Print all contacts from phone book
    print(phone_book)

    # Find favorite phone_numbers
    favorite_contacts = phone_book.find_favorites_contacts()
    print(PhoneBook.print_phone_book("Список избранных номеров", favorite_contacts))

    # Find contact by name
    contact = phone_book.find_by_name("Jhon", "Smith")
    print("Найдем контакт по имени:")
    print(contact)

    # Remove contact from phone book
    phone_number = '+81232567001'
    print(f"Удаляем контакт \"{phone_number}\"")
    phone_book.remove_contact(phone_number)
    phone_number = '+71234567809'
    print(f"Удаляем контакт \"{phone_number}\"")
    phone_book.remove_contact(phone_number)
    print(phone_book)

    filename = "file12.txt"
    try:
        with open(filename, 'w', encoding='utf8') as file:
            adv_print("11111111", "222222", "333333", start="Заголовок", max_line=3, sep="\n", end="\n\n", in_file=file)
            adv_print("444444444", "5", "777", start="Заголовок2", sep="\n", end="\n\n", in_file=file)
            adv_print("1", start="Заголовок3", sep="\n", end="\n\n", in_file=file)
            adv_print("1111", "4", "33333", start="Заголовок4", max_line=5, sep=" *** ", end="\n*****\n", in_file=file)
            adv_print("", start="Заголовок5", sep="\n", end="\n\n")
            adv_print("Заголовок6")
    except PermissionError:
        print(f"Недостаточно прав доступа для записи в файл \"{filename}\".")
