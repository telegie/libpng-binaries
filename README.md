# libpng-binaries

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


## For iOS

cmake ../libpng -DCMAKE_SYSTEM_NAME=iOS -DCMAKE_OSX_DEPLOYMENT_TARGET=14.0 -DCMAKE_INSTALL_PREFIX="../install" -DPNG_SHARED=0 -DPNG_ARM_NEON=off
make
make install

Note: XCode's toolchain for iOS provide zlib, so no need for us to provide it.
