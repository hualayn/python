# pycharm安装lxml库  

##### 参见 https://www.cnblogs.com/xiexiaoxiao/p/7020422.html 

通过常规的方法安装lxml库，一直报错（错误：Install packages failed: Installing packages: error occurred.）  
然后，想在phcharm的terminal终端下通过pip install lxml的方法来安装，结果也报错：
        
         Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools"

- 安装Microsoft C++    
    打开链接下载安装程序： Microsoft Visual C++ Build Tools 2015  
    链接地址：http://go.microsoft.com/fwlink/?LinkId=691126  
    ，双击visualcppbuildtools_full.exe，选择默认即可，点击安装

    - 再次pip install lxml,提示

            *********************************************************************************
            Could not find function xmlCheckVersion in library libxml2. Is libxml2 installed?
            *********************************************************************************

- 安装wheel
    在终端下：pip install wheel，顺利安装成功

- 下载lxml  
    https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml  
    下载python对应版本的lxml库  
    如我的python版本：

            Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
            Type "help", "copyright", "credits" or "license" for more information.

    Python 3.8.0对应cp38，win32对应win32  
    下载lxml：lxml‑4.4.1‑cp38‑cp38‑win32.whl  
    并把文件改名为：lxml‑4.4.1‑cp38‑none‑win32.whl  
    （参见 https://blog.csdn.net/wwwlyj123321/article/details/79066226）

- 安装lxml

        (venv) D:\python>pip install lxml-4.4.1-cp38-none-win32
        Processing d:\python\lxml-4.4.1-cp38-none-win32.whl
        Installing collected packages: lxml
        Successfully installed lxml-4.4.1

