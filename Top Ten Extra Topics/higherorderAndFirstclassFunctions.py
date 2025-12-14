def pluralize(word):
    def helper(w):
        return w + "s"
    return helper(word)

val = pluralize('girl')
print("\n", val, "\n")

def addition_maker(n):
    def maker(x):
        return n + x
    return maker

add_two = addition_maker(2)

val = add_two(1)
print('\n', val, '\n')