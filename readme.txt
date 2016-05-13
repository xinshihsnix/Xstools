这是一个Python egg文件

* egg 文件的制作
    来源:http://blog.csdn.net/turkeyzhou/article/details/8876658

    # -----------------------------
    $ mkdir egg-demo
    $ cd egg-demo
    $ touch setup.py
    $ ls
    setup.py
    # -------------------------------
    $ cat setup.py
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    from setuptools import setup

    setup()
    #----------------------------------
    $ python setup.py bdist_egg
    #---------------------------------
    $ cat setup.py
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    from setuptools import setup, find_packages

    setup(
            name = "demo",
            version="0.1.0",
            packages = find_packages(),
            zip_safe = False,

            description = "egg test demo.",
            long_description = "egg test demo, haha.",
            author = "amoblin",
            author_email = "amoblin@ossxp.com",

            license = "GPL",
            keywords = ("test", "egg"),
            platforms = "Independant",
            url = "",
            )
    #--------------------------------------------------
    $ mkdir demo
    $ cat demo/__init__.py
    #!/usr/bin/env python
    #-*- coding:utf-8 -*-

    def test():
        print "Hello, I'm amoblin."

    if __name__ == '__main__':
        test()
    #-----------------------------------------------
    $ python setup.py bdist_egg
    #---------------------------------------------
    $ python -c "from demo import test;test()"
    Hello, I'm amoblin.
    #----------------------------------------------

* egg 卸载
    $ cd /usr/local/lib/python2.6/dist-packages
    $ cat easy-install.pth|grep demo
    ./demo-0.1.0-py2.6.egg
    $ ls -F|grep demo
    demo-0.1.0-py2.6.egg/

    卸载egg文件很简单，首先将包含此egg的行从easy-install.pth中删除，然后删除egg文件夹即可。