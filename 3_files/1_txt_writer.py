import faker

some_file = open("example_write.txt", "w")

text = """Nature's bequest gives nothing but doth lend,
And being frank she lends to those are free
"""

some_file.write(text)

some_file.close()
