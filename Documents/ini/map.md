After several years of map coding we know that we CANT change cost and build time of unit or structure with map.ini but it turns out to be wrong - its ACTUALLY POSSIBLE to adjust it.

Just copy the code into your map.ini and adjust it on your own choice.
```
PlayerTemplate FactionAmerica
  ProductionCostChange = AmericaCommandCenter -90% ;Reduce Cost
  ProductionCostChange = AmericaVehicleDozer  90% ;Adds Cost
  ProductionTimeChange = AmericaCommandCenter -100% ; Reduce Buildtime
  ProductionTimeChange = AmericaVehicleDozer 500% ; Add Buildtime
End
```

Map.ini Basics Tutorial
http://www.cnclabs.com/forums/cnc_postst10478_Map-ini-basics.aspx
How to make ai dont sell their captured faction buildings in a specific map
http://www.cnclabs.com/forums/cnc_postsm148967_-Tutorial--How-to-make-ai-dont-sell-their-captured-faction-buildings-in-a-specific-map.aspx#post148967
