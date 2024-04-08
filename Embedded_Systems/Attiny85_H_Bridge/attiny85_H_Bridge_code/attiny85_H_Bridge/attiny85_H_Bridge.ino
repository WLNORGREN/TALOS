#include <avr/io.h>
#include <util/delay.h>

void setup() {
  // Set PORTB:2 (physical pin 7) as an output
  DDRB |= (1 << PB2);
  // Set PORTB:1 (physical pin 6) as an output
  DDRB |= (1 << PB1);
  // Set PORTB:0 (physical pin 5) as an input
  DDRB &= ~(1 << PB0);

  PORTB |= (1 << PB2);
  PORTB &= ~(1 << PB1);
  PORTB |= (1 << PB0);

  
}

void loop() {

    // Read the value of PB0 pin using bitwise operations
    
  byte portValue = PINB; // Read the whole PORTB register
  byte pinValue = portValue & (1 << PB0); // Extract the value of PB0 using bitwise AND
  
  if (pinValue == 1){
    PORTB = 0; 
    PORTB |= (1 << PB1);
    
    _delay_ms(5);
  }
  else if (pinValue != 1){
    PORTB = 0; 
    PORTB |= (1 << PB2);;
    _delay_ms(5);
  }
 
 
  
}
