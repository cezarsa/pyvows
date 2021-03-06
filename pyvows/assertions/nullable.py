#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyVows testing engine
# https://github.com/heynemann/pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

from pyvows import Vows, VowsAssertionError

@Vows.assertion
def to_be_null(topic):
    if topic is not None:
        raise VowsAssertionError('Expected topic(%s) to be None', topic)

@Vows.assertion
def not_to_be_null(topic):
    if topic is None:
        raise VowsAssertionError('Expected topic(%s) not to be None', topic)

