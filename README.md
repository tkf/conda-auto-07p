# Conda recipe for AUTO 07p

[![Build Status][travis-img]][travis-url]

Example usage:

```sh
git clone https://github.com/tkf/conda-auto-07p
cd conda-auto-07p
conda build .
conda create --name auto-07p --use-local auto-07p
source activate auto-07p
auto $AUTO_DIR/demos/python/demo2.auto
```

[travis-img]: https://travis-ci.org/tkf/conda-auto-07p.svg?branch=master
[travis-url]: https://travis-ci.org/tkf/conda-auto-07p
