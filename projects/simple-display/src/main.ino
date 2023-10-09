#include "Arduino.h"
#include <TFT_eSPI.h>

#include "wifi.hpp"

TFT_eSPI tft = TFT_eSPI();

void setup() {
    Serial.begin(115200);

    tft.init();
    tft.fillScreen(TFT_BLACK);
    wifi_scan("eduroam", "some_username", "some_password");
}

void loop() {
    time_t time_elapsed = 0;

    while (true) {
        tft.fillScreen(TFT_BLACK);
        tft.setCursor(0, 0);
        tft.setTextColor(TFT_YELLOW, TFT_BLACK);
        tft.printf("Time elapsed: %ld", time_elapsed);
        Serial.println("Draw Complete");
        sleep(1);
    }
    return;
}
