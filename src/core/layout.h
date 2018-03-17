// Copyright 2017 jem@seethis.link
// Licensed under the MIT license (http://opensource.org/licenses/MIT)

#pragma once

#include "config.h"
#include "core/flash.h"

#include "core/settings.h"

#include "core/flash.h"
#include "core/keycode.h"
#include "core/matrix_interpret.h"
#include "core/util.h"

#ifdef LAYOUT_VARIABLE_LOC
#define __LAYOUT_LOC
#define __LAYOUT_PADDING_LOC
#else
#define __LAYOUT_LOC AT(LAYOUT_ADDR)
#define __LAYOUT_PADDING_LOC AT(LAYOUT_ADDR + sizeof(layout))
#endif

#define LAYOUT_MAX_NUMBER_KEYBOARDS 64
#define LAYOUT_MAX_NUMBER_DEVICES 64

#ifdef NO_MATRIX

#define LAYOUT_PORT_KEY_NUM_MAP_ADDR (LAYOUT_ADDR + 0)

#else

#define LAYOUT_PORT_ROW_PINS_ADDR    (LAYOUT_ADDR + 0)
// #define LAYOUT_PORT_COL_MASKS_ADDR   (LAYOUT_PORT_ROW_PINS_ADDR + MAX_NUM_ROWS)
// #define LAYOUT_PORT_KEY_NUM_MAP_ADDR (LAYOUT_PORT_COL_MASKS_ADDR + IO_PORT_COUNT)
#define LAYOUT_PORT_COL_PINS_ADDR   (LAYOUT_PORT_ROW_PINS_ADDR + MAX_NUM_ROWS)
#define LAYOUT_PORT_KEY_NUM_MAP_ADDR (LAYOUT_PORT_COL_PINS_ADDR + MAX_NUM_COLS)

#endif

// #define LAYOUT_PORT_KEY_NUM_MAP_ADDR (LAYOUT_ADDR + 16)

AT__LAYOUT_ADDR extern const uint8_t g_layout_storage[];
extern XRAM flash_addr_t g_layout_storage_pos[MAX_NUM_KEYBOARDS];

void keyboard_layouts_init(void);
