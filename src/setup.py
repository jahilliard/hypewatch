import setuptools

setuptools.setup(name="src",
                 packages=setuptools.find_packages(),
                 # Project uses reStructuredText, so ensure that the docutils get
                 # installed or upgraded on the target machine
                 install_requires=['docutils>=0.3'],

                 # metadata for upload to PyPI
                 author="Me",
                 author_email="me@example.com",
                 description="This is an Example Package",
                 license="PSF",
                 keywords="hello world example examples",
                 url="http://example.com/HelloWorld/",  # project home page, if any

                 # could also include long_description, download_url, classifiers, etc.
                 )
