# libpng-binaries

While libpng supports CMake, prebuilding binaries since it leaves some files in weird places when directly used by CMake as a subdirectory.

mkdir build
cd build

## For Windows

cmake ..\libpng -G "Visual Studio 17 2022" -A x64 -DCMAKE_INSTALL_PREFIX="..\1.6.38\x64-windows" -DZLIB_ROOT="..\zlib-binaries\1.2.11\x64-windows\release" -DZ_SOLO=1 -DPNG_SHARED=0

Run INSTALL of libpng.sln in Release.

## For Mac

cmake ../libpng -DCMAKE_OSX_ARCHITECTURES=arm64 -DCMAKE_INSTALL_PREFIX="../install" -DZLIB_ROOT="../zlib-binaries/1.2.11/arm64-mac" -DPNG_SHARED=0 -DPNG_ARM_NEON=off
make
make install

## For Linux

cmake ../libpng -DCMAKE_INSTALL_PREFIX="../1.6.38/x64-linux" -DZLIB_ROOT="../zlib-binaries/1.2.11/x64-linux" -DPNG_SHARED=0
make
make install

## For iOS

cmake ../libpng -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_DEPLOYMENT_TARGET=14.0 -DCMAKE_INSTALL_PREFIX="../1.6.38/arm64-ios" -DPNG_SHARED=0 -DPNG_ARM_NEON=on -DCMAKE_SYSTEM_PROCESSOR=arm
make
make install

Note: XCode's toolchain for iOS provide zlib, so no need for us to provide it. Also, iOS requires neon support from libpng.


## For iPhone Simulator

cmake ../libpng -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_DEPLOYMENT_TARGET=14.0 -DCMAKE_INSTALL_PREFIX="../1.6.38/arm64-iphonesimulator" -DPNG_SHARED=0 -DPNG_ARM_NEON=on -DCMAKE_SYSTEM_PROCESSOR=arm -DCMAKE_OSX_SYSROOT=iphonesimulator
