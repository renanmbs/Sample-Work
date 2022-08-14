//Imported libraries
#include <esp_now.h>
#include <WiFi.h>
#define CHANNEL 1 //Channel

//Parameters
uint8_t macSlaves[][6] = {{0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF}}; //Array of Slaves Mac Adresses (in this case it is not a specified slave)
int slavesCount = sizeof(macSlaves)/6/sizeof(uint8_t); //Size of the array with the Mac Adresses of slaves
uint8_t broadcast[] = {0xFF, 0xFF,0xFF,0xFF,0xFF,0xFF}; //Send message to every ESP around (change to specific ESP if wanted)

void setup() {
  
  Serial.begin(115200);

  //ESP in station mode
  WiFi.mode(WIFI_STA);

  //Show the macAdress
  Serial.print("Mac Address in Station: "); 
  Serial.println(WiFi.macAddress());

  //Start ESP now
  InitESPNow();

  //Loop through each slave
  for(int i = 0; i < slavesCount; i++){
    
    esp_now_peer_info_t slave; //Save the information fromt the slave
    
    slave.channel = CHANNEL; //Channel
    
    slave.encrypt = 0; //No cryptography (change to 1 if needed)

    memcpy(slave.peer_addr, macSlaves[i], sizeof(macSlaves[i]));  ///Copy the address of the array to the system
    
    esp_now_add_peer(&slave); //Start Slave
    
  }
  
  esp_now_register_send_cb(Send_data); //Register what to send

  send(); //Send message

}

//Show that the ESP now initialized correctly
void InitESPNow() {
  
  //Sucessful
  if (esp_now_init() == ESP_OK) {
    Serial.println("ESPNow Init Success");
    
  }
  //Not successfull
  else {
    Serial.println("ESPNow Init Failed");
    ESP.restart(); //Restart ESP Now
  }
}

void send(){
  
  int message = 1953; //Message sending

  //Sending message
  esp_err_t result = esp_now_send(broadcast, (uint8_t*) &message, sizeof(message));
  Serial.print("Send Status: ");
  
  //Se o envio foi bem sucedido
  if (result == ESP_OK) {
    Serial.println(" ");
    Serial.println("*****************************************");
    Serial.println("Success");
    
  }
  //Se aconteceu algum erro no envio
  else {
    Serial.println("Error");
    
  }
}

//Function for an update of the sending
void Send_data(const uint8_t *mac_addr, esp_now_send_status_t status) {

  //Parameter
  char macStr[18];
  
  //Copy the Mac adress to a string
  snprintf(macStr, sizeof(macStr), "%02x:%02x:%02x:%02x:%02x:%02x",
           mac_addr[0], mac_addr[1], mac_addr[2], mac_addr[3], mac_addr[4], mac_addr[5]);
           
  Serial.print("Sent to: "); 
  Serial.println(macStr); //Mac Address sent to

  Serial.print("Status: "); 
  Serial.println(status == ESP_NOW_SEND_SUCCESS ? "Success" : "Fail"); //Status of sending

  delay(1000); //Delay

  send();
}

void loop() {
  
}

 
