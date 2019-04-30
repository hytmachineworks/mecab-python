from setuptools import setup, Extension


setup(name="mecab-python",
      version="0.996",
      py_modules=["MeCab"],
      ext_modules=[
          Extension("_MeCab",
                    ["MeCab_wrap.cxx", ],
                    include_dirs=[r"C:\MeCab\sdk"],
                    library_dirs=[r"C:\MeCab\sdk"],
                    libraries=["libmecab"])
      ])