### 安装成功！  
terminal log如下：



        (venv) D:\python>pip install lxml
        Collecting lxml
          Using cached https://files.pythonhosted.org/packages/c4/43/3f1e7d742e2a7925be180b6af5e0f67d38de2f37560365ac1a0b9a04c015/lxml-4.4.1.tar.gz
        Installing collected packages: lxml
          Running setup.py install for lxml ... error
            Complete output from command D:\python\venv\Scripts\python.exe -u -c "import setuptools, tokenize;__file__='C:\\Users\\Administrator.USER-20190628KD\\AppData\\Local\\Temp\\pip-instal
        l-m8t8auuf\\lxml\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\Adm
        inistrator.USER-20190628KD\AppData\Local\Temp\pip-record-dwosf8ow\install-record.txt --single-version-externally-managed --compile --install-headers D:\python\venv\include\site\python3.8
        \lxml:
            Building lxml version 4.4.1.
            Building without Cython.
            ERROR: b"'xslt-config' \xb2\xbb\xca\xc7\xc4\xda\xb2\xbf\xbb\xf2\xcd\xe2\xb2\xbf\xc3\xfc\xc1\xee\xa3\xac\xd2\xb2\xb2\xbb\xca\xc7\xbf\xc9\xd4\xcb\xd0\xd0\xb5\xc4\xb3\xcc\xd0\xf2\r\n\xb
        b\xf2\xc5\xfa\xb4\xa6\xc0\xed\xce\xc4\xbc\xfe\xa1\xa3\r\n"
            ** make sure the development packages of libxml2 and libxslt are installed **

            Using build configuration of libxslt
            running install
            running build
            running build_py
            creating build
            creating build\lib.win32-3.8
            creating build\lib.win32-3.8\lxml
            copying src\lxml\builder.py -> build\lib.win32-3.8\lxml
            copying src\lxml\cssselect.py -> build\lib.win32-3.8\lxml
            copying src\lxml\doctestcompare.py -> build\lib.win32-3.8\lxml
            copying src\lxml\ElementInclude.py -> build\lib.win32-3.8\lxml
            copying src\lxml\pyclasslookup.py -> build\lib.win32-3.8\lxml
            copying src\lxml\sax.py -> build\lib.win32-3.8\lxml
            copying src\lxml\usedoctest.py -> build\lib.win32-3.8\lxml
            copying src\lxml\_elementpath.py -> build\lib.win32-3.8\lxml
            copying src\lxml\__init__.py -> build\lib.win32-3.8\lxml
            creating build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\__init__.py -> build\lib.win32-3.8\lxml\includes
            creating build\lib.win32-3.8\lxml\html
            copying src\lxml\html\builder.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\clean.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\defs.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\diff.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\ElementSoup.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\formfill.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\html5parser.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\soupparser.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\usedoctest.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\_diffcommand.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\_html5builder.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\_setmixin.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\__init__.py -> build\lib.win32-3.8\lxml\html
            creating build\lib.win32-3.8\lxml\isoschematron
            copying src\lxml\isoschematron\__init__.py -> build\lib.win32-3.8\lxml\isoschematron
            copying src\lxml\etree.h -> build\lib.win32-3.8\lxml
            copying src\lxml\etree_api.h -> build\lib.win32-3.8\lxml
            copying src\lxml\lxml.etree.h -> build\lib.win32-3.8\lxml
            copying src\lxml\lxml.etree_api.h -> build\lib.win32-3.8\lxml
            copying src\lxml\includes\c14n.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\config.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\dtdvalid.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\etreepublic.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\htmlparser.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\relaxng.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\schematron.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\tree.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\uri.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xinclude.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xmlerror.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xmlparser.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xmlschema.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xpath.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xslt.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\__init__.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\etree_defs.h -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\lxml-version.h -> build\lib.win32-3.8\lxml\includes
            creating build\lib.win32-3.8\lxml\isoschematron\resources
            creating build\lib.win32-3.8\lxml\isoschematron\resources\rng
            copying src\lxml\isoschematron\resources\rng\iso-schematron.rng -> build\lib.win32-3.8\lxml\isoschematron\resources\rng
            creating build\lib.win32-3.8\lxml\isoschematron\resources\xsl
            copying src\lxml\isoschematron\resources\xsl\RNG2Schtrn.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl
            copying src\lxml\isoschematron\resources\xsl\XSD2Schtrn.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl
            creating build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_abstract_expand.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_dsdl_include.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_message.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_skeleton_for_xslt1.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_svrl_for_xslt1.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\readme.txt -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            running build_ext
            building 'lxml.etree' extension
            error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual C++ Build Tools": https://visualstudio.microsoft.com/downloads/

            ----------------------------------------
        Command "D:\python\venv\Scripts\python.exe -u -c "import setuptools, tokenize;__file__='C:\\Users\\Administrator.USER-20190628KD\\AppData\\Local\\Temp\\pip-install-m8t8auuf\\lxml\\setup.
        py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\Administrator.USER-20190628
        KD\AppData\Local\Temp\pip-record-dwosf8ow\install-record.txt --single-version-externally-managed --compile --install-headers D:\python\venv\include\site\python3.8\lxml" failed with error
         code 1 in C:\Users\Administrator.USER-20190628KD\AppData\Local\Temp\pip-install-m8t8auuf\lxml\


        (venv) D:\python>pip install lxml
        Collecting lxml
          Using cached https://files.pythonhosted.org/packages/c4/43/3f1e7d742e2a7925be180b6af5e0f67d38de2f37560365ac1a0b9a04c015/lxml-4.4.1.tar.gz
        Installing collected packages: lxml
          Running setup.py install for lxml ... error
            Complete output from command D:\python\venv\Scripts\python.exe -u -c "import setuptools, tokenize;__file__='C:\\Users\\Administrator.USER-20190628KD\\AppData\\Local\\Temp\\pip-instal
        l-5kysm3gj\\lxml\\setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\Adm
        inistrator.USER-20190628KD\AppData\Local\Temp\pip-record-7jmictt1\install-record.txt --single-version-externally-managed --compile --install-headers D:\python\venv\include\site\python3.8
        \lxml:
            Building lxml version 4.4.1.
            Building without Cython.
            ERROR: b"'xslt-config' \xb2\xbb\xca\xc7\xc4\xda\xb2\xbf\xbb\xf2\xcd\xe2\xb2\xbf\xc3\xfc\xc1\xee\xa3\xac\xd2\xb2\xb2\xbb\xca\xc7\xbf\xc9\xd4\xcb\xd0\xd0\xb5\xc4\xb3\xcc\xd0\xf2\r\n\xb
        b\xf2\xc5\xfa\xb4\xa6\xc0\xed\xce\xc4\xbc\xfe\xa1\xa3\r\n"
            ** make sure the development packages of libxml2 and libxslt are installed **

            Using build configuration of libxslt
            running install
            running build
            running build_py
            creating build
            creating build\lib.win32-3.8
            creating build\lib.win32-3.8\lxml
            copying src\lxml\builder.py -> build\lib.win32-3.8\lxml
            copying src\lxml\cssselect.py -> build\lib.win32-3.8\lxml
            copying src\lxml\doctestcompare.py -> build\lib.win32-3.8\lxml
            copying src\lxml\ElementInclude.py -> build\lib.win32-3.8\lxml
            copying src\lxml\pyclasslookup.py -> build\lib.win32-3.8\lxml
            copying src\lxml\sax.py -> build\lib.win32-3.8\lxml
            copying src\lxml\usedoctest.py -> build\lib.win32-3.8\lxml
            copying src\lxml\_elementpath.py -> build\lib.win32-3.8\lxml
            copying src\lxml\__init__.py -> build\lib.win32-3.8\lxml
            creating build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\__init__.py -> build\lib.win32-3.8\lxml\includes
            creating build\lib.win32-3.8\lxml\html
            copying src\lxml\html\builder.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\clean.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\defs.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\diff.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\ElementSoup.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\formfill.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\html5parser.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\soupparser.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\usedoctest.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\_diffcommand.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\_html5builder.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\_setmixin.py -> build\lib.win32-3.8\lxml\html
            copying src\lxml\html\__init__.py -> build\lib.win32-3.8\lxml\html
            creating build\lib.win32-3.8\lxml\isoschematron
            copying src\lxml\isoschematron\__init__.py -> build\lib.win32-3.8\lxml\isoschematron
            copying src\lxml\etree.h -> build\lib.win32-3.8\lxml
            copying src\lxml\etree_api.h -> build\lib.win32-3.8\lxml
            copying src\lxml\lxml.etree.h -> build\lib.win32-3.8\lxml
            copying src\lxml\lxml.etree_api.h -> build\lib.win32-3.8\lxml
            copying src\lxml\includes\c14n.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\config.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\dtdvalid.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\etreepublic.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\htmlparser.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\relaxng.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\schematron.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\tree.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\uri.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xinclude.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xmlerror.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xmlparser.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xmlschema.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xpath.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\xslt.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\__init__.pxd -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\etree_defs.h -> build\lib.win32-3.8\lxml\includes
            copying src\lxml\includes\lxml-version.h -> build\lib.win32-3.8\lxml\includes
            creating build\lib.win32-3.8\lxml\isoschematron\resources
            creating build\lib.win32-3.8\lxml\isoschematron\resources\rng
            copying src\lxml\isoschematron\resources\rng\iso-schematron.rng -> build\lib.win32-3.8\lxml\isoschematron\resources\rng
            creating build\lib.win32-3.8\lxml\isoschematron\resources\xsl
            copying src\lxml\isoschematron\resources\xsl\RNG2Schtrn.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl
            copying src\lxml\isoschematron\resources\xsl\XSD2Schtrn.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl
            creating build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_abstract_expand.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_dsdl_include.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_message.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_schematron_skeleton_for_xslt1.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\iso_svrl_for_xslt1.xsl -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            copying src\lxml\isoschematron\resources\xsl\iso-schematron-xslt1\readme.txt -> build\lib.win32-3.8\lxml\isoschematron\resources\xsl\iso-schematron-xslt1
            running build_ext
            building 'lxml.etree' extension
            creating build\temp.win32-3.8
            creating build\temp.win32-3.8\Release
            creating build\temp.win32-3.8\Release\src
            creating build\temp.win32-3.8\Release\src\lxml
            C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\BIN\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -DCYTHON_CLINE_IN_TRACEBACK=0 -Isrc -Isrc\lxml\includes -ID:\python\venv\include
         -IC:\Programs\Python\Python38-32\include -IC:\Programs\Python\Python38-32\include "-IC:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\INCLUDE" "-IC:\Program Files (x86)\Windows Ki
        ts\10\include\10.0.10240.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\8.1\include\shared" "-IC:\Program Files (x86)\Windows Kits\8.1\include\um" "-IC:\Program Files (x86)\Windows Kits\
        8.1\include\winrt" /Tcsrc\lxml\etree.c /Fobuild\temp.win32-3.8\Release\src\lxml\etree.obj -w
            cl : Command line warning D9025 : overriding '/W3' with '/w'
            etree.c
            c:\users\administrator.user-20190628kd\appdata\local\temp\pip-install-5kysm3gj\lxml\src\lxml\includes/etree_defs.h(14): fatal error C1083: Cannot open include file: 'libxml/xmlversio
        n.h': No such file or directory
            Compile failed: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\cl.exe' failed with exit status 2
            creating Users
            creating Users\ADMINI~1.USE
            creating Users\ADMINI~1.USE\AppData
            creating Users\ADMINI~1.USE\AppData\Local
            creating Users\ADMINI~1.USE\AppData\Local\Temp
            C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\BIN\cl.exe /c /nologo /Ox /W3 /GL /DNDEBUG /MD -I/usr/include/libxml2 "-IC:\Program Files (x86)\Microsoft Visual Studio 14.0\VC
        \INCLUDE" "-IC:\Program Files (x86)\Windows Kits\10\include\10.0.10240.0\ucrt" "-IC:\Program Files (x86)\Windows Kits\8.1\include\shared" "-IC:\Program Files (x86)\Windows Kits\8.1\inclu
        de\um" "-IC:\Program Files (x86)\Windows Kits\8.1\include\winrt" /TcC:\Users\ADMINI~1.USE\AppData\Local\Temp\xmlXPathInitiwdiirmc.c /FoUsers\ADMINI~1.USE\AppData\Local\Temp\xmlXPathIniti
        wdiirmc.obj
            xmlXPathInitiwdiirmc.c
            C:\Users\ADMINI~1.USE\AppData\Local\Temp\xmlXPathInitiwdiirmc.c(1): fatal error C1083: Cannot open include file: 'libxml/xpath.h': No such file or directory
            error: command 'C:\\Program Files (x86)\\Microsoft Visual Studio 14.0\\VC\\BIN\\cl.exe' failed with exit status 2
            *********************************************************************************
            Could not find function xmlCheckVersion in library libxml2. Is libxml2 installed?
            *********************************************************************************

            ----------------------------------------
        Command "D:\python\venv\Scripts\python.exe -u -c "import setuptools, tokenize;__file__='C:\\Users\\Administrator.USER-20190628KD\\AppData\\Local\\Temp\\pip-install-5kysm3gj\\lxml\\setup.
        py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record C:\Users\Administrator.USER-20190628
        KD\AppData\Local\Temp\pip-record-7jmictt1\install-record.txt --single-version-externally-managed --compile --install-headers D:\python\venv\include\site\python3.8\lxml" failed with error
         code 1 in C:\Users\Administrator.USER-20190628KD\AppData\Local\Temp\pip-install-5kysm3gj\lxml\

        (venv) D:\python>pip install wheel
        Collecting wheel
          Downloading https://files.pythonhosted.org/packages/00/83/b4a77d044e78ad1a45610eb88f745be2fd2c6d658f9798a15e384b7d57c9/wheel-0.33.6-py2.py3-none-any.whl
        Installing collected packages: wheel
        Successfully installed wheel-0.33.6

        (venv) D:\python>python
        Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
        Type "help", "copyright", "credits" or "license" for more information.
        >>> quit()

        (venv) D:\python>pip install lxml-4.3.5-cp38-cp38-win32.whl
        lxml-4.3.5-cp38-cp38-win32.whl is not a supported wheel on this platform.
        
        (venv) D:\python>pip install lxml-4.4.1-cp38-none-win32
        Processing d:\python\lxml-4.4.1-cp38-none-win32.whl
        Installing collected packages: lxml
        Successfully installed lxml-4.4.1
