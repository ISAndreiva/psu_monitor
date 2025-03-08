#include <Arduino.h>
#include <Wire.h>
#include "pmbus.h"
#include <ESP8266WiFi.h>
#include <espnow.h>

static const char     *title = "PMBus", *build_date = __DATE__;
static PMBus           psu;
uint8_t broadcastAddress[] = {0x2C, 0x3A, 0xE8, 0x3D, 0xD5, 0x38};

typedef struct psu_message {
  float I_in, V_in, W_in, I_out, V_out, W_out, fan_rpm, T1, T2, T3;
} psu_message;

  psu_message psu_data;

void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Last Packet Send Status: ");
  if (sendStatus == 0){
    Serial.println("Delivery success");
  }
  else{
    Serial.println("Delivery fail");
  }
}

void setup() {

  int  status, i;
  char text[128];

  text[0] =
  status  = i = 0;

  Wire.begin(2,0);
  WiFi.mode(WIFI_STA);
    if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }
  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(OnDataSent);
  esp_now_add_peer(broadcastAddress, ESP_NOW_ROLE_SLAVE, 11, NULL, 0);


  Serial.begin(115200);
  Wire.setClock(100000);

  Serial.print("\r\n");
  Serial.print((char *) title);
  Serial.print("\r\n");
  Serial.print((char *) build_date);
  Serial.print("\r\n\n");

  //

  delay(100);

  psu.init(NULL,NULL,0,0x58,&Serial, &Wire);
  psu.check_model();
}

/*
 * 
 */

void loop() {
  
  
  psu.scan();

  /*
  Serial.println("AC:");
  Serial.println(psu.I_in);
  Serial.println(psu.V_in);
  Serial.println("DC:");
  Serial.println(psu.I_out);
  Serial.println(psu.V_out);
  Serial.println(psu.W_out);
  Serial.println("PSU Data:");
  Serial.println(psu.fan[0]);
  Serial.println(psu.T[0]);
  Serial.println(psu.T[1]);
  Serial.println(psu.T[2]);
  */

  psu_data.I_in = psu.I_in;
  psu_data.V_in = psu.V_in;
  psu_data.W_in = psu.W_in;
  psu_data.I_out = psu.I_out;
  psu_data.V_out = psu.V_out;
  psu_data.W_out = psu.W_out;
  psu_data.fan_rpm = psu.fan[0];
  psu_data.T1 = psu.T[0];
  psu_data.T2 = psu.T[1];
  psu_data.T3 = psu.T[2];

  

  esp_now_send(broadcastAddress, (uint8_t *) &psu_data, sizeof(psu_data));

  delay(1000);
}


/*
 *
 */

