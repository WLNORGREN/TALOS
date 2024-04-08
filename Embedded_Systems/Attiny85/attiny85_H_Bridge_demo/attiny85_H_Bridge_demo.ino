#include <avr/io.h>
#include <util/delay.h>

void setup() {
  // Set PORTB:2 (physical pin 7) as an output
  DDRB |= (1 << PB2);
  // Set PORTB:1 (physical pin 6) as an output
  DDRB |= (1 << PB1);

  PORTB |= (1 << PB2);
  PORTB |= (0 << PB1);
}

void loop() {
  
  // Toggle the state of PORTB:2 every 500ms (1Hz)
  PORTB ^= (1 << PB2);
  _delay_ms(500);
  // Toggle the state of PORTB:1 every 500ms (1Hz)
  PORTB ^= (1 << PB1);
  _delay_ms(500);
}
