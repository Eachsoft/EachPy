
# EachPy #


## About ##

A collection of python packages from EachSoft.


## Packages ##

* [JuceGen](en/JuceGen/README.md) - A generator of .jucer Projucer projects. Generate projects and then use Projucer to resave them for building with Ide such as Xcode or Visual Studio.


## Installation ##

### Install from cloned repository ###

If you do not have build and setuptools install them with these commands
```
python3 -m pip install --upgrade build
pip3 install --upgrade pip
pip3 install setuptools
```

Then in the root of the repository execute 
```
# 1. build the distribution.
python3 -m pip install -e .
```

```
# To uninstall the repository execute...
python3 -m pip uninstall EachPy
```




