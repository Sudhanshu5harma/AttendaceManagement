#include <SoftwareSerial.h> // include the Software Serial Library

SoftwareSerial rfid_reader(7,1); // Creat a Software Serial Object Mapping it to 7th pin as Rx and 1st Pin as Tx

void setup()
{
  rfid_reader.begin(9600); // Initialise Serial Communication with the RFID reader
  Serial.begin(9600); // Initialise Serial Communication with the Serial Monitor
}

void loop()
{
  
  if(rfid_reader.available()) // Check if there is Incoming Data in the RFID Reader Serial Buffer. 
  {
    while(rfid_reader.available()) // Keep reading Byte by Byte from the Buffer till the RFID Reader Buffer is empty
    {
      char input = rfid_reader.read(); // Read 1 Byte of data and store it in a character variable
      Serial.print(input); // Print the Byte
      delay(5); // A small delay - Removing this might make the Program run faster and not respond properly as data from the reader could be slow
    }
    // Print Tag Length
    Serial.println();
  }
}
