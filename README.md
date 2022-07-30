# libpng-binaries

While libpng supports CMake, prebuilding binaries since it leaves some files in weird places when directly used by CMake as a subdirectory.

mkdir build
cd build

## For Windows

cmake ..\libpng -G "Visual Studio 17 2022" -A x64 -DCMAKE_INSTALL_PREFIX="..\install" -DZLIB_ROOT="..\zlib-binaries\1.2.11\x64-windows\release" -DZ_SOLO=1 -DPNG_SHARED=0

Run Install of libpng.sln in Release
Copy files inside \install to the version file and push.

## For Mac

cmake ../libpng -DCMAKE_OSX_ARCHITECTURES=arm64 -DCMAKE_INSTALL_PREFIX="../install" -DZLIB_ROOT="../zlib-binaries/1.2.11/arm64-mac" -DPNG_SHARED=0 -DPNG_ARM_NEON=off
make
make install

Note: Currently, libpng is from https://github.com/ssrobins/libpng/tree/xcode_new_build_system. This is due to PR at https://github.com/glennrp/libpng/pull/359 not being pulled to upstream yet and libpng submodule should face upstream again when this PR is accepted.

## For Linux

cmake ../libpng -DCMAKE_INSTALL_PREFIX="../1.6.38-ssrobins/x64-linux" -DZLIB_ROOT="../zlib-binaries/1.2.11/x64-linux" -DPNG_SHARED=0
make
make install

## For iOS

cmake ../libpng -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_DEPLOYMENT_TARGET=14.0 -DCMAKE_INSTALL_PREFIX="../install" -DPNG_SHARED=0 -DPNG_ARM_NEON=on -DCMAKE_SYSTEM_PROCESSOR=arm
make
make install

Note: XCode's toolchain for iOS provide zlib, so no need for us to provide it. Also, iOS requires neon support from libpng.


## For iPhone Simulator

cmake ../libpng -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_DEPLOYMENT_TARGET=14.0 -DCMAKE_INSTALL_PREFIX="../1.6.38-ssrobins/arm64-iphonesimulator" -DPNG_SHARED=0 -DPNG_ARM_NEON=on -DCMAKE_SYSTEM_PROCESSOR=arm -DCMAKE_OSX_SYSROOT=iphonesimulator

