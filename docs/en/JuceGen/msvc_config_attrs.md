# Visual Studio Config Settings #

Settings affecting the configuration of Visual Studio projects.

### Attributes ###
[architectureType](#architecturetype)

[debugInformationFormat](#debuginformationformat)

[fastMath](#fastmath)

[optimisationLevel](#optimisationlevel)

[intermediatesPath](#intermediatespath)

[warningLevel](#warninglevel)

[warningsAreErrors](#warningsareerrors)

[useRuntimeLibDLL](#useruntimelibdll)

[multiProcessorCompilation](#multiprocessorcompilation)

[enableIncrementalLinking](#enableincrementallinking)

[generateDebugSymbols](#generatedebugsymbols)

[prebuildCommand](#prebuildcommand)

[postbuildCommand](#postbuildcommand)

[characterSet](#characterset)

[pluginBinaryCopyStep](#pluginbinarycopystep)

[vst3BinaryLocation](#vst3binarylocation)

[vst3BinaryLocation_x64](#vst3binarylocation_x64)

[vst3BinaryLocation_arm64](#vst3binarylocation_arm64)

[vst3BinaryLocation_arm64ec](#vst3binarylocation_arm64ec)

[aaxBinaryLocation](#aaxbinarylocation)

[aaxBinaryLocation_x64](#aaxbinarylocation_x64)

[aaxBinaryLocation_arm64](#aaxbinarylocation_arm64)

[aaxBinaryLocation_arm64ec](#aaxbinarylocation_arm64ec)

[vstBinaryLocation](#vstbinarylocation)

[vstBinaryLocation_x64](#vstbinarylocation_x64)

[vstBinaryLocation_arm64](#vstbinarylocation_arm64)

[vstBinaryLocation_arm64ec](#vstbinarylocation_arm64ec)

[lv2BinaryLocation](#lv2binarylocation)

[lv2BinaryLocation_x64](#lv2binarylocation_x64)

[lv2BinaryLocation_arm64](#lv2binarylocation_arm64)

[lv2BinaryLocation_arm64ec](#lv2binarylocation_arm64ec)

[unityBinaryLocation](#unitybinarylocation)

[unityBinaryLocation_x64](#unitybinarylocation_x64)

[unityBinaryLocation_arm64](#unitybinarylocation_arm64)

[unityBinaryLocation_arm64ec](#unitybinarylocation_arm64ec)


### architectureType
#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
win32 :- Win32
x64 :- x64
ARM64 :- ARM64
ARM64EC :- ARM64EC
```
Which Windows architecture to use.
### debugInformationFormat
#### Choice ####
Can be one of these values
```
None :- None
OldStyle :- C7 Compatible (/Z7)
ProgramDatabase :- Program Database (/Zi)
EditAndContinue :- Program Database for Edit And Continue (/ZI)
```
The type of debugging information created for your program for this configuration. This will always be used in a debug configuration and will be used in a release configuration with forced generation of debug symbols.
### fastMath
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to use FAST_MATH non-IEEE mode. (Warning: this can have unexpected results!)
### optimisationLevel
#### Choice ####
Can be one of these values
```
optimisationOff :- Disabled (/Od)
optimiseMinSize :- Minimise size (/O1)
optimiseMaxSpeed :- Maximise speed (/O2)
optimiseFull :- Full optimisation (/Ox)
```
The optimisation level for this configuration
### intermediatesPath
#### Type: String of max length of max 2048 characters. ####
An optional path to a folder to use for the intermediate build files. Note that Visual Studio allows you to use macros in this path, e.g. "$(TEMP)\MyAppBuildFiles\$(Configuration)", which is a handy way to send them to the user's temp folder.
### warningLevel
#### Choice ####
Can be one of these values
```
2 :- Low
3 :- Medium
4 :- High
```
The compilation warning level to use.
### warningsAreErrors
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to treat compilation warnings as errors.
### useRuntimeLibDLL
#### Choice ####
Can be one of these values
```
false :- Use static runtime
true :- Use DLL runtime
```
If the static runtime is selected then your app/plug-in will not be dependent upon users having Microsoft's redistributable C++ runtime installed. However, if you are linking libraries from different sources you must select the same type of runtime used by the libraries.
### multiProcessorCompilation
#### Choice ####
Can be one of these values
```
true :- Enabled
false :- Disabled
```
Allows the compiler to use of all the available processors, which can reduce compilation time. This is enabled by default and should only be disabled if you know what you are doing.
### enableIncrementalLinking
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable to avoid linking from scratch for every new build. Disable to ensure that your final release build does not contain padding or thunks.
### generateDebugSymbols
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to force generation of debug symbols in a release configuration.
### prebuildCommand
#### Type: String of max length of max 2048 characters. ####
Some command that will be run before a build starts.
### postbuildCommand
#### Type: String of max length of max 2048 characters. ####
Some command that will be run after a build starts.
### characterSet
#### Choice ####
Can be one of these values
```
MultiByte :- MultiByte
Unicode :- Unicode
```
Specifies the character set used when building.
### pluginBinaryCopyStep
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to copy plugin binaries to a specified folder after building.
### vst3BinaryLocation
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### vst3BinaryLocation_x64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### vst3BinaryLocation_arm64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### vst3BinaryLocation_arm64ec
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### aaxBinaryLocation
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### aaxBinaryLocation_x64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### aaxBinaryLocation_arm64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### aaxBinaryLocation_arm64ec
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### vstBinaryLocation
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### vstBinaryLocation_x64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### vstBinaryLocation_arm64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### vstBinaryLocation_arm64ec
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### lv2BinaryLocation
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### lv2BinaryLocation_x64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### lv2BinaryLocation_arm64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### lv2BinaryLocation_arm64ec
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### unityBinaryLocation
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### unityBinaryLocation_x64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### unityBinaryLocation_arm64
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
### unityBinaryLocation_arm64ec
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled binary should be placed.
