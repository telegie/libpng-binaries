#!/usr/bin/env python3
import platform
import subprocess
from pathlib import Path


def build_zlib():
	here = Path(__file__).parent.resolve()
	subprocess.run(["python3", f"{here}/zlib-binaries/build.py"])


def build_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
    			    "-S", f"{here}/libpng",
    			    "-B", f"{here}/build/arm64-mac",
    			    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-mac",
    			    "-D", f"DZLIB_ROOT={here}/zlib-binaries/1.2.11/arm64-mac",
    			    "-D", "PNG_SHARED=0",
    			    "-D", "PNG_ARM_NEON=off"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "-j8"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "install"])


def build_ios_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
    			    "-S", f"{here}/libpng",
    			    "-B", f"{here}/build/arm64-ios",
    			    "-D", "CMAKE_SYSTEM_NAME=iOS",
    			    "-D", "CMAKE_OSX_DEPLOYMENT_TARGET=14.0",
    			    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-ios",
    			    "-D", "PNG_SHARED=0",
    			    "-D", "PNG_ARM_NEON=on",
    			    "-D", "CMAKE_SYSTEM_PROCESSOR=arm"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-ios", "-j8"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-ios", "install"])


def build_iphonesimulator_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
    			    "-S", f"{here}/libpng",
    			    "-B", f"{here}/build/arm64-iphonesimulator",
    			    "-D", "CMAKE_SYSTEM_NAME=iOS",
    			    "-D", "CMAKE_OSX_DEPLOYMENT_TARGET=14.0",
    			    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-iphonesimulator",
    			    "-D", "PNG_SHARED=0",
    			    "-D", "PNG_ARM_NEON=on",
    			    "-D", "CMAKE_SYSTEM_PROCESSOR=arm",
    			    "-D", "CMAKE_OSX_SYSROOT=iphonesimulator"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-iphonesimulator", "-j8"])
    subprocess.run(["make", "-C", f"{here}/build/arm64-iphonesimulator", "install"])


def main():
    build_zlib()

    if platform.system() == "Darwin":
        build_mac_binaries()
        build_ios_binaries()
        build_iphonesimulator_binaries()


if __name__ == "__main__":
	main()
