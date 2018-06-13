#!/bin/sh

if [ "$#" -lt 1 ]; then
    echo Usage $0 [cmd]
    exit 1
fi

IMAGE=blang/latex:ctanfull
exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/data "$IMAGE" "$@"
