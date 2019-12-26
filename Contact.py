class Contact:
    def __init__(self, first_name, last_name, phone_number, favorite=False, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.favorite = favorite
        self.additional_info = kwargs.copy()

        # for name, value in kwargs.items():
        #     self.additional_info[name] = value

    def __str__(self):
        string = f"Имя: {self.first_name}\nФамилия: {self.last_name}\nТелефон: {self.phone_number}"
        if self.favorite:
            favorite_str = "есть"
        else:
            favorite_str = "нет"
        string += f"\nВ избранных: {favorite_str}\nДополнительная итформация:"
        for name, value in self.additional_info.items():
            string += f"\n\t{name} : {value}"
        return string + '\n'
