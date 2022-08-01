#!/usr/bin/env bash

cmake ../libpng -DCMAKE_INSTALL_PREFIX="../1.6.38-ssrobins/x64-linux" -DZLIB_ROOT="$(dirname $(pwd))/zlib-binaries/1.2.11/x64-linux" -DPNG_SHARED=0 -DCMAKE_C_FLAGS=-fPIC 
