# Common Export Settings #

These are the settings common to all exporters, such as Xcode and Visual Studio.

### Attributes ###
[targetFolder](#targetfolder)

[vstLegacyFolder](#vstlegacyfolder)

[aaxFolder](#aaxfolder)

[araFolder](#arafolder)

[extraDefs](#extradefs)

[extraCompilerFlags](#extracompilerflags)

[extraLinkerFlags](#extralinkerflags)

[externalLibraries](#externallibraries)

[enableGNUExtensions](#enablegnuextensions)

[smallIcon](#smallicon)

[bigIcon](#bigicon)

[userNotes](#usernotes)


### targetFolder
#### Type: String of max length of max 2048 characters. ####
The location of the folder in which the project will be created. This path can be absolute, but it's much more sensible to make it relative to the jucer project directory.
### vstLegacyFolder
If you're building a VST plug-in or host, you can use this field to override the global VST (Legacy) SDK path with a project-specific path. This can be an absolute path, or a path relative to the Projucer project file.
### aaxFolder
If you're building an AAX plug-in, this must be the folder containing the AAX SDK. This can be an absolute path, or a path relative to the Projucer project file.
### araFolder
If you're building an ARA enabled plug-in, this must be the folder containing the ARA SDK. This can be an absolute path, or a path relative to the Projucer project file.
### extraDefs
#### Type: String of max length of max 32768 characters. ####
Extra preprocessor definitions. Use the form "NAME1=value NAME2=value", using whitespace, commas, or new-lines to separate the items - to include a space or comma in a definition, precede it with a backslash.
### extraCompilerFlags
#### Type: String of max length of max 8192 characters. ####
Extra command-line flags to be passed to the compiler. This string can contain references to preprocessor definitions in the form ${NAME_OF_DEFINITION}, which will be replaced with their values.
### extraLinkerFlags
#### Type: String of max length of max 8192 characters. ####
Extra command-line flags to be passed to the linker. You might want to use this for adding additional libraries. This string can contain references to preprocessor definitions in the form ${NAME_OF_VALUE}, which will be replaced with their values.
### externalLibraries
#### Type: String of max length of max 8192 characters. ####
Additional libraries to link (one per line). You should not add any platform specific decoration to these names. This string can contain references to preprocessor definitions in the form ${NAME_OF_VALUE}, which will be replaced with their values.
### enableGNUExtensions
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enabling this will use the GNU C++ language standard variant for compilation.
### smallIcon
#### Choice ####
Can be one of these values
```
 :- <None>
5 or 6 etc.. :- Image id from binary data
```
Sets an icon to use for the executable.
### bigIcon
#### Choice ####
Can be one of these values
```
 :- <None>
5 or 6 etc.. :- Image id from binary data
```
Sets an icon to use for the executable.
### userNotes
#### Type: String of max length of max 32768 characters. ####
Extra comments: This field is not used for code or project generation, it's just a space where you can express your thoughts.
