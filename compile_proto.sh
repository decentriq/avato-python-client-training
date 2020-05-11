#!/bin/bash

for proto_file in proto/*.proto; do
    protoc -I=proto --python_out=avato_training/proto $proto_file
done
