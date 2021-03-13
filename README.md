# pdfcrop

A simple wrapper around GhostWrapper for removing whitespace in pdfs.

# Installation

## For Regular Users
```{bash}
cd /path/to/pdfcrop  
python3 setup.py sdist bdist_wheel  
python3 -m pip install dist/*.whl --user
rm -r dist build *.egg_info MANIFEST  
```

## For Developers

```{bash}
cd /path/to/pdfcrop  
python3 setup.py develop --user
```

## Uninstallation

```{bash}
python3 -m pip uninstall pdfcrop
```
