# Android Export Config Settings #

Settings affecting the configuration of Android Studio projects.

### Attributes ###
[recommendedWarnings](#recommendedwarnings)

[optimisationLevel](#optimisationlevel)

[androidArchitectures](#androidarchitectures)

[androidBuildConfigRemoteNotifsConfigFile](#androidbuildconfigremotenotifsconfigfile)

[androidAdditionalXmlValueResources](#androidadditionalxmlvalueresources)

[androidAdditionalDrawableResources](#androidadditionaldrawableresources)

[androidAdditionalRawValueResources](#androidadditionalrawvalueresources)

[androidCustomStringXmlElements](#androidcustomstringxmlelements)


### recommendedWarnings
#### Choice ####
Can be one of these values
```
LLVM :- Enabled
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
### androidArchitectures
#### Type: String of max length of max 256 characters. ####
A list of the architectures to build (for a fat binary). Leave empty to build for all possible android architectures.
### androidBuildConfigRemoteNotifsConfigFile
#### Type: String of max length of max 2048 characters. ####
Path to google-services.json file. This will be the file provided by Firebase when creating a new app in Firebase console. This will override the setting from the main Android exporter node.
### androidAdditionalXmlValueResources
#### Type: String of max length of max 8192 characters. ####
Paths to additional "value resource" files in XML format that should be included in the app (one per line). If you have additional XML resources that should be treated as value resources, add them here.
### androidAdditionalDrawableResources
#### Type: String of max length of max 8192 characters. ####
Paths to additional "drawable resource" directories that should be included in the app (one per line). They will be added to "res" directory of Android project. Each path should point to a directory named "drawable" or "drawable-<size>" where <size> should be something like "hdpi", "ldpi", "xxxhdpi" etc, for instance "drawable-xhdpi". Refer to Android Studio documentation for available sizes.
### androidAdditionalRawValueResources
#### Type: String of max length of max 8192 characters. ####
Paths to additional "raw resource" files that should be included in the app (one per line). Resource file names must contain only lowercase a-z, 0-9 or underscore.
### androidCustomStringXmlElements
#### Type: String of max length of max 8192 characters. ####
Custom XML resources that will be added to string.xml as children of <resources> element. Example: 
<string name="value">text</string>
<string name2="value2">text2</string>

