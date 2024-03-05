#!/bin/sh

set -x

flux install --export \
    --cluster-domain xxx.cluster-domain.replace.invalid \
    -n xxx-namespace-replace \
    | sed -re'
        s/xxx\.cluster-domain\.replace\.invalid/{{.Values.internalDomain}}/g;
        s/xxx-namespace-replace/{{.Release.Namespace}}/g' \
    >templates/flux-system.yaml

git add .
git commit -v
