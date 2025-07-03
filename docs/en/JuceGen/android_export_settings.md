# Android Export Settings #

Settings affecting the export of Android Studio projects.

### Attributes ###
[androidAdditionalJavaFolders](#androidadditionaljavafolders)

[androidAdditionalResourceFolders](#androidadditionalresourcefolders)

[androidJavaLibs](#androidjavalibs)

[androidProjectRepositories](#androidprojectrepositories)

[androidRepositories](#androidrepositories)

[androidDependencies](#androiddependencies)

[androidCustomAppBuildGradleContent](#androidcustomappbuildgradlecontent)

[androidGradleSettingsContent](#androidgradlesettingscontent)

[androidScreenOrientation](#androidscreenorientation)

[androidCustomActivityClass](#androidcustomactivityclass)

[androidCustomApplicationClass](#androidcustomapplicationclass)

[androidVersionCode](#androidversioncode)

[androidMinimumSDK](#androidminimumsdk)

[androidTargetSDK](#androidtargetsdk)

[androidExtraAssetsFolder](#androidextraassetsfolder)

[gradleVersion](#gradleversion)

[androidPluginVersion](#androidpluginversion)

[gradleToolchain](#gradletoolchain)

[gradleClangTidy](#gradleclangtidy)

[androidOboeRepositoryPath](#androidoboerepositorypath)

[androidInternetNeeded](#androidinternetneeded)

[androidMicNeeded](#androidmicneeded)

[androidCameraNeeded](#androidcameraneeded)

[androidBluetoothScanNeeded](#androidbluetoothscanneeded)

[androidBluetoothAdvertiseNeeded](#androidbluetoothadvertiseneeded)

[androidBluetoothConnectNeeded](#androidbluetoothconnectneeded)

[androidReadMediaAudioPermission](#androidreadmediaaudiopermission)

[androidReadMediaImagesPermission](#androidreadmediaimagespermission)

[androidReadMediaVideoPermission](#androidreadmediavideopermission)

[androidExternalWritePermission](#androidexternalwritepermission)

[androidInAppBillingPermission](#androidinappbillingpermission)

[androidVibratePermission](#androidvibratepermission)

[androidEnableContentSharing](#androidenablecontentsharing)

[androidOtherPermissions](#androidotherpermissions)

[androidPushNotifications](#androidpushnotifications)

[androidEnableRemoteNotifications](#androidenableremotenotifications)

[androidRemoteNotificationsConfigFile](#androidremotenotificationsconfigfile)

[androidManifestCustomXmlElements](#androidmanifestcustomxmlelements)

[androidKeyStore](#androidkeystore)

[androidKeyStorePass](#androidkeystorepass)

[androidKeyAlias](#androidkeyalias)

[androidKeyAliasPass](#androidkeyaliaspass)

[androidTheme](#androidtheme)


### androidAdditionalJavaFolders
#### Type: String of max length of max 32768 characters. ####
Folders inside which additional java source files can be found (one per line). For example, if you are using your own Activity you should place the java files for this into a folder and add the folder path to this field.
### androidAdditionalResourceFolders
#### Type: String of max length of max 32768 characters. ####
Folders inside which additional resource files can be found (one per line). For example, if you want to add your own layout xml files then you should place a layout xml file inside a folder and add the folder path to this field.
### androidJavaLibs
#### Type: String of max length of max 32768 characters. ####
Java libs (JAR files) (one per line). These will be copied to app/libs folder and "implementation files" dependency will be automatically added to module "dependencies" section for each library, so do not add the dependency yourself.
### androidProjectRepositories
#### Type: String of max length of max 32768 characters. ####
Custom project repositories (one per line). These will be used in project-level gradle file "allprojects { repositories {" section instead of default ones.
### androidRepositories
#### Type: String of max length of max 32768 characters. ####
Module repositories (one per line). These will be added to module-level gradle file repositories section. 
### androidDependencies
#### Type: String of max length of max 32768 characters. ####
Module dependencies (one per line). These will be added to module-level gradle file "dependencies" section. If adding any java libs in "Java libraries to include" setting, do not add them here as they will be added automatically.
### androidCustomAppBuildGradleContent
#### Type: String of max length of max 32768 characters. ####
Additional content to be appended to module's build.gradle inside android { section. 
### androidGradleSettingsContent
#### Type: String of max length of max 32768 characters. ####
You can customize the content of settings.gradle here
### androidScreenOrientation
#### Choice ####
Can be one of these values
```
unspecified :- Portrait and Landscape
portrait :- Portrait
landscape :- Landscape
```
The screen orientations that this app should support
### androidCustomActivityClass
#### Type: String of max length of max 256 characters. ####
If not empty, specifies the Android Activity class name stored in the app's manifest which should be used instead of Android's default Activity. If you specify a custom Activity then you should implement onNewIntent() function like the one in com.rmsl.juce.JuceActivity, if you wish to be able to handle push notification events.
### androidCustomApplicationClass
#### Type: String of max length of max 256 characters. ####
If not empty, specifies the Android Application class name stored in the app's manifest which should be used instead of JUCE's default JuceApp class. If you specify a custom App then you must call com.rmsl.juce.Java.initialiseJUCE somewhere in your code before calling any JUCE functions.
### androidVersionCode
#### Type: String of max length of max 32 characters. ####
An integer value that represents the version of the application code, relative to other versions.
### androidMinimumSDK
#### Type: String of max length of max 32 characters. ####
The number of the minimum version of the Android SDK that the app requires (must be 24 or higher).
### androidTargetSDK
#### Type: String of max length of max 32 characters. ####
The number of the version of the Android SDK that the app is targeting.
### androidExtraAssetsFolder
#### Type: String of max length of max 256 characters. ####
A path to a folder (relative to the project folder) which contains extra android assets.
### gradleVersion
#### Type: String of max length of max 32 characters. ####
The version of gradle that is used to build this app (4.10 is fine for JUCE)
### androidPluginVersion
#### Type: String of max length of max 32 characters. ####
The version of the android build plugin for gradle that is used to build this app
### gradleToolchain
#### Choice ####
Can be one of these values
```
clang :- clang
gcc :- gcc
```
The toolchain that gradle should invoke for NDK compilation (variable model.android.ndk.tooclhain in app/build.gradle)
### gradleClangTidy
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled and the toolchain is clang this will run clang-tidy when compiling.
### androidOboeRepositoryPath
#### Type: String of max length of max 2048 characters. ####
Path to the root of Oboe repository. This path can be absolute, or relative to the build directory. Make sure to point Oboe repository to commit with SHA c5c3cc17f78974bf005bf33a2de1a093ac55cc07 before building. Leave blank to use the version of Oboe distributed with JUCE.
### androidInternetNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.INTERNET flag in the manifest.
### androidMicNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.RECORD_AUDIO flag in the manifest.
### androidCameraNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.CAMERA flag in the manifest.
### androidBluetoothScanNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.BLUETOOTH_SCAN, android.permission.BLUETOOTH and android.permission.BLUETOOTH_ADMIN flags in the manifest. This is required for Bluetooth MIDI on Android.
### androidBluetoothAdvertiseNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.BLUETOOTH_ADVERTISE, android.permission.BLUETOOTH and android.permission.BLUETOOTH_ADMIN flags in the manifest.
### androidBluetoothConnectNeeded
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.BLUETOOTH_CONNECT, android.permission.BLUETOOTH and android.permission.BLUETOOTH_ADMIN flags in the manifest. This is required for Bluetooth MIDI on Android.
### androidReadMediaAudioPermission
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.READ_MEDIA_AUDIO and android.permission.READ_EXTERNAL_STORAGE flags in the manifest.
### androidReadMediaImagesPermission
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.READ_MEDIA_IMAGES and android.permission.READ_EXTERNAL_STORAGE flags in the manifest.
### androidReadMediaVideoPermission
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.READ_MEDIA_VIDEO and android.permission.READ_EXTERNAL_STORAGE flags in the manifest.
### androidExternalWritePermission
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.WRITE_EXTERNAL_STORAGE flag in the manifest.
### androidInAppBillingPermission
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the com.android.vending.BILLING flag in the manifest.
### androidVibratePermission
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, this will set the android.permission.VIBRATE flag in the manifest.
### androidEnableContentSharing
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
If enabled, your app will be able to share content with other apps.
### androidOtherPermissions
#### Type: String of max length of max 2048 characters. ####
A space-separated list of other permission flags that should be added to the manifest.
### androidPushNotifications
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable this to grant your app the capability to receive push notifications.
### androidEnableRemoteNotifications
#### Choice ####
Can be one of these values
```
Enabled = 1
Disabled = 0
```
Enable to be able to send remote notifications to devices running your app (min API level 14). Enable the "Push Notifications Capability" setting, provide Remote Notifications Config File, configure your app in Firebase Console and ensure you have the latest Google Repository in Android Studio's SDK Manager.
### androidRemoteNotificationsConfigFile
#### Type: String of max length of max 2048 characters. ####
Path to google-services.json file. This will be the file provided by Firebase when creating a new app in Firebase console.
### androidManifestCustomXmlElements
#### Type: String of max length of max 8192 characters. ####
You can specify custom AndroidManifest.xml content overriding the default one generated by Projucer. Projucer will automatically create any missing and required XML elements and attributes and merge them into your custom content.
### androidKeyStore
#### Type: String of max length of max 2048 characters. ####
The key.store value, used when signing the release package.
### androidKeyStorePass
#### Type: String of max length of max 2048 characters. ####
The key.store password, used when signing the release package.
### androidKeyAlias
#### Type: String of max length of max 2048 characters. ####
The key.alias value, used when signing the release package.
### androidKeyAliasPass
#### Type: String of max length of max 2048 characters. ####
The key.alias password, used when signing the release package.
### androidTheme
#### Type: String of max length of max 256 characters. ####
E.g. @android:style/Theme.NoTitleBar or leave blank for default
