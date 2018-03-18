# PyCaesarCrypt

[![Build Status](https://travis-ci.org/martinseener/pycaesarcrypt.svg?branch=master)](https://travis-ci.org/martinseener/pycaesarcrypt)

PyCaesarCrypt is a demo repository for showing the usage of [TravisCI](https://travis-ci.org/) with [pytest](https://pytest.org) and implements a python module to encrypt/decrypt things using the [caesar chiffre](https://en.wikipedia.org/wiki/Caesar_cipher) and the special form [ROT13](https://en.wikipedia.org/wiki/ROT13).

### Installation & Usage

```
git clone https://github.com/martinseener/pycaesarcrypt.git
```

From your python script import pycaesarcrypt using

```
from <path> import pycaesarcrypt

# Instantiate the object
pycc = pycaesarcrypt()
result = pycc.encrypt('Text', 14)
```

## Contributing and License

If you want to help me out, you're very welcome.

1. Check for open issues or open a new issue to start a discussion around a feature idea or a bug.
2. Fork the repository on Github and make your changes on your own **development** branch (just branch off of master).
3. Send a pull request (with the **master** branch as the target).

### Changelog

See [CHANGELOG.md](CHANGELOG.md)

### License

PyCaesarCrypt is available under the MIT license. See the [LICENSE](LICENSE) file for more info.