# PRD: ESPHome-Based Dual Button Dimmer Control

## Overview
This project defines a Home Assistant automation blueprint for controlling a dimmable light using two binary sensors (e.g. from ESPHome) representing an "Up" and a "Down" button. The buttons support tap and hold behaviors.

## Goals

- ✅ Support two physical buttons (UP/DOWN)
- ✅ Distinguish tap vs hold by duration
- ✅ Tap = on/off or brightness step
- ✅ Hold = continuous dimming loop
- ✅ Avoid deprecated `script.dimming_loop_stop`
- ✅ Avoid re-flashing hardware
- ✅ Keep blueprint self-contained + clean

## Inputs

- `up_button`: Binary sensor (e.g., GPIO or Zigbee)
- `down_button`: Binary sensor
- `target_light`: Light entity

## Functional Requirements

- Trigger on `state_changed` for buttons
- Only run logic on `new_state.state == 'off'`
- Measure press duration in milliseconds
- Tap = 50–400ms
- Hold ≥ 400ms
- On tap/hold:
  - UP: brightness_step_pct 10% / dimming loop
  - DOWN: turn_off / dimming loop down
- Use `mode: restart`

## Blueprint

```yaml
blueprint:
  name: Dimmer with Two Buttons (Tap + Hold)
  description: >
    Tap to turn on/off or change brightness. Hold to adjust brightness smoothly.
    Requires `dimming_loop` and `dimming_loop_down` scripts to exist in your system.

  domain: automation
  source_url: https://github.com/jacobmr/blueprints/blob/main/dimmer_two_button.yaml
  input:
    up_button:
      name: UP Button
      selector:
        entity:
          domain: binary_sensor
    down_button:
      name: DOWN Button
      selector:
        entity:
          domain: binary_sensor
    target_light:
      name: Light to control
      selector:
        target:
          entity:
            domain: light

trigger:
  - platform: event
    event_type: state_changed
    event_data:
      entity_id: !input up_button
  - platform: event
    event_type: state_changed
    event_data:
      entity_id: !input down_button

variables:
  light_entity: !input target_light
  up_button_id: !input up_button
  down_button_id: !input down_button
  tap_min_ms: 50
  tap_max_ms: 400

action:
  - variables:
      is_up: "{{ trigger.event.data.entity_id == up_button_id }}"
      new_state: "{{ trigger.event.data.new_state }}"
      old_state: "{{ trigger.event.data.old_state }}"
      event_duration_ms: >
        {% set start = old_state.last_changed.timestamp() %}
        {% set end = new_state.last_changed.timestamp() %}
        {{ ((end - start) * 1000) | int }}

  - choose:
      - conditions: "{{ new_state.state == 'off' }}"
        sequence:
          - choose:
              - conditions: "{{ is_up }}"
                sequence:
                  - choose:
                      - conditions: "{{ event_duration_ms > tap_min_ms and event_duration_ms < tap_max_ms }}"
                        sequence:
                          - service: light.turn_on
                            data:
                              entity_id: "{{ light_entity }}"
                              brightness_step_pct: 10
                              transition: 0.3
                      - conditions: "{{ event_duration_ms >= tap_max_ms }}"
                        sequence:
                          - service: script.dimming_loop
                            data:
                              variables:
                                target_light: "{{ light_entity }}"
              - conditions: "{{ not is_up }}"
                sequence:
                  - choose:
                      - conditions: "{{ event_duration_ms > tap_min_ms and event_duration_ms < tap_max_ms }}"
                        sequence:
                          - service: light.turn_off
                            data:
                              entity_id: "{{ light_entity }}"
                      - conditions: "{{ event_duration_ms >= tap_max_ms }}"
                        sequence:
                          - service: script.dimming_loop_down
                            data:
                              variables:
                                target_light: "{{ light_entity }}"

mode: restart
```

## Required Scripts

### `script.dimming_loop`

```yaml
alias: dimming_loop
mode: restart
fields:
  target_light:
    name: Light
    required: true
sequence:
  - repeat:
      while: []
      sequence:
        - service: light.turn_on
          data:
            entity_id: "{{ target_light }}"
            brightness_step_pct: 5
            transition: 0.2
        - delay:
            milliseconds: 200
```

### `script.dimming_loop_down`

```yaml
alias: dimming_loop_down
mode: restart
fields:
  target_light:
    name: Light
    required: true
sequence:
  - repeat:
      while: []
      sequence:
        - service: light.turn_on
          data:
            entity_id: "{{ target_light }}"
            brightness_step_pct: -5
            transition: 0.2
        - delay:
            milliseconds: 200
```

