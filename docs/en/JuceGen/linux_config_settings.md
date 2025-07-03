# Linux Export Config Settings #

Settings affecting the configuration of Linux make projects.

### Attributes ###
[recommendedWarnings]](#recommendedwarnings])

[optimisationLevel](#optimisationlevel)

[architectureType](#architecturetype)

[pluginBinaryCopyStep](#pluginbinarycopystep)

[vst3BinaryLocation](#vst3binarylocation)

[lv2BinaryLocation](#lv2binarylocation)

[unityPluginBinaryLocation](#unitypluginbinarylocation)

[vstBinaryLocation](#vstbinarylocation)


### recommendedWarnings]
#### Choice ####
Can be one of these values
```
GCC :- GCC
LLVM :- LLVM
 :- Disabled
```
Enable this to add a set of recommended compiler warning flags.
### optimisationLevel
#### Choice ####
Can be one of these values
```
1 :- -O0 (no optimisation)
2 :- -Os (minimise code size)
4 :- -O1 (fast)
5 :- -O2 (faster)
3 :- -O3 (fastest with safe optimisations)
6 :- -Ofast (uses aggressive optimisations)
```
The optimisation level for this configuration
### architectureType
#### Choice ####
Can be one of these values
```
 :- <None>
-march=native :- Native
-m32 :- 32-bit (-m32)
-m64 :- 64-bit (-m64)
-march=armv6 :- ARM v6
-march=armv7 :- ARM v7
-march=armv8-a :- ARM v8-a
```
Specifies the 32/64-bit architecture to use. If you don't see the required architecture in this list, you can also specify the desired flag on the command-line when invoking make by passing "TARGET_ARCH=-march=<arch to use>"
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
The folder in which the compiled VST3 binary should be placed.
### lv2BinaryLocation
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled LV2 binary should be placed.
### unityPluginBinaryLocation
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled Unity plugin binary and associated C# GUI script should be placed.
### vstBinaryLocation
#### Type: String of max length of max 1024 characters. ####
The folder in which the compiled legacy VST binary should be placed.
