#http:// learnpythontheredway.org/book/ex8.html

formatter = "%r %r %r %r"

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."))

# 3번쨰줄에서 but it didn't sing 에 ""로 마무리되는이유는 didn't에 '가들어가서 그렇다.
