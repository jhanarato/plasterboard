Having slapped this project together in an afternoon, I was surprised to get a pull request from one of the fine folks on the ArjunCodes Discord server.

To be accepted, any changes made should support this use case:

## Plasterboard Estimation Use Case

Given a building constructed using a stud frame:

1) Create a list of rooms in the building. (eg. Bathroom, Bedroom 1)
2) Create a list of surfaces for each room, typically walls and ceilings though a room may be more irregular in shape. 
3) Select the sheet material and quantity for each surface.
4) Supply the number of sheets used on a surface (typically 1 or 2, though it's possible to use more).
5) Using the information provided, produce a [bill of materials](https://en.wikipedia.org/wiki/Bill_of_materials). This breaks down the required materials by room and then gives a summary that can be passed on to suppliers for a quote.