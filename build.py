#!/usr/bin/env python3
import platform
import subprocess
from pathlib import Path


def build_zlib():
	here = Path(__file__).parent.resolve()
	subprocess.run(["python3", f"{here}/zlib-binaries/build.py"], check=True)


def build_x64_windows_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/libpng",
                    "-B", f"{here}/build/x64-windows",
                    "-A" "x64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-windows",
                    "-D", f"ZLIB_ROOT={here}/zlib-binaries/install/x64-windows"],
                   check=True)
    subprocess.run(["msbuild",
                    f"{here}/build/x64-windows/INSTALL.vcxproj",
                    "/p:Configuration=RelWithDebInfo"],
                   check=True)


def build_arm64_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
    			    "-S", f"{here}/libpng",
    			    "-B", f"{here}/build/arm64-mac",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
    			    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-mac",
    			    "-D", f"ZLIB_ROOT={here}/zlib-binaries/install/arm64-mac",
    			    "-D", "PNG_SHARED=0",
    			    "-D", "PNG_ARM_NEON=off"],
                   check=True)
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "-j8"], check=True)
    subprocess.run(["make", "-C", f"{here}/build/arm64-mac", "install"], check=True)


def build_x64_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/libpng",
                    "-B", f"{here}/build/x64-mac",
                    "-D", "CMAKE_OSX_ARCHITECTURES=x86_64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-mac",
                    "-D", f"ZLIB_ROOT={here}/zlib-binaries/install/x64-mac",
                    "-D", "PNG_SHARED=0",
                    "-D", "PNG_ARM_NEON=off"],
                   check=True)
    subprocess.run(["make", "-C", f"{here}/build/x64-mac", "-j8"], check=True)
    subprocess.run(["make", "-C", f"{here}/build/x64-mac", "install"], check=True)


def build_arm64_ios_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
    			    "-S", f"{here}/libpng",
    			    "-B", f"{here}/build/arm64-ios",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
    			    "-D", "CMAKE_SYSTEM_NAME=iOS",
                    "-D", "CMAKE_OSX_DEPLOYMENT_TARGET=14.0",
    			    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-ios",
    			    "-D", "PNG_SHARED=0",
    			    "-D", "PNG_ARM_NEON=on",
    			    "-D", "CMAKE_SYSTEM_PROCESSOR=arm"],
                   check=True)
    subprocess.run(["make", "-C", f"{here}/build/arm64-ios", "-j8"], check=True)
    subprocess.run(["make", "-C", f"{here}/build/arm64-ios", "install"], check=True)


def build_arm64_iphonesimulator_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
    			    "-S", f"{here}/libpng",
    			    "-B", f"{here}/build/arm64-iphonesimulator",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
    			    "-D", "CMAKE_SYSTEM_NAME=iOS",
                    "-D", "CMAKE_OSX_DEPLOYMENT_TARGET=14.0",
    			    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-iphonesimulator",
    			    "-D", "PNG_SHARED=0",
    			    "-D", "PNG_ARM_NEON=on",
    			    "-D", "CMAKE_SYSTEM_PROCESSOR=arm",
    			    "-D", "CMAKE_OSX_SYSROOT=iphonesimulator"],
                   check=True)
    subprocess.run(["make", "-C", f"{here}/build/arm64-iphonesimulator", "-j8"], check=True)
    subprocess.run(["make", "-C", f"{here}/build/arm64-iphonesimulator", "install"], check=True)


def build_x64_linux_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/libpng",
                    "-B", f"{here}/build/x64-linux",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-linux",
                    "-D", f"ZLIB_ROOT={here}/zlib-binaries/install/x64-linux",
                    "-D", "PNG_SHARED=0",
                    "-D", "CMAKE_C_FLAGS=-fPIC"],
                   check=True)
    subprocess.run(["make", "-C", f"{here}/build/x64-linux", "-j8"], check=True)
    subprocess.run(["make", "-C", f"{here}/build/x64-linux", "install"], check=True)


def main():
    build_zlib()

    if platform.system() == "Windows":
        build_x64_windows_binaries()
        return
    elif platform.system() == "Darwin":
        build_arm64_mac_binaries()
        build_x64_mac_binaries()
        build_arm64_ios_binaries()
        build_arm64_iphonesimulator_binaries()
        return
    elif platform.system() == "Linux":
        build_x64_linux_binaries()
        return

    raise Exception(f"libpng build not supported.")


if __name__ == "__main__":
	main()
