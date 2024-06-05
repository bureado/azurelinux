#!/bin/bash
# Portions Copyright (c) 2020 Microsoft Corporation

# See verity-parse.sh for documentation.

check() {
    # Only include if requested by the dracut configuration files
    require_binaries trident || return 1
    return 255
}

depends() {
    
}

install() {
    inst "trident"
}