# File Transfer DXL Python Client Library
[![OpenDXL Bootstrap](https://img.shields.io/badge/Built%20With-OpenDXL%20Bootstrap-blue.svg)](https://github.com/opendxl/opendxl-bootstrap-python)
[![Build Status](https://travis-ci.org/opendxl-community/opendxl-file-transfer-client-python.png?branch=master)](https://travis-ci.org/opendxl-community/opendxl-file-transfer-client-python)

## Overview

The File Transfer DXL Python client library provides the ability to transfer
files via the
[Data Exchange Layer](http://www.mcafee.com/us/solutions/data-exchange-layer.aspx)
(DXL) fabric.

OpenDXL brokers are configured by default to limit the maximum size of a message
to 1 MB. The File Transfer DXL Python client allows the contents of a file to be
transferred in segments small enough to fit into a DXL message.

This client can be used in conjunction with the
[File Transfer DXL Service](https://github.com/opendxl-community/opendxl-file-transfer-client-python),
an application which registers a service with the DXL fabric and a request
callback which can store files sent to it.

## Documentation

See the [Wiki](https://github.com/opendxl-community/opendxl-file-transfer-client-python/wiki)
for an overview of the File Transfer API DXL Python client library and usage
examples.

See the
[File Transfer DXL Python client documentation](https://opendxl-community.github.io/opendxl-file-transfer-client-python/pydoc)
for installation instructions, API documentation, and usage examples.

## Installation

To start using the File Transfer DXL Python client library:

* Download the [Latest Release](https://github.com/opendxl-community/opendxl-file-transfer-client-python/releases)
* Extract the release .zip file
* View the `README.html` file located at the root of the extracted files.
  * The `README` links to the documentation which includes installation
    instructions and usage examples.

## Bugs and Feedback

For bugs, questions and discussions please use the
[GitHub Issues](https://github.com/opendxl-community/opendxl-file-transfer-client-python/issues).

## LICENSE

Copyright 2018
