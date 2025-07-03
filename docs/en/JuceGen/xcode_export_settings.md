# Xcode Export Settings #

Settings affecting the export of Xcode projects.

### Attributes ###
[customXcassetsFolder](#customxcassetsfolder)

[customLaunchStoryboard](#customlaunchstoryboard)

[customXcodeResourceFolders](#customxcoderesourcefolders)

[duplicateAppExResourcesFolder](#duplicateappexresourcesfolder)

[buildNumber](#buildnumber)

[iosDeviceFamily](#iosdevicefamily)

[iPhoneScreenOrientation](#iphonescreenorientation)

[iPadScreenOrientation](#ipadscreenorientation)

[uiFileSharingEnabled](#uifilesharingenabled)

[uiSupportsDocumentBrowser](#uisupportsdocumentbrowser)

[uiStatusBarHidden](#uistatusbarhidden)

[uiRequiresFullScreen](#uirequiresfullscreen)

[documentExtensions](#documentextensions)

[useLegacyBuildSystem](#uselegacybuildsystem)

[applicationCategory](#applicationcategory)

[validArchs](#validarchs)

[appSandbox](#appsandbox)

[appSandboxInheritance](#appsandboxinheritance)

[appSandboxOptions](#appsandboxoptions)

[appSandboxHomeDirRO](#appsandboxhomedirro)

[appSandboxHomeDirRW](#appsandboxhomedirrw)

[appSandboxAbsDirRO](#appsandboxabsdirro)

[appSandboxAbsDirRW](#appsandboxabsdirrw)

[appSandboxExceptionIOKit](#appsandboxexceptioniokit)

[hardenedRuntime](#hardenedruntime)

[hardenedRuntimeOptions](#hardenedruntimeoptions)

[microphonePermissionNeeded](#microphonepermissionneeded)

[microphonePermissionsText](#microphonepermissionstext)

[cameraPermissionNeeded](#camerapermissionneeded)

[cameraPermissionText](#camerapermissiontext)

[bluetoothPermissionNeeded](#bluetoothpermissionneeded)

[bluetoothPermissionText](#bluetoothpermissiontext)

[sendAppleEventsPermissionNeeded](#sendappleeventspermissionneeded)

[sendAppleEventsPermissionText](#sendappleeventspermissiontext)

[iosInAppPurchases](#iosinapppurchases)

[iosContentSharing](#ioscontentsharing)

[iosBackgroundAudio](#iosbackgroundaudio)

[iosBackgroundBle](#iosbackgroundble)

[iosAppGroups](#iosappgroups)

[iCloudPermissions](#icloudpermissions)

[networkingMulticast](#networkingmulticast)

[iosPushNotifications](#iospushnotifications)

[customPList](#customplist)

[pListPreprocess](#plistpreprocess)

[pListPrefixHeader](#plistprefixheader)

[suppressPlistResourceUsage](#suppressplistresourceusage)

[extraFrameworks](#extraframeworks)

[frameworkSearchPaths](#frameworksearchpaths)

[extraCustomFrameworks](#extracustomframeworks)

[embeddedFrameworks](#embeddedframeworks)

[subprojects](#subprojects)

[prebuildCommand](#prebuildcommand)

[postbuildCommand](#postbuildcommand)

[exporterBundleIdentifier](#exporterbundleidentifier)

[iosDevelopmentTeamID](#iosdevelopmentteamid)

[iosAppGroupsID](#iosappgroupsid)

[keepCustomXcodeSchemes](#keepcustomxcodeschemes)

[useHeaderMap](#useheadermap)


### customXcassetsFolder
Platform:- iOS

#### Type: String of max length of max 128 characters. ####
If this field is not empty, your Xcode project will use the custom xcassets folder specified here 
                       for the app icons, and will ignore the Icon files specified above. If the provided xcassets folder 
                       contains a launchimage it will be used, unless a custom storyboard is specified.
### customLaunchStoryboard
Platform:- iOS

#### Type: String of max length of max 256 characters. ####
If this field is not empty then the specified launch storyboard file will be added to the project as an Xcode 
                       resource and will be used for the app's launch screen, otherwise a default blank launch storyboard will be used. 
                       The file path should be relative to the project folder.
### customXcodeResourceFolders
#### Type: String of max length of max 8192 characters. ####
You can specify a list of custom resource folders here (separated by newlines or whitespace). 
                   References to these folders will then be added to the Xcode resources. 
                   This way you can specify them for OS X and iOS separately, and modify the content of the resource folders 
                   without re-saving the Projucer project.
### duplicateAppExResourcesFolder
Platform:- isAudioPluginProject==True

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Disable this to prevent the Projucer from creating a duplicate resources folder for AUv3 app extensions.
### buildNumber
#### Type: String of max length of max 128 characters. ####
The current version of the project. Used to disambiguate different builds of the same project on App Store Connect. 
                   If this field is empty, the project's version will be used as the build number. 
                   For more details about the difference between the project version and build version, see developer.apple.com/library/archive/technotes/tn2420/_index.html
### iosDeviceFamily
Platform:- iOS

#### Choice ####
Can be one of these values
```
1 :- iPhone
2 :- iPad
1,2 :- Universal
```
The device family to target.
### iPhoneScreenOrientation
Platform:- iOS

#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
UIInterfaceOrientationPortrait :- Portrait
UIInterfaceOrientationPortraitUpsideDown :- Portrait Upside Down
UIInterfaceOrientationLandscapeLeft :- Landscape Left
UIInterfaceOrientationLandscapeRight :- Landscape Right
```
The screen orientations that this app should support on iPhones.
### iPadScreenOrientation
Platform:- iOS

#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
UIInterfaceOrientationPortrait :- Portrait
UIInterfaceOrientationPortraitUpsideDown :- Portrait Upside Down
UIInterfaceOrientationLandscapeLeft :- Landscape Left
UIInterfaceOrientationLandscapeRight :- Landscape Right
```
The screen orientations that this app should support on iPads.
### uiFileSharingEnabled
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to expose your app's files to iTunes.
### uiSupportsDocumentBrowser
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to allow the user to access your app documents from a native file chooser.
### uiStatusBarHidden
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to disable the status bar in your app.
### uiRequiresFullScreen
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Disable this to enable non-fullscreen views such as Slide Over or Split View in your app. 
         "You will also need to enable all orientations.
### documentExtensions
Platform:- isGUIApplication

#### Type: String of max length of max 128 characters. ####
A comma-separated list of file extensions for documents that your app can open. 
                       Using a leading '.' is optional, and the extensions are not case-sensitive.
### useLegacyBuildSystem
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to use the deprecated "Legacy Build System" in Xcode 10 and above. 
                   This may fix build issues that were introduced with the new build system in Xcode 10 and subsequently fixed in Xcode 10.2, 
                   however the new build system is recommended for apps targeting Apple silicon.
### applicationCategory
Platform:- OSX

#### Choice ####
Can be one of these values
```
 :- None
public.app-category.business :- Business
public.app-category.developer-tools :- Developer Tools
public.app-category.education :- Education
public.app-category.entertainment :- Entertainment
public.app-category.finance :- Finance
public.app-category.games :- Games
public.app-category.action-games :- Games - Action
public.app-category.adventure-games :- Games - Adventure
public.app-category.arcade-games :- Games - Arcade
public.app-category.board-games :- Games - Board
public.app-category.card-games :- Games - Card
public.app-category.casino-games :- Games - Casino
public.app-category.dice-games :- Games - Dice
public.app-category.educational-games :- Games - Educational
public.app-category.family-games :- Games - Family
public.app-category.kids-games :- Games - Kids
public.app-category.music-games :- Games - Music
public.app-category.puzzle-games :- Games - Puzzle
public.app-category.racing-games :- Games - Racing
public.app-category.role-playing-games :- Games - Role Playing
public.app-category.simulation-games :- Games - Simulation
public.app-category.sports-games :- Games - Sports
public.app-category.strategy-games :- Games - Strategy
public.app-category.trivia-games :- Games - Trivia
public.app-category.word-games :- Games - Word
public.app-category.graphics-design :- Graphics Design
public.app-category.healthcare-fitness :- Healthcare & Fitness
public.app-category.lifestyle :- Lifestyle
public.app-category.medical :- Medial
public.app-category.music :- Music
public.app-category.news :- News
public.app-category.photography :- Photography
public.app-category.productivity :- Productivity
public.app-category.reference :- Reference
public.app-category.social-networking :- Social Networking
public.app-category.sports :- Sports
public.app-category.travel :- Travel
public.app-category.utilities :- Utilities
public.app-category.video :- Video
public.app-category.weather :- Weather
```
The application category.
### validArchs
Platform:- OSX

#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
i386 :- i386
x86_64 :- x86_64
arm64 :- arm64
arm64e :- arm64e
```
The full set of architectures which this project may target. 
                       Each configuration will build for the intersection of this property, and the per-configuration macOS Architecture property
### appSandbox
Platform:- OSX

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to use the app sandbox.
### appSandboxInheritance
Platform:- OSX

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If app sandbox is enabled, this setting will configure a child process to inherit the sandbox of its parent. 
                       Note that if you enable this and have specified any other app sandbox entitlements below, the child process 
                       will fail to launch.
### appSandboxOptions
Platform:- OSX

#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
com.apple.security.network.server :- Network: Incoming Connections (Server)
com.apple.security.network.client :- Network: Outgoing Connections (Client)
com.apple.security.device.camera :- Hardware: Camera
com.apple.security.device.microphone :- Hardware: Microphone
com.apple.security.device.usb :- Hardware: USB
com.apple.security.print :- Hardware: Printing
com.apple.security.device.bluetooth :- Hardware: Bluetooth
com.apple.security.personal-information.addressbook :- App Data: Contacts
com.apple.security.personal-information.location :- App Data: Location
com.apple.security.personal-information.calendars :- App Data: Calendar
com.apple.security.files.user-selected.read-only :- File Access: User Selected File (Read Only)
com.apple.security.files.user-selected.read-write :- File Access: User Selected File (Read/Write)
com.apple.security.files.downloads.read-only :- File Access: Downloads Folder (Read Only)
com.apple.security.files.downloads.read-write :- File Access: Downloads Folder (Read/Write)
com.apple.security.files.pictures.read-only :- File Access: Pictures Folder (Read Only)
com.apple.security.files.pictures.read-write :- File Access: Pictures Folder (Read/Write)
com.apple.security.assets.music.read-only :- File Access: Music Folder (Read Only)
com.apple.security.assets.music.read-write :- File Access: Music Folder (Read/Write)
com.apple.security.assets.movies.read-only :- File Access: Movies Folder (Read Only)
com.apple.security.assets.movies.read-write :- File Access: Movies Folder (Read/Write)
com.apple.security.temporary-exception.audio-unit-host :- Temporary Exception: Audio Unit Hosting
com.apple.security.temporary-exception.mach-lookup.global-name :- Temporary Exception: Global Mach Service
com.apple.security.temporary-exception.mach-register.global-name :- Temporary Exception: Global Mach Service Dynamic Registration
com.apple.security.temporary-exception.shared-preference.read-only :- Temporary Exception: Shared Preference Domain (Read Only)
com.apple.security.temporary-exception.shared-preference.read-write :- Temporary Exception: Shared Preference Domain (Read/Write)
```
Only used if appSandBox is enabled.
### appSandboxHomeDirRO
Platform:- OSX

#### Type: String of max length of max 8192 characters. ####
A list of the corresponding paths (separated by newlines or whitespace). 
                           See Apple's File Access Temporary Exceptions documentation.
### appSandboxHomeDirRW
Platform:- OSX

#### Type: String of max length of max 8192 characters. ####
A list of the corresponding paths (separated by newlines or whitespace). 
                           See Apple's File Access Temporary Exceptions documentation.
### appSandboxAbsDirRO
Platform:- OSX

#### Type: String of max length of max 8192 characters. ####
A list of the corresponding paths (separated by newlines or whitespace). 
                           See Apple's File Access Temporary Exceptions documentation.
### appSandboxAbsDirRW
Platform:- OSX

#### Type: String of max length of max 8192 characters. ####
A list of the corresponding paths (separated by newlines or whitespace). 
                           See Apple's File Access Temporary Exceptions documentation.
### appSandboxExceptionIOKit
Platform:- OSX

#### Type: String of max length of max 8192 characters. ####
A list of IOUserClient subclasses to open or to set properties on. 
            See Apple's IOKit User Client Class Temporary Exception documentation.
### hardenedRuntime
Platform:- OSX

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to use the hardened runtime required for app notarization.
### hardenedRuntimeOptions
Platform:- OSX

#### Multiple Choice ####
Can be a combination of any of these values separated by comma
```
com.apple.security.cs.allow-jit :- Runtime Exceptions: Allow Execution of JIT-compiled Code
com.apple.security.cs.allow-unsigned-executable-memory :- Runtime Exceptions: Allow Unsigned Executable Memory
com.apple.security.cs.allow-dyld-environment-variables :- Runtime Exceptions: Allow DYLD Environment Variables
com.apple.security.cs.disable-library-validation :- Runtime Exceptions: Disable Library Validation
com.apple.security.cs.disable-executable-page-protection :- Runtime Exceptions: Disable Executable Memory Protection
com.apple.security.cs.debugger :- Runtime Exceptions: Debugging Tool
com.apple.security.device.audio-input :- Resource Access: Audio Input
com.apple.security.device.camera :- Resource Access: Camera
com.apple.security.personal-information.location :- Resource Access: Location
com.apple.security.personal-information.addressbook :- Resource Access: Address Book
com.apple.security.personal-information.calendars :- Resource Access: Calendar
com.apple.security.personal-information.photos-library :- Resource Access: Photos Library
com.apple.security.automation.apple-events :- Resource Access: Apple Events
```
Only used if hardenedRuntime is enabled
### microphonePermissionNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to allow your app to use the microphone. 
                      The user of your app will be prompted to grant microphone access permissions.
### microphonePermissionsText
#### Type: String of max length of max 1024 characters. ####
A short description of why your app requires microphone access.
### cameraPermissionNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to allow your app to use the camera. 
                   The user of your app will be prompted to grant camera access permissions.
### cameraPermissionText
#### Type: String of max length of max 1024 characters. ####
A short description of why your app requires camera access.
### bluetoothPermissionNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to allow your app to use Bluetooth on iOS 13.0 and above, and macOS 11.0 and above. 
                   The user of your app will be prompted to grant Bluetooth access permissions.
### bluetoothPermissionText
#### Type: String of max length of max 1024 characters. ####
A short description of why your app requires Bluetooth access.
### sendAppleEventsPermissionNeeded
Platform:- !iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to allow your app to send Apple events. 
         The user of your app will be prompted to grant permissions to control other apps.
### sendAppleEventsPermissionText
Platform:- !iOS

#### Type: String of max length of max 1024 characters. ####
A short description of why your app requires the ability to send Apple events.
### iosInAppPurchases
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to grant your app the capability for in-app purchases. 
                   This option requires that you specify a valid Development Team ID.
### iosContentSharing
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to allow your app to share content with other apps.
### iosBackgroundAudio
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to grant your app the capability to access audio when in background mode. 
                       This permission is required if your app creates a MIDI input or output device.
### iosBackgroundBle
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to grant your app the capability to connect to Bluetooth LE devices when in background mode.
### iosAppGroups
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to grant your app the capability to share resources between apps using the same app group ID.
### iCloudPermissions
Platform:- iOS

#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to grant your app the capability to use native file load/save browser windows on iOS.
### networkingMulticast
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Your app must have this entitlement to send or receive IP multicast or broadcast. 
                   You will also need permission from Apple to use this entitlement.
### iosPushNotifications
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to grant your app the capability to receive push notifications.
### customPList
#### Type: String of max length of max 8192 characters. ####
You can paste the contents of an XML PList file in here, and the settings that it contains will override any 
                   settings that the Projucer creates. BEWARE! When doing this, be careful to remove from the XML any 
                   values that you DO want the Projucer to change!
### pListPreprocess
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to preprocess PList file. This will allow you to set values to preprocessor defines,
                    for instance if you define: #define MY_FLAG 1 in a prefix header file (see PList prefix header), you can have
                    a key with MY_FLAG value and it will be replaced with 1.
### pListPrefixHeader
#### Type: String of max length of max 512 characters. ####
Header file containing definitions used in plist file (see PList Preprocess).
### suppressPlistResourceUsage
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Suppress the resourceUsage key in the target's generated Plist. This is useful for AU
                    plugins that must access resources which cannot be declared in the resourceUsage block, such
                    as UNIX domain sockets. In particular, PACE-protected AU plugins may require this option to be enabled
                    in order for the plugin to load in GarageBand.
### extraFrameworks
#### Type: String of max length of max 2048 characters. ####
A comma-separated list of extra system frameworks that should be added to the build. 
                   (Don't include the .framework extension in the name)
                    The frameworks are expected to be located in /System/Library/Frameworks
### frameworkSearchPaths
#### Type: String of max length of max 8192 characters. ####
A set of paths to search for custom frameworks (one per line).
### extraCustomFrameworks
#### Type: String of max length of max 8192 characters. ####
Paths to custom frameworks that should be added to the build (one per line). 
                   You will probably need to add an entry to the Framework Search Paths for each unique directory.
### embeddedFrameworks
#### Type: String of max length of max 8192 characters. ####
Paths to frameworks to be embedded with the app (one per line). 
                   If you are adding a framework here then you do not need to specify it in Extra Custom Frameworks too. 
                   You will probably need to add an entry to the Framework Search Paths for each unique directory.
### subprojects
#### Type: String of max length of max 8192 characters. ####
Paths to Xcode projects that should be added to the build (one per line). 
                   These can be absolute or relative to the build directory. 
                   The names of the required build products can be specified after a colon, comma separated, 
                   e.g. "path/to/MySubProject.xcodeproj: MySubProject, OtherTarget". 
                   If no build products are specified, all build products associated with a subproject will be added.
### prebuildCommand
#### Type: String of max length of max 32768 characters. ####
Some shell-script that will be run before a build starts.
### postbuildCommand
#### Type: String of max length of max 32768 characters. ####
Some shell-script that will be run after a build completes.
### exporterBundleIdentifier
#### Type: String of max length of max 256 characters. ####
Use this to override the project bundle identifier for this exporter. 
                   This is useful if you want to use different bundle identifiers for Mac and iOS exporters in the same project.
### iosDevelopmentTeamID
#### Type: String of max length of max 10 characters. ####
The Team ID to be used for setting up code-signing for your application. 
                   This is a ten-character string (for example "S7B6T5XJ2Q") that can be found under the "Organisational Unit"
                   field of your developer certificate in Keychain Access or in the membership page of your account on developer.apple.com.
### iosAppGroupsID
Platform:- iOS

#### Type: String of max length of max 256 characters. ####
The App Group ID to be used for allowing multiple apps to access a shared resource folder. Multiple IDs can be 
                       added separated by a semicolon. The App Groups Capability setting must be enabled for this setting to have any effect.
### keepCustomXcodeSchemes
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to keep any Xcode schemes you have created for debugging or running, e.g. to launch a plug-in in 
                   various hosts. If disabled, all schemes are replaced by a default set.
### useHeaderMap
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to make Xcode search all the projects folders for include files. This means you can be lazy 
                   and not bother using relative paths to include your headers, but it means your code won't be 
                   compatible with other build systems
