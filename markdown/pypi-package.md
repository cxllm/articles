## Creating a PyPi package

In this article, I'll be showing you how to make a basic PyPi package

### The Package's Code

Start out by creating a new folder for your PyPi package, you can name this whatever you like.
Open this newly created folder inside a code editor of your choice (I will use JetBrains PyCharm).
Create a new folder named whatever you would like your package to be imported as, e.g.

```
mkdir package_name
```

This would be imported as

```python
import package_name
```

Inside this folder, create a file called `__init__.py` which will be used as the file which all the contents of your module will be in.
In this example, I will be making a simple module which adds two numbers together, so I create a file called main.py and put this content in:

```python
def add(a, b):
    return a + b
```

Now, going back to the `__init__.py` file, I would then add these lines to it

```python
from main import add # import the function from the main.py file

__all__ = ["add"] # If imported like import * from package_name, these are the things imported
```

Both of these files would be in the folder you created earlier.

### Package Setup

Going back to the original folder, you want to create two files: setup.py and README.md. At this point, your structure will look something like this:

```
.
├── README.md
├── package_name
│   ├── __init__.py
│   └── main.py
└── setup.py
```

In this setup.py file, there will be most of the information about the package contained inside, such as name, description, author, website, etc.

```python
from setuptools import setup, find_packages

with open("README.md", "r") as rd: # Load the README file
    long_description = rd.read()
setup(
    name="example-package", # Package Name
    version="1.0.0", # Version Number
    description="An example package", # Description
    url="https://example.com", # Website (usually github or docs page)
    author="Callum", # Your name
    author_email="me@cxllm.xyz", # Your email
    classifiers=[ # Various Descriptors
        "Development Status :: 4 - Beta",
        "License :: Freely Distributable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
    ],
    keywords=["example", "examples"], # Keywords to find your package by
    packages=find_packages(), # Finds packages in the folder
    long_description=long_description, # Your README
    long_description_content_type="text/markdown",
    install_requires=[], # Packages you need
)
```

Once you have completed this, and created a README file, your package is ready to publish. There is one thing you will need to install, called twine. You may be able to find it on your OS's repos, and if not, you can use pip.
e.g.

```
sudo pacman -S twine
```

or

```
sudo pip install twine
```

Once you've installed this, you need to generate your package's tar file, which you can do like this

```
python setup.py sdist
```

Which will create a dist folder with a tar.gz file in it. We will then use twine to upload this package to the [PyPi Registry](https://pypi.org).
Before you upload, you will need to create an account here, which can be done easily. Once you've done that, you can run

```
twine upload dist/* --skip-existing
```

This command will use the tar files in the dist folder (and skip any existing packages on there) to upload your package to the PyPi Registry.

That's how you create and upload a package to PyPi, I hope you found this helpful!
