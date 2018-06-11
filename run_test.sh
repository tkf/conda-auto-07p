#!/bin/bash

set -ex

cp -r "${AUTO_DIR}/demos" .

(cd demos/ab; auto ab.auto)
(cd demos/abc; auto abc.auto)

for demo in demos/python/demo*.auto
do
    yes | auto "$demo"
done
