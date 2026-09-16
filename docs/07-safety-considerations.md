# 07 — Safety Considerations

[⬅ Back to README](../README.md)

This work is lower electrical risk than the power/cooling infrastructure in the [capacity expansion project](https://github.com/Suryatejagamidi11/data-center-capacity-expansion-plan), but it's not risk-free, and the same OSHA 10-Hour Construction Safety and Health baseline applies.

- **ESD protection:** wrist strap grounded to the rack frame before handling any switch, transceiver, or card — static discharge is the most common way a technician damages equipment during "routine" troubleshooting.
- **Working in live racks:** confirm which side of a rack (front/back) has other technicians or live cabling before pulling a cable, to avoid disrupting an unrelated production port.
- **Fiber safety:** never look into the end of an active fiber connector or patch cord — laser light from transceivers is invisible and can cause eye damage; always assume a fiber run is live until confirmed otherwise.
- **Ladder/lift work:** overhead cable tray work above 4 ft follows standard fall-protection practice consistent with OSHA construction guidelines, same as the ladder-rack work in the capacity expansion project.
- **Labeling before disconnecting:** never unplug an unlabeled cable to "see what it does" — trace and label it first, since pulling the wrong cable in a live rack can take down unrelated production traffic.
