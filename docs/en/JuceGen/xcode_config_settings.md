# Xcode Export Config Settings #

Settings affecting the configuration of Xcode projects.

### Attributes ###
[optimisationLevel](#optimisationlevel)

[recommendedWarnings](#recommendedwarnings)

[iosBaseSDK](#iosbasesdk)

[iosDeploymentTarget](#iosdeploymenttarget)

[macOSBaseSDK](#macosbasesdk)

[macOSDeploymentTarget](#macosdeploymenttarget)

[macOSArchitecture](#macosarchitecture)

[customXcodeFlags](#customxcodeflags)

[plistPreprocessorDefinitions](#plistpreprocessordefinitions)

[codeSigningIdentity](#codesigningidentity)

[fastMathEnabled](#fastmathenabled)

[stripLocalSymbolsEnabled](#striplocalsymbolsenabled)


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
### recommendedWarnings
#### Choice ####
Can be one of these values
```
LLVM :- Enabled
 :- Disabled
```
Enable this to add a set of recommended compiler warning flags.
### iosBaseSDK
Platform:- iOS

#### Type: String of max length of max 8 characters. ####
The version of the iOS SDK to link against. This must be in the format major.minor and contain only the numeric version number. 
                    If this is left empty then the default will be used." +
                    The minimum supported version is 14.4.
### iosDeploymentTarget
Platform:- iOS

#### Type: String of max length of max 8 characters. ####
The minimum version of iOS to target. This must be in the format major.minor and contain only the numeric version number. 
                    If this is left empty then the default will be used." +
                    The minimum supported version is 12.0.
### macOSBaseSDK
Platform:- OSX

#### Type: String of max length of max 8 characters. ####
The version of the macOS SDK to link against. This must be in the format major.minor and contain only the numeric version number. 
                    If this is left empty then the default will be used." +
                    The minimum supported version is 11.1.
### macOSDeploymentTarget
Platform:- OSX

#### Type: String of max length of max 8 characters. ####
The minimum version of macOS to target. This must be in the format major.minor and contain only the numeric version number. 
                    If this is left empty then the default will be used." +
                    The minimum supported version is 10.11.
### macOSArchitecture
Platform:- OSX

#### Choice ####
Can be one of these values
```
Native :- Native architecture of build machine
32BitUniversal :- Standard 32-bit
64BitUniversal :- Standard 32/64-bit
64BitIntel :- Standard 64-bit
```
The type of macOS binary that will be produced.
### customXcodeFlags
#### Type: String of max length of max 8192 characters. ####
A comma-separated list of custom Xcode setting flags which will be appended to the list of generated flags, e.g. MACOSX_DEPLOYMENT_TARGET_i386 = 10.5
### plistPreprocessorDefinitions
#### Type: String of max length of max 2048 characters. ####
Preprocessor definitions used during PList preprocessing (see PList Preprocess).
### codeSigningIdentity
#### Type: String of max length of max 1024 characters. ####
The name of a code-signing identity for Xcode to apply.
### fastMathEnabled
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to use FAST_MATH non-IEEE mode. (Warning: this can have unexpected results!)
### stripLocalSymbolsEnabled
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to strip any locally defined symbols resulting in a smaller binary size. Enabling this will also remove any function names from crash logs. Must be disabled for static library projects. Note that disabling this will not necessarily generate full debug symbols. For release configs, you will also need to add the following to the "Custom Xcode Flags" field: GCC_GENERATE_DEBUGGING_SYMBOLS = YES, STRIP_INSTALLED_PRODUCT = NO, COPY_PHASE_STRIP = NO
