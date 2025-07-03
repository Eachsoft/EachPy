# Visual Studio Exporter Settings #

Settings affecting the export of Visual Studio projects.

### Attributes ###
[manifestFile](#manifestfile)

[IPPLibrary](#ipplibrary)

[IPP1ALibrary](#ipp1alibrary)

[MKL1ALibrary](#mkl1alibrary)

[targetPlatformVersion](#targetplatformversion)


### manifestFile
#### Type: String of max length of max 8192 characters. ####
Path to a manifest input file which should be linked into your binary (path is relative to jucer file).
### IPPLibrary
#### Choice ####
Can be one of these values
```
 :- No
true :- Yes (Default Linking)
Parallel_Static :- Multi-Threaded Static Library
Sequential :- Single-Threaded Static Library
Parallel_Dynamic :- Multi-Threaded DLL
Sequential_Dynamic :- Single-Threaded DLL
```
This option is deprecated, use the "Use IPP Library (oneAPI)" option instead. Enable this to use Intel's Integrated Performance Primitives library, if you have an older version that was not supplied in the oneAPI toolkit.
### IPP1ALibrary
#### Choice ####
Can be one of these values
```
 :- No
true :- Yes (Default Linking)
Static_Library :- Static Library
Dynamic_Library :- Dynamic Library
```
Enable this to use Intel's Integrated Performance Primitives library, supplied as part of the oneAPI toolkit.
### MKL1ALibrary
#### Choice ####
Can be one of these values
```
 :- No
Parallel :- Parallel
Sequential :- Sequential
Cluster :- Cluster
```
Enable this to use Intel's MKL library, supplied as part of the oneAPI toolkit.
### targetPlatformVersion
#### Type: String of max length of max 20 characters. ####
Specifies the version of the Windows SDK that will be used when building this project. if sdk = Windows10 then Leave this field empty to use the latest Windows 10 SDK installed on the build machine, else
                   The default value for this exporter is the default windows target platform version)
