kp-ubuntu@kp:~/Downloads/python$ touch main.py
kp-ubuntu@kp:~/Downloads/python$ mkdir ryan
kp-ubuntu@kp:~/Downloads/python$ cd ryan
kp-ubuntu@kp:~/Downloads/python/ryan$ touch __init__.py
kp-ubuntu@kp:~/Downloads/python/ryan$ touch config.py test.py
kp-ubuntu@kp:~/Downloads/python/ryan$ ls -la
total 8
drwxrwxr-x 2 kp-ubuntu kp-ubuntu 4096 Oct 27 11:55 .
drwxrwxr-x 3 kp-ubuntu kp-ubuntu 4096 Oct 27 11:55 ..
-rw-rw-r-- 1 kp-ubuntu kp-ubuntu    0 Oct 27 11:55 config.py
-rw-rw-r-- 1 kp-ubuntu kp-ubuntu    0 Oct 27 11:55 __init__.py
-rw-rw-r-- 1 kp-ubuntu kp-ubuntu    0 Oct 27 11:55 test.py
kp-ubuntu@kp:~/Downloads/python/ryan$ gedit config.py
kp-ubuntu@kp:~/Downloads/python/ryan$ gedit test.py
kp-ubuntu@kp:~/Downloads/python/ryan$ gedit ../main.py
kp-ubuntu@kp:~/Downloads/python/ryan$ cd ../
kp-ubuntu@kp:~/Downloads/python$ ls -la
total 16
drwxrwxr-x 3 kp-ubuntu kp-ubuntu 4096 Oct 27 11:56 .
drwxr-xr-x 6 kp-ubuntu kp-ubuntu 4096 Oct 27 11:54 ..
-rw-rw-r-- 1 kp-ubuntu kp-ubuntu   27 Oct 27 11:56 main.py
drwxrwxr-x 2 kp-ubuntu kp-ubuntu 4096 Oct 27 11:56 ryan
kp-ubuntu@kp:~/Downloads/python$ python3 ryan/test.py
__main__
Relative import failed
True
kp-ubuntu@kp:~/Downloads/python$ gedit ryan/test.py
kp-ubuntu@kp:~/Downloads/python$ python3 main.py
ryan.test
True
Absolute import failed


================================================================================





TL;DR: You can't do relative imports from the file you execute since __main__ module is not a part of a package.

Absolute imports - import something available on sys.path

Relative imports - import something relative to the current module, must be a part of a package

If you're running both variants in exactly the same way, one of them should work. Here is an example that should help you understand what's going on. Let's add another main.py file with the overall directory structure like this:

.
./main.py
./ryan/__init__.py
./ryan/config.py
./ryan/test.py
And let's update test.py to see what's going on:

# config.py
debug = True
# test.py
print(__name__)

try:
    # Trying to find module in the parent package
    from . import config
    print(config.debug)
    del config
except ImportError:
    print('Relative import failed')

try:
    # Trying to find module on sys.path
    import config
    print(config.debug)
except ModuleNotFoundError:
    print('Absolute import failed')
# main.py
import ryan.test
Let's run test.py first:

$ python ryan/test.py
__main__
Relative import failed
True
Here "test" is the __main__ module and doesn't know anything about belonging to a package. However import config should work, since the ryan folder will be added to sys.path.

Let's run main.py instead:

$ python main.py
ryan.test
True
Absolute import failed
And here test is inside of the "ryan" package and can perform relative imports. import config fails since implicit relative imports are not allowed in Python 3.

Hope this helped.

P.S.: If you're sticking with Python 3 there is no more need for __init__.py files.
