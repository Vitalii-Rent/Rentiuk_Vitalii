class BaseClass:
    def __init__(self, path):
        self.path = path

    def get_path(self):
        return self.path

    def process_data(self):
        raise NotImplementedError("Subclass must implement abstract method")


class ChildClass(BaseClass):
    def __init__(self, path, quantity):
        super().__init__(path)
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity

    def process_data(self):
        # Implement data processing logic here
        rotated_value = self._rotate_value(100, self.quantity)
        return rotated_value

    def _rotate_value(self, value, quantity):
        rotated_value = value
        return rotated_value * 2


class GrandChildClass(ChildClass):
    def __init__(self, path, quantity, flag):
        super().__init__(path, quantity)
        self.flag = flag

    def get_flag(self):
        return self.flag

    def process_data(self):
        if self.flag:
            # Implement special processing logic if flag is True
            return self._special_process_data()
        else:
            # Call parent implementation if flag is False
            return super().process_data()

    def _special_process_data(self):
        # Implement special processing logic here
        rotated_value = self._rotate_value(200, self.quantity)
        return rotated_value * 4

