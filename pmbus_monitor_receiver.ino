#include <ESP8266WiFi.h>
#include <espnow.h>

typedef struct psu_message {
  float I_in, V_in, W_in, I_out, V_out, W_out, fan_rpm, T1, T2, T3;
} psu_message;
psu_message psu_data;

void OnDataRecv(uint8_t * mac, uint8_t *incomingData, uint8_t len) {
  memcpy(&psu_data, incomingData, sizeof(psu_data));
  Serial.println("Begin transmission");
  Serial.println(psu_data.I_in);
  Serial.println(psu_data.V_in);
  Serial.println(psu_data.W_in);
  Serial.println(psu_data.I_out);
  Serial.println(psu_data.V_out);
  Serial.println(psu_data.W_out);
  Serial.println(psu_data.fan_rpm);
  Serial.println(psu_data.T1);
  Serial.println(psu_data.T2);
  Serial.println(psu_data.T3);
  Serial.println("End transmission");
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_SLAVE);
  esp_now_register_recv_cb(OnDataRecv);
}

void loop() {
  // put your main code here, to run repeatedly:

}
