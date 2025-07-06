
# JuceGen #

A project generator for Projucer that works with Python. Manage multiple plugins
more efficiently using python script to specify files, macros and settings for
Projucer projects. 


* [About](#about)
* [Installation](#installation)
* [Examples](#examples)
* [Project Settings](project_settings.md) - The project is the primary object for Projucer projects.
* [Project Options](juceoptions.md) - How to control the JUCEOPTIONS element of Projucer projects.
* [Common Export Settings](export_settings.md) - The exporter settings allow control over each type of export.
    * [MSVC Exporter](msvc_exporter_settings.md)
    * [Xcode Exporter](xcode_export_settings.md)
    * [Linux Exporter](linux_export_settings.md)
    * [Android Exporter](android_export_settings.md)
* Config Settings
    * [MSVC Config](msvc_config_settings.md)
    * [Xcode Config](xcode_config_settings.md)
    * [Linux Config](linux_config_settings.md)
    * [Android Config](android_config_settings.md)
* [Setting Attributes](#setting-attributes)


## About ##

JuceGen is a set of python classes that are used directly from a python script
to set all the values needed to write out a .jucer Projucer project file. The
.jucer file can then be opened with Projucer and saved into many formats such
as Xcode, Visual Studio, Linux Makefile or Android studio projects. Using
JuceGen objects like this simplifies the task of managing Juce based projects.
Bevcause the projects are generated with simple python code and dedicated
to making Projucer projects, it is easier to use than other script
based build system alternatives.

## Installation ##

Currently JuceGen is a part of EachPy and if EachPy is installed then JuceGen
module is installed with it. To run the example projects the ExamplesConfig.py
file needs to be edited so that JuceGen knows where the Juce directory is.

## Examples ##

* [Simple Plugin](../../../examples/JuceGen/SimplePlugin/README.md)
* [Gui App](../../../examples/JuceGen/GuiApp/README.md)
* [Console App](../../../examples/JuceGen/ConsoleApp/README.md)

## Setting Attributes ##

* [Overview](#attributes-overview)
* [Setting Attribute Values](#setting-attributes)

### Nodes Overview ###

JuceGen works with various objects that represent the parts of a Projucer project.
The primary object is the Project, and it contains the modules, exporters and configs.
The primary way to set the values is to use the attributes of each type of object.
The attribute names correspond with the names used in the .jucer file of a Projucer project. 

#### Setting Attributes ####
To set attributes of a project, exporter or config object, use this syntax below.

```python
# Attributes can be set by indexer
project["pluginDescription"] = "A description of the plugin"

# Or the attrs property
project.attrs["pluginDescription"] = "A description of the plugin"
```

#### Setting Preprocessor Definitions ####
The **defs** property of the project object specifies preprocessor definitions(macros) that
will apply to all targets in the project. 

```python
# Add a macro
project.add_define("A_MACRO")

# Add a macro with a value
project.add_define("A_MACRO_WITH_VALUE","1")

# Or set it with the indexed field 'defs'
project.defs["A_MACRO"] = "1"

# Or assign directly to the Projucer project attribute if its the project object
project.attrs["extraDefs"] = "A_MACRO&#10;A_MACRO_WITH_VALUE=1&#10"

```
#### Adding Files ####
Files are added to the project object of JuceGen. The kind of files
yu add are normally .cpp and .h files as well as graphics resource such as
png files, but you can also add reference files which are files that
are not used in the build or app but are present in the generated projects
for reference. If you add .mm objective c files
for mac then Projucer will only use those for exports to Xcode projects.

```python
# Use the add_files function to add files. The usual type of
# parameter to pass for the filenames is a list of strings. 
# The files are added relative to the current value of context["SourceDir"].
project.add_files(["MyFile.cpp", "MyFile.h"])

# You can specify a base path to use for many files. In this
# example the files in the list will be located in SomeDir.
project.add_files(["MyFile.cpp", "MyFile.h"], "/MyProject/SomeDir")

# The group where the files are added can be specified.
project.add_files(["MyFile.cpp", "MyFile.h"], group="/MyProject/SomeGroup")

# If you do not want to compile the files but just have them
# in the project for reference then you can specify this with the
# kind parameter.
project.add_files(["MyFile.cpp", "MyFile.h"], kind="ref")

# Or call add_file_refs
project.add_file_refs(["MyFile.cpp", "MyFile.h"])

```

#### Setting Include Paths ####
TODO!!!

#### Setting Library Paths ####
TODO!!!

