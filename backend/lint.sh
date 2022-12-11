#!/bin/bash

set -e
set -x

mypy --namespace-packages --explicit-package-bases .
flake8 .
black . --check
isort --profile black . --check-only
