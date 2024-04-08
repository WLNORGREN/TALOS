#include <avr/io.h>
#include <util/delay.h>

void setup() {
  // Set PORTB:2 (physical pin 7) as an output
  DDRB |= (1 << PB2);
  // Set PORTB:1 (physical pin 6) as an output
  DDRB |= (1 << PB1);
  // Set PORTB:0 (physical pin 5) as an input
  DDRB |= (0 << PB0);



}

void loop() {
  if (bitRead(PINB,0) == 1){
  // Toggle the state of PORTB:2 if input is HIGH
    PORTB ^= (1 << PB2);
  }
  
  else {
    PORTB ^= (1 << PB1);
  }
  _delay_ms(10);

}
