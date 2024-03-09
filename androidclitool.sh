#!/bin/bash 
shopt -s extglob 
if [ -z "$1" ] 
  then 
    echo "Supply path to  commandlinetools-linux-*_latest.zip" 
    exit 1 
fi 
android_sdk=$(pwd)/android_sdk 
mkdir -p $android_sdk 
unzip $1 -d $android_sdk 
latest=$android_sdk/cmdline-tools/latest 
mkdir -p $latest 
mv $android_sdk/cmdline-tools/!(latest) $latest 
$latest/bin/sdkmanager "ndk;25.2.9519653" "build-tools;33.0.2" "platforms;android-31" "platform-tools" 
cp -avr $android_sdk/cmdline-tools/latest $android_sdk/tools
