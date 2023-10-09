#pragma once

#include <WiFi.h>
#include "esp_wpa2.h"

void wifi_scan(const char* essid, const char* username, const char* password) {
    bool ssidFound = false;
    delay(10);

    // disconnect from AP if previously connected
    WiFi.mode(WIFI_STA);

    WiFi.disconnect();

    // scan until we can find WiFi
    while (!ssidFound) {
        Serial.println("scan start");
        int n_networks = WiFi.scanNetworks();
        Serial.println("scan done");

        if (n_networks == 0) {
            Serial.println("no networks found");
        } else {
            Serial.printf("%d networks found\n", n_networks);
            Serial.print(n_networks);

            for (int i = 0; i < n_networks; ++i) {
                String ssid = WiFi.SSID(i);
                int    rssi = WiFi.RSSI(i); // signal str

                Serial.printf("%d: %s (%d) %c",
                              i + 1,
                              ssid.c_str(),
                              rssi,
                              WiFi.encryptionType(i) ==
                              WIFI_AUTH_OPEN ? ' ' : '*');

                delay(10);

                ssid.trim();
                if (ssid == essid) {
                    Serial.printf(" <==== network found");
                    ssidFound = true;
                }
                Serial.println("");
            }
        }
        Serial.println("");

        // Wait a bit before scanning
        if (!ssidFound)
            delay(5000);
    }

    // disconnect from AP
    Serial.printf("Connecting to %s", essid);
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();

    // wpa2 connection
    esp_wifi_sta_wpa2_ent_set_username((uint8_t *)username,
                                       strlen(username));
    esp_wifi_sta_wpa2_ent_set_password((uint8_t *)password,
                                      strlen(password));
    esp_wifi_sta_wpa2_ent_enable();

    WiFi.begin(essid); // c o n n e c t
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }

    Serial.printf("WiFi is connected to: %s\n", essid);
    Serial.printf("IP address: %s\n",
                  WiFi.localIP().toString().c_str()); // LAN IP
}
