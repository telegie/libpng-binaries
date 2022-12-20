#!/usr/bin/env python3
import argparse
import platform
import shutil
import subprocess
from pathlib import Path


def build_zlib(parser_args):
    here = Path(__file__).parent.resolve()
    cmd_args = ["python3", f"{here}/zlib-binaries/build.py"]
    if parser_args.rebuild:
        cmd_args += ["--rebuild"]
    subprocess.run(cmd_args, check=True)


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
                    "-G", "Ninja",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-mac",
                    "-D", f"ZLIB_ROOT={here}/zlib-binaries/install/arm64-mac",
                    "-D", "PNG_SHARED=0",
                    "-D", "PNG_ARM_NEON=off"],
                   check=True)
    subprocess.run(["ninja"], cwd=f"{here}/build/arm64-mac", check=True)
    subprocess.run(["ninja", "install"], cwd=f"{here}/build/arm64-mac", check=True)


def build_x64_mac_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/libpng",
                    "-B", f"{here}/build/x64-mac",
                    "-G", "Ninja",
                    "-D", "CMAKE_OSX_ARCHITECTURES=x86_64",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-mac",
                    "-D", f"ZLIB_ROOT={here}/zlib-binaries/install/x64-mac",
                    "-D", "PNG_SHARED=0",
                    "-D", "PNG_ARM_NEON=off"],
                   check=True)
    subprocess.run(["ninja"], cwd=f"{here}/build/x64-mac", check=True)
    subprocess.run(["ninja", "install"], cwd=f"{here}/build/x64-mac", check=True)


def build_arm64_ios_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/libpng",
                    "-B", f"{here}/build/arm64-ios",
                    "-G", "Ninja",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
                    "-D", "CMAKE_SYSTEM_NAME=iOS",
                    "-D", "CMAKE_OSX_DEPLOYMENT_TARGET=14.0",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-ios",
                    "-D", "PNG_SHARED=0",
                    "-D", "PNG_ARM_NEON=on",
                    "-D", "CMAKE_SYSTEM_PROCESSOR=arm"],
                   check=True)
    subprocess.run(["ninja"], cwd=f"{here}/build/arm64-ios", check=True)
    subprocess.run(["ninja", "install"], cwd=f"{here}/build/arm64-ios", check=True)


def build_arm64_iphonesimulator_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/libpng",
                    "-B", f"{here}/build/arm64-iphonesimulator",
                    "-G", "Ninja",
                    "-D", "CMAKE_OSX_ARCHITECTURES=arm64",
                    "-D", "CMAKE_SYSTEM_NAME=iOS",
                    "-D", "CMAKE_OSX_DEPLOYMENT_TARGET=14.0",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/arm64-iphonesimulator",
                    "-D", "PNG_SHARED=0",
                    "-D", "PNG_ARM_NEON=on",
                    "-D", "CMAKE_SYSTEM_PROCESSOR=arm",
                    "-D", "CMAKE_OSX_SYSROOT=iphonesimulator"],
                   check=True)
    subprocess.run(["ninja"], cwd=f"{here}/build/arm64-iphonesimulator", check=True)
    subprocess.run(["ninja", "install"], cwd=f"{here}/build/arm64-iphonesimulator", check=True)


def build_x64_linux_binaries():
    here = Path(__file__).parent.resolve()
    subprocess.run(["cmake",
                    "-S", f"{here}/libpng",
                    "-B", f"{here}/build/x64-linux",
                    "-G", "Ninja",
                    "-D", f"CMAKE_INSTALL_PREFIX={here}/install/x64-linux",
                    "-D", f"ZLIB_ROOT={here}/zlib-binaries/install/x64-linux",
                    "-D", "PNG_SHARED=0",
                    "-D", "CMAKE_C_FLAGS=-fPIC"],
                   check=True)
    subprocess.run(["ninja"], cwd=f"{here}/build/x64-linux", check=True)
    subprocess.run(["ninja", "install"], cwd=f"{here}/build/x64-linux", check=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rebuild", action="store_true")
    parser_args = parser.parse_args()

    build_zlib(parser_args)

    here = Path(__file__).parent.resolve()
    if parser_args.rebuild:
        shutil.rmtree(f"{here}/build")

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
