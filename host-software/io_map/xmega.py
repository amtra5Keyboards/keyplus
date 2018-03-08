#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2018 jem@seethis.link
# Licensed under the MIT license (http://opensource.org/licenses/MIT)

import io_map.chip_id

from io_map.common import IoMapper, IoMapperError, IoMapperPins

XmegaPinsA4U = IoMapperPins(
    ports = {
        'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'R': 5
    },
    pins = [
        0xff,
        0x0f,
        0xff,
        0x3f,
        0x0f,
        0x03,
    ],
    default_rows = [
        'D0', 'D1', 'D2', 'D3', 'D4', 'D5',
        'C3', 'C2', 'C1', 'C0'
    ],
    default_cols = [
        'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7',
        'B0', 'B1', 'B2', 'B3',
        'C0', 'C1', 'C2', 'C3',
    ],
    port_size = 8
)

XmegaPinsA3U = IoMapperPins(
    ports = None,
    pins = None,
    port_size = 8
)

XmegaPinsA1U = IoMapperPins(
    ports = None,
    pins = None,
    port_size = 8
)

class IoMapperXmega(IoMapper):
    XMEGA_SERIES_TABLE = {
        'A4U': XmegaPinsA4U,
        'A3U': XmegaPinsA3U,
        'C3': XmegaPinsA3U, # same as A series
        'A1U': XmegaPinsA1U,
        'C1': XmegaPinsA1U, # same as A series
    }

    def __init__(self, chip_id):
        self.chip_info = io_map.chip_id.lookup_chip_id(chip_id)

        assert(self.chip_info != None)
        assert(self.chip_info.architecture == 'XMEGA')
        assert(self.chip_info.series in self.XMEGA_SERIES_TABLE)
        self.pin_mapper = IoMapperXmega.XMEGA_SERIES_TABLE[self.chip_info.series]

    def get_pin_number(self, pin_name):
        try:
            pin_name = pin_name.upper()
            port = pin_name[0]
            pin = int(pin_name[1:])
        except:
            raise IoMapperError("Invalid pin name '{}', correct format "
                                "is a letter followed by a number. E.g. C1, B0, etc"
                                .format(pin_name))

        if not self.pin_mapper.is_valid_pin(port, pin):
            raise IoMapperError("The pin '{}' does not exist on the given microcontroller '{}'"
                                .format(pin_name, self.chip_info.name))

        return self.pin_mapper.get_pin_number(port, pin)

    def get_pin_name(self, pin_number):
        port_number, pin_bit = self.get_pin(pin_number)
        if port_number not in self.ports or pin_bit > self.port_size:
            raise IoMapperError("Pin number '{}' doesn't exist on this mcu"
                                .format(pin_number))
        return "{port_name}{pin_bit}".format(
            port_name = self.ports[port_number],
            pin_bit = pin_bit,
        )
