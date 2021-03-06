# Build

ifndef MCU
    MCU = atxmega32a4u
endif

# C_SRC += # extra includes

CDEFS += -DNRF24_CE_PORT=PORTD
CDEFS += -DNRF24_CE_PIN=PIN5_bm

CDEFS += -DVBUS_PIN_PORT=E
CDEFS += -DVBUS_PIN_NUM=2
CDEFS += -DVBUS_PIN_INT_NUM=1

CDEFS += -DNRF24_IRQ_PIN_PORT=C
CDEFS += -DNRF24_IRQ_PIN_NUM=3
CDEFS += -DNRF24_IRQ_INT_NUM=1

USE_USB := 1
USE_SCANNER := 1
USE_NRF24 := 0
USE_CHECK_PIN := 0
USE_I2C := 0
USE_HARDWARE_SPECIFIC_SCAN := 0
