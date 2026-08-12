from machine import Pin, I2C
import ssd1306
import time
import math

# OLED setup
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

frame = 0

while True:
    oled.fill(0)

    # =========================
    # LEFT STATUS
    # =========================

    oled.text("THORIUM", 0, 8)
    oled.text("-01", 0, 24)
    oled.text("ONLINE", 0, 44)

    # Divider
    oled.vline(55, 0, 64, 1)

    # =========================
    # RIGHT ANIMATION
    # =========================

    cx = 91
    cy = 32

    # Draw radar circles manually
    for radius in (8, 15, 22):
        for a in range(0, 360, 8):
            x = int(cx + math.cos(math.radians(a)) * radius)
            y = int(cy + math.sin(math.radians(a)) * radius)

            if 56 <= x < 128 and 0 <= y < 64:
                oled.pixel(x, y, 1)

    # Rotating radar line
    angle = frame * 0.12

    x = int(cx + math.cos(angle) * 22)
    y = int(cy + math.sin(angle) * 22)

    oled.line(cx, cy, x, y, 1)

    # Center
    oled.fill_rect(cx - 1, cy - 1, 3, 3, 1)

    # Moving detection point
    bx = int(cx + math.cos(angle * 1.7) * 15)
    by = int(cy + math.sin(angle * 1.7) * 15)

    oled.fill_rect(bx, by, 2, 2, 1)

    oled.show()

    frame += 1
    time.sleep_ms(60)