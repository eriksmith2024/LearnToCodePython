    def bark(self):
        if self.is_working:
            print(self.name, 'says " I can\'t bark, I\'m working"')
        else:
            Dog.bark(self)