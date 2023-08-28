def function():
    def function2():
        print('hello')
        function()
    a = input('input')
    if int(a) > 5:
        function2()
    def function2():
        print('hello')
function()
