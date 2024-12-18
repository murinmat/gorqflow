#!/bin/bash


pyarmor gen -O gorqflow-obfuscated -r -i gorqflow
mv gorqflow gorqflow-original
mv gorqflow-obfuscated/gorqflow gorqflow
python -m build --wheel -o dist
rm -rf gorqflow gorqflow-obfuscated
mv gorqflow-original gorqflow

for file in dist/*.whl; do
    new_name=$(echo "$file" | sed 's/gorqflow/gorqflow-obfuscated/')
    mv "$file" "$new_name"
done
