#include <avr/io.h>
#include <util/delay.h>

void setup() {
  // Set PORTB:2 (physical pin 7) as an output
  DDRB |= (1 << PB2);
}

void loop() {
  // Toggle the state of PORTB:2 every 500ms (1Hz)
  PORTB ^= (1 << PB2);
  _delay_ms(2);
}
