# Project Settings #

The project settings affect the entire project and all exporters. 

### Attributes ###
[projectName](#projectname)

[version](#version)

[projectLineFeed](#projectlinefeed)

[companyName](#companyname)

[companyCopyright](#companycopyright)

[companyWebsite](#companywebsite)

[companyEmail](#companyemail)

[useAppConfig](#useappconfig)

[addUsingNamespaceToJuceHeader](#addusingnamespacetojuceheader)

[projectType](#projecttype)

[bundleIdentifier](#bundleidentifier)

[pluginFormats](#pluginformats)

[pluginCharacteristics](#plugincharacteristics)

[pluginName](#pluginname)

[pluginDesc](#plugindesc)

[pluginManufacturer](#pluginmanufacturer)

[pluginManufacturerCode](#pluginmanufacturercode)

[pluginCode](#plugincode)

[pluginChannelConfigs](#pluginchannelconfigs)

[pluginAAXIdentifier](#pluginaaxidentifier)

[pluginAUExportPrefix](#pluginauexportprefix)

[pluginAUMainType](#pluginaumaintype)

[pluginAUSandboxSafe](#pluginausandboxsafe)

[pluginVSTNumMidiInputs](#pluginvstnummidiinputs)

[pluginVSTNumMidiOutputs](#pluginvstnummidioutputs)

[pluginVST3Category](#pluginvst3category)

[pluginAAXCategory](#pluginaaxcategory)

[pluginVSTCategory](#pluginvstcategory)

[pluginLV2URI](#pluginlv2uri)

[pluginARAAnalyzableContent](#pluginaraanalyzablecontent)

[pluginARATransformFlags](#pluginaratransformflags)

[pluginARAFactoryID](#pluginarafactoryid)

[pluginARAArchiveID](#pluginaraarchiveid)

[pluginARACompatibleArchiveIDs](#pluginaracompatiblearchiveids)

[maxBinaryFileSize](#maxbinaryfilesize)

[includeBinaryDataInJuceHeader](#includebinarydatainjuceheader)

[binaryDataNamespace](#binarydatanamespace)

[cppStandard](#cppstandard)

[preprocessorDefs](#preprocessordefs)

[headerSearchPaths](#headersearchpaths)

[postExportShellCommandPosix](#postexportshellcommandposix)

[postExportShellCommandWin](#postexportshellcommandwin)

[userNotes](#usernotes)


### projectName
#### Type: String of max length of max 256 characters. ####
The name of the project.
### version
#### Type: String of max length of max 16 characters. ####
The project's version number. This should be in the format major.minor.point[.point] where you should omit the final (optional) [.point] if you are targeting AU and AUv3 plug-ins as they only support three number versions.
### projectLineFeed
#### Choice ####
Can be one of these values
```

 :- \r\n

 :- \n
```
Use this to set the line feed which will be used when creating new source files for this project (this won't affect any existing files).
### companyName
#### Type: String of max length of max 256 characters. ####
Your company name, which will be added to the properties of the binary where possible
### companyCopyright
#### Type: String of max length of max 256 characters. ####
Your company copyright, which will be added to the properties of the binary where possible
### companyWebsite
#### Type: String of max length of max 256 characters. ####
Your company website, which will be added to the properties of the binary where possible
### companyEmail
#### Type: String of max length of max 256 characters. ####
Your company e-mail, which will be added to the properties of the binary where possible
### useAppConfig
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, the Projucer will generate module wrapper stubs which include AppConfig.h and will include AppConfig.h in the JuceHeader.h. If disabled, all the settings that would previously have been specified in the AppConfig.h will be injected via the build system instead, which may simplify the includes in the project.
### addUsingNamespaceToJuceHeader
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, the JuceHeader.h will include a "using namespace juce" statement. If disabled, no such statement will be included. This setting used to be enabled by default, but it is recommended to leave it disabled for new projects.
### projectType
The type of project (e.g., GUI Application, Console Application, Static Library, etc.).

  - **consoleapp**: A console application that runs in a command-line interface without a graphical user interface. Suitable for command-line tools or applications that do not require any GUI components.
  - **guiapp**: A standard GUI application used for applications with a graphical user interface, typically including windows, buttons, and other interactive components.

  - **library**: A static library project. This type generates a library that can be linked into other applications, providing reusable code without a standalone executable.

  - **dll**: A dynamic link library (DLL) project, typically used for Windows. It produces a shared library that can be used by other applications at runtime.

  - **audioplug**: An audio plugin project. This type is used for creating audio effects or instruments in various plugin formats (e.g., VST, AU, AAX). It is specifically designed for integration with digital audio workstations (DAWs) and supports audio processing.

  - **audioapp**: An audio application project that combines elements of both GUI applications and audio processing, suitable for standalone audio applications like synthesizers or DAW-like interfaces.

### bundleIdentifier
#### Type: String of max length of max 256 characters. ####
A unique identifier for this product, mainly for use in OSX/iOS builds. It should be something like 'com.yourcompanyname.yourproductname'
### pluginFormats
#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
buildVST3 :- VST3
buildAU :- AU
buildAUv3 :- AUv3
buildAAX :- AAX
buildStandalone :- Standalone
buildLV2 :- LV2
buildUnity :- Unity
enableIAA :- Enable IAA
buildVST :- VST (Legacy)
enableARA :- Enable ARA
```
Plugin formats to build. If you have selected "VST (Legacy)" then you will need to ensure that you have a VST2 SDK in your header search paths. The VST2 SDK can be obtained from the vstsdk3610_11_06_2018_build_37 (or older) VST3 SDK or JUCE version 5.3.2. You also need a VST2 license from Steinberg to distribute VST2 plug-ins. If you enable ARA you will have to obtain the ARA SDK by recursively cloning https://github.com/Celemony/ARA_SDK and checking out the tag releases/2.1.0.
### pluginCharacteristics
#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
pluginIsSynth :- Plugin is a Synth
pluginWantsMidiIn :- Plugin MIDI Input
pluginProducesMidiOut :- Plugin MIDI Output
pluginIsMidiEffectPlugin :- MIDI Effect Plugin
pluginEditorRequiresKeys :- Plugin Editor Requires Keyboard Focus
pluginAAXDisableBypass :- Disable AAX Bypass
pluginAAXDisableMultiMono :- Disable AAX Multi-Mono
```
Some characteristics of your plugin such as whether it is a synth, produces MIDI messages, accepts MIDI messages etc.
### pluginName
#### Type: String of max length of max 128 characters. ####
The name of your plugin (keep it short!)
### pluginDesc
#### Type: String of max length of max 256 characters. ####
A short description of your plugin.
### pluginManufacturer
#### Type: String of max length of max 256 characters. ####
The name of your company (cannot be blank).
### pluginManufacturerCode
#### Type: String of max length of max 4 characters. ####
A four-character unique ID for your company. Note that for AU compatibility, this must contain at least one upper-case letter! GarageBand 10.3 requires the first letter to be upper-case, and the remaining letters to be lower-case.
### pluginCode
#### Type: String of max length of max 4 characters. ####
A four-character unique ID for your plugin. Note that for AU compatibility, this must contain exactly one upper-case letter! GarageBand 10.3 requires the first letter to be upper-case, and the remaining letters to be lower-case.
### pluginChannelConfigs
#### Type: String of max length of max 1024 characters. ####
This list is a comma-separated set list in the form {numIns, numOuts} and each pair indicates a valid plug-in configuration. For example {1, 1}, {2, 2} means that the plugin can be used either with 1 input and 1 output, or with 2 inputs and 2 outputs. If your plug-in requires side-chains, aux output buses etc., then you must leave this field empty and override the isBusesLayoutSupported callback in your AudioProcessor.
### pluginAAXIdentifier
#### Type: String of max length of max 256 characters. ####
The value to use for the JucePlugin_AAXIdentifier setting
### pluginAUExportPrefix
#### Type: String of max length of max 128 characters. ####
A prefix for the names of exported entry-point functions that the component exposes - typically this will be a version of your plugin's name that can be used as part of a C++ token.
### pluginAUMainType
#### Choice ####
Can be one of these values
```
'aufx' :- kAudioUnitType_Effect
'aufc' :- kAudioUnitType_FormatConverter
'augn' :- kAudioUnitType_Generator
'aumi' :- kAudioUnitType_MIDIProcessor
'aumx' :- kAudioUnitType_Mixer
'aumu' :- kAudioUnitType_MusicDevice
'aumf' :- kAudioUnitType_MusicEffect
'auol' :- kAudioUnitType_OfflineEffect
'auou' :- kAudioUnitType_Output
'aupn' :- kAudioUnitType_Panner
```
AU main type.
### pluginAUSandboxSafe
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Check this box if your plug-in is sandbox safe. A sand-box safe plug-in is loaded in a restricted path and can only access it's own bundle resources and the Music folder. Your plug-in must be able to deal with this. Newer versions of GarageBand require this to be enabled.
### pluginVSTNumMidiInputs
#### Choice ####
Can be one of these values
```
1 :- 1
2 :- 2
3 :- 3
4 :- 4
5 :- 5
6 :- 6
7 :- 7
8 :- 8
9 :- 9
10 :- 10
11 :- 11
12 :- 12
13 :- 13
14 :- 14
15 :- 15
```
For VST and VST3 plug-ins that accept MIDI, this allows you to configure the number of inputs.
### pluginVSTNumMidiOutputs
#### Choice ####
Can be one of these values
```
1 :- 1
2 :- 2
3 :- 3
4 :- 4
5 :- 5
6 :- 6
7 :- 7
8 :- 8
9 :- 9
10 :- 10
11 :- 11
12 :- 12
13 :- 13
14 :- 14
15 :- 15
```
For VST and VST3 plug-ins that produce MIDI, this allows you to configure the number of outputs.
### pluginVST3Category
#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
Fx :- Fx
Instrument :- Instrument
Analyzer :- Analyzer
Delay :- Delay
Distortion :- Distortion
Drum :- Drum
Dynamics :- Dynamics
EQ :- EQ
External :- External
Filter :- Filter
Generator :- Generator
Mastering :- Mastering
Modulation :- Modulation
Mono :- Mono
Network :- Network
NoOfflineProcess :- NoOfflineProcess
OnlyOfflineProcess :- OnlyOfflineProcess
OnlyRT :- OnlyRT
Pitch Shift :- Pitch Shift
Restoration :- Restoration
Reverb :- Reverb
Sampler :- Sampler
Spatial :- Spatial
Stereo :- Stereo
Surround :- Surround
Synth :- Synth
Tools :- Tools
Up-Downmix :- Up-Downmix
```
VST3 category. Most hosts require either "Fx" or "Instrument" to be selected in order for the plugin to be recognised. If neither of these are selected, the appropriate one will be automatically added based on the "Plugin is a synth" option.
### pluginAAXCategory
#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
0 :- None
1 :- EQ
2 :- Dynamics
4 :- PitchShift
8 :- Reverb
16 :- Delay
32 :- Modulation
64 :- Harmonic
128 :- NoiseReduction
256 :- Dither
512 :- SoundField
1024 :- HWGenerators
2048 :- SWGenerators
4096 :- WrappedPlugin
8192 :- Effect
65536 :- MIDIEffect
```
AAX category.
### pluginVSTCategory
#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
kPlugCategUnknown :- kPlugCategUnknown
kPlugCategEffect :- kPlugCategEffect
kPlugCategSynth :- kPlugCategSynth
kPlugCategAnalysis :- kPlugCategAnalysis
kPlugCategMastering :- kPlugCategMastering
kPlugCategSpacializer :- kPlugCategSpacializer
kPlugCategRoomFx :- kPlugCategRoomFx
kPlugSurroundFx :- kPlugSurroundFx
kPlugCategRestoration :- kPlugCategRestoration
kPlugCategOfflineProcess :- kPlugCategOfflineProcess
kPlugCategShell :- kPlugCategShell
kPlugCategGenerator :- kPlugCategGenerator
```
VST category.
### pluginLV2URI
#### Type: String of max length of max 128 characters. ####
This acts as a unique identifier for this plugin. If you make any incompatible changes to your plugin (remove parameters, reorder parameters, change preset format etc.) you MUST change this value. LV2 hosts will assume that any plugins with the same URI are interchangeable.
### pluginARAAnalyzableContent
#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
1 :- Notes
2 :- Tempo Entries
4 :- Bar Signatures
8 :- Static Tuning
16 :- Dynamic Tuning Offsets
32 :- Key Signatures
64 :- Sheet Chords
```
ARA Analyzeable Content Types.
### pluginARATransformFlags
#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
1 :- Time Stretch
2 :- Time Stretch (reflecting tempo)
4 :- Content Based Fades At Tail
8 :- Content Based Fades At Head
```
ARA Transformation Flags.
### pluginARAFactoryID
#### Type: String of max length of max 256 characters. ####
ARA Factory ID.
### pluginARAArchiveID
#### Type: String of max length of max 256 characters. ####
ARA Document Archive ID.
### pluginARACompatibleArchiveIDs
#### Type: String of max length of max 1024 characters. ####
List of compatible ARA Document Archive IDs - one per line
### maxBinaryFileSize
#### Choice ####
Can be one of these values
```
20480 :- 20480
10240 :- 10240
6144 :- 6144
2048 :- 2048
1024 :- 1024
512 :- 512
256 :- 256
128 :- 128
64 :- 64
```
When splitting binary data into multiple cpp files, the Projucer attempts to keep the file sizes below this threshold. (Note that individual resource files which are larger than this size cannot be split across multiple cpp files).
### includeBinaryDataInJuceHeader
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Include BinaryData.h in the JuceHeader.h file
### binaryDataNamespace
#### Type: String of max length of max 256 characters. ####
The namespace containing the binary assets.
### cppStandard
The standard of the C++ language that will be used for compilation.
### preprocessorDefs
#### Type: String of max length of max 32768 characters. ####
Global preprocessor definitions. Use the form "NAME1=value NAME2=value", using whitespace, commas, or new-lines to separate the items - to include a space or comma in a definition, precede it with a backslash.
### headerSearchPaths
Global header search paths.
### postExportShellCommandPosix
#### Type: String of max length of max 1024 characters. ####
A command that will be executed by the system shell after saving this project on macOS or Linux. The string "%%1%%" will be substituted with the absolute path to the project root folder.
### postExportShellCommandWin
#### Type: String of max length of max 1024 characters. ####
A command that will be executed by the system shell after saving this project on Windows. The string "%%1%%" will be substituted with the absolute path to the project root folder.
### userNotes
#### Type: String of max length of max 32768 characters. ####
Extra comments: This field is not used for code or project generation, it's just a space where you can express your thoughts.
