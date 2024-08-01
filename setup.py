import setuptools

setuptools.setup(
    name="pdfcrop",
    #packages=setuptools.find_packages(where='src'),
    #package_dir = {'':'src'},
    scripts=['bin/pdfcrop', 'bin/rotate_pdf'],
    version="0.0.1",
    author="Luke Logan",
    author_email="llogan@hawk.iit.edu",
    description="A simple tool to crop whitespace in pdfs",
    url="https://github.com/lukemartinlogan/pdfcrop",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 0 - Pre-Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Users",
        "License :: None",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Office",
    ],
    long_description=""
)
