#create a copy of its own source code
class foo:
    def bar():
        print
        'Hello'

import inspect
print(inspect.getsource(bar()))