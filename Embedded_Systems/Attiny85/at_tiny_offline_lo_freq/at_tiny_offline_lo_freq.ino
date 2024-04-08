#include <avr/io.h>
#include <util/delay.h>



void setup() {
  // Set PORTB:0 (physical pin 5) as an output
  DDRB |= (1 << PB0);
  

}

void loop() {
  // Toggle the state of PORTB:2 every 500ms (1Hz)
  PORTB ^= (1 << PB0);
  _delay_ms(500);

}
