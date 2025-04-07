import setuptools

setuptools.setup(
    name="pdfcrop",
    #packages=setuptools.find_packages(where='src'),
    #package_dir = {'':'src'},
    scripts=['bin/pdfcrop', 'bin/rotate_pdf', 'bin/pdf_to_svg'],
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
    long_description="",
    install_requires=[
        'scikit-learn>=0.24.0',
        'xgboost>=1.3.1',
        'numpy>=1.19.1',
        'pandas>=1.1.0',
        'scipy>=1.5.3',
        'pytest',
        'PyPDF2',
        'cairosvg',
        'pdf2image',
        'aspose-words'
    ]
)
