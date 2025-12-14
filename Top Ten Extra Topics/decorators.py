def paragraph(func):
    def add_markup():
        return '<p>' + func() + '</p>'
    return add_markup

@paragraph
def get_text():
    return ' hello head first teacher'

# Correct way to print with a blank line before and after
print("\n", get_text(), "\n")
