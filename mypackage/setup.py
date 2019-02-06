import setuptools
with open("/home/avneeshkumargupta/Desktop/by git/tested_repo/README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='tested_repo',
     version='19.0.1',
     scripts=['tested_repo'],
     author="Avneesh.Gupta",
     author_email="avneesh.gupta@paytm.com",
     description="Utility package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/avneesh-gupta/tested_repo",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
     ],
 )