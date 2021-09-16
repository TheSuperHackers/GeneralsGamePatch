# GeneralsGamePatch
Welcome to the Generals Game Patch project that aims to fix and improve the original Generals Zero Hour 1.04 version.

### Core objectives
- Fix game crashes, exploits and bugs
- Fix severe faction balancing issues for Multiplayer
- Stay true to the original content, design and art direction of Generals Zero Hour 1.04

### Additional objectives
- Build new tools to simplify access and use of Mods, Addons and other optional game content
- Retain best compatibility and accessibility to Original Game version(s), Mods, Addons and Custom Maps
- Improve Game AI
- Improve Menu operability and visuals
- Improve Control Bar operability and visuals
- Fix and improve some models, textures and audio
- Fix and improve Official Maps
- Add new Language(s)

### Community Survey
1: https://bit.ly/zh_survey_1ben

### External Discussions
https://bit.ly/zhpatch

### Issues & Tasks
- https://github.com/xezon/GeneralsGamePatch/issues
- https://github.com/xezon/GeneralsGamePatch/tree/main/Patch104pZH/Design/Tasks

### How to contribute
If you are new to Git, you will need to learn how to use it. Search the web to find resources and git client apps to help you. Fork this repository, clone the fork, commit your changes and create a pull request that we can review.

### How we approach core objectives
In our first survey we asked community how they feel about addressing bugs that affect gameplay: More than 90% of players want bugs to be fixed. Based on this result and also our discussions and experiences in the developer team, we decided to tackle changes and fixes with the following approach:

1. Changes and fixes are decided and created in isolated development branches. If a change has severe controversial, but potentially positive effects on gameplay, then it will be reviewed and tweaked before it goes into the main branch.
2. Changes and fixes are merged into the main development branch, so that they can be tested in a combined setting. No changes are cemented: Tests, reviews and tweaks may be necessary to adjust changes further to fit them together well. If a change causes negative consequences that cannot be tweaked away in a good way, then it may be reverted entirely to the original state.
3. Changes and fixes may require input from pro players for accurate evaluation. Ideally changes are looked at in test environments and real matches to gather accurate data and impressions of a given change. It is worthwhile to know and consider which other controversial changes exist within the same game setting, as they can influence each other.
4. Changes and fixes may be subject to a matter of preference that requires the whole community to give input on. In such cases we will include related questions in new surveys and evaluate and apply the results accordingly.

## Bug fixes and improvements currently applied, in no particular order

| Review | Description |
|:------:|-------------|
|     | Fixed issue that showed wrong model of GLA Battle Bus in bunkered state                                               |
|     | Fixed exploit that granted USA a significant amount of cash after building a Drop Zone                                |
|     | Fixed issue that would permanently reduce the power level of a faction                                                |
|     | Improved the performance of USA Patriot missile assist effect by around 60%                                           |
|     | Fixed issue that prevented China Tank and China Nuke Outposts to attack buildings and terrain                         |
|     | Improved the mobility of the China Dozer to avoid scenarios where it gets stuck unnecessarily                         |
| Yes | Removed Heat Haze effect from Microwave Tank and GPS Scrambler to avoid critical rendering glitches                   |
|     | Fixed critical issue that crashed all clients in a match                                                              |
|     | Fixed issue that made units keep firing onto already killed infantry units                                            |
|     | Fixed issue that spawned wrong USA Ranger types on Particle Cannon kills                                              |
|     | Fixed issue that prevented a stealthed and attacking GLA Palace to reveal itself                                      |
|     | Fixed issue where a player would not be defeated by just owning a GLA Tunnel/Stinger hole                             |
|     | Added red bullet tracers to heroic USA Pathfinders and GLA JarmenKell                                                 |
|     | Fixed exploit that allowed to shoot with the GLA Scud Storm at any time                                               |
|     | Added correct anthrax particle effect colors to Toxin Tractor puddles                                                 |
|     | Fixed issue that allowed to trigger demo traps by placing scaffolds nearby                                            |
|     | Fixed issue that caused Toxin demo trap to prematurely create toxin puddle before explosion                           |
|     | Fixed GLA Stealth Saboteur death voice                                                                                |
|     | Fixed issue that sent the China Supply Truck flying high in the sky when shot                                         |
| Yes | Fixed issue that made it difficult to drive over the China Infantry Minigunner                                        |
|     | Fixed issue that had Toxin Shells lose Projectile effect after acquiring Anthrax Beta                                 |
|     | Fixed issue that made Gamma Toxin Streams have green particles when clearing buildings                                |
|     | Fixed wrong UI portrait image of GLA Sneak attack                                                                     |
|     | Fixed wrong UI ability image of GLA Saboteur                                                                          |
|     | Fixed issue that made Demo GLA Rocket Buggy lose red missile effect after acquiring Rocket Upgrade                    |
|     | Fixed wrong demo charge voice effect for Demo GLA Jarmen Kell                                                         |
|     | Fixed wrong poison death voice effects for USA and China infantry units                                               |
|     | Fixed wrong death voice effects for Demo GLA infantry                                                                 |
|     | Fixed issue that made GLA Marauder become indestructible unit after being crushed by China Overlord tank              |
|     | Expanded army selection drop down box in Menu Game Room to see all factions at once without scrolling                 |
|     | Fixed Demo GLA vehicle destruction effect glitches                                                                    |
|     | Fixed issue that made Demo GLA Combat Bike used by GLA Worker miss the vehicle destruction effect                     |
|     | Fixed issue that made Demo GLA Battle Bus vanish after demo suicide without applying any damage                       |
|     | Added missing faction colors to Snow China Speaker Tower building model                                               |
|     | Fixed issue that allowed GLA Toxin Tractor to attack units standing too close to it                                   |
|     | Fixed issue that hid China Bunkers and China Propaganda Center from radar minimap                                     |
|     | Fixed issue that had China unit upgrades not render with red color when Frenzy power was applied                      |
|     | Expanded menu map selection lists to 1200 entries                                                                     |
|     | Fixed wrong cameo image of USA Alpha Aurora                                                                           |
|     | Fixed issue that prevented to build Drones on multi sub-faction USA Humvee group selection                            |
| Yes | Fixed issue that delayed Demo GLA Technical suicide by up to 0.75 seconds                                             |
|     | Removed obsolete suicide button from Demo GLA Worker when Demo Upgrade is not yet owned                               |
|     | Fixed issue that prevented executing demo suicide with different unit types in a group selection                      |
|     | Fixed issue that prevented evacuating units with different unit types in a group selection                            |
|     | Added missing Demo Upgrade icon to Demo GLA Tunnel and Stinger                                                        |
|     | Fixed issue that made non-VUSA Avengers retaliate with laser guidance ability                                         |
|     | Fixed issue with USA Avenger that had small piece of geometry float nearby                                            |
|     | Fixed issue where GLA Combat Cycle had two death sounds                                                               |
|     | Fixed issue where Laser USA Humvee had two infantry enter sounds                                                      |
|     | Fixed issue that caused USA Pilots to walk slower when fully vetted                                                   |
|     | Removed non-functional Chemical Suits from USA Pilots                                                                 |
|     | Removed non-functional Advanced Training from USA Pilots                                                              |
|     | Fixed issue that made GLA Saboteur disappear when killed on GLA Combat Cycle                                          |
|     | Fixed inconsistency issue that allowed GLA Hijacker and GLA Saboteur ride the Toxin GLA Combat Cycle                  |
|     | USA Spy Drone is no longer selectable with Select All key(s) (Q W)                                                    |
|     | USA Spectre Gunship is no longer selectable with Select All key(s) (Q W)                                              |
|     | Fixed issue where hits on bunkered GLA Battle Bus would cause screen shake effects                                    |
|     | Added missing sounds to USA Sentry Drone movement command                                                             |
|     | Added missing sounds to USA Pilot enter building command                                                              |
|     | Added missing sounds to VGLA Battle Bus                                                                               |
|     | Fixed wrong sounds on USA Fire Base selection                                                                         |
|     | Fixed wrong unit tooltip on Laser USA Aurora                                                                          |
|     | Added missing AP Rocket Upgrade icon to GLA SCUD Launcher cameo                                                       |
|     | Added missing Patriotism Upgrade icon to Infantry China Tank Hunter                                                   |
|     | Added missing Upgrade icons to GLA Rebels                                                                             |
|     | Fixed wrong upgrade icon placements on USA Tomahawk                                                                   |
|     | Fixed China Nuklear Missile exploit                                                                                   |
|     | Fixed issue that had USA Spectre Gunship lose its player color when shot down                                         |
|     | Fixed issue where China Battlemasters from different sub faction did not benefit from Horde Bonus                     |
|     | Fixed broken weapons and animations on GLA HiDef Scud Launcher (cut)                                                  |
|     | Added missing red smoke effect for Demo GLA Terrorist on Combat Cycle after Demo Upgrade                              |
|     | Added missing construction sound effect for USA Sentry Drone                                                          |
|     | Fixed China Nuke Cannon Neutron Shells exploit                                                                        |
|     | Added missing booby trap sound effect for Demo GLA Rebel                                                              |
|     | Fixed issue where some USA Chinooks collected 100 milliseconds slower than others                                     |
|     | Fixed issue where damage smoke effects on China Outpost would not disappear after repair                              |
| Yes | Fixed issue where damage smoke effects on China Outpost would show for enemy player when stealthed                    |
|     | Fixed issue where GLA Battle Bus would turn chassis after targeting air unit                                          |
|     | Fixed issue where GLA Battle Bus would stop moving after targeting air unit                                           |
|     | Fixed issue where USA Humvee without TOW missile would stop moving after targeting air unit                           |
|     | Fixed issue where Toxin GLA Rocket Soldier on Combat Cycle did not shoot with correct rocket type                     |
|     | Fixed issue where Demo GLA Rocket Soldier on Combat Cycle did not shoot with correct rocket type                      |
|     | Fixed issue where GLA Fake Command Center did look different to real Command Center after Fortified Structure upgrade |
|     | Fixed issue where several dummy weapons caused confusing attack notifications                                         |
|     | Fixed issue where China Helix with Gattling Gun could attack air units                                                |
|     | Fixed wrong USA Ranger spawn type of Paradrop ability                                                                 |
|     | Fixed exploit that allowed to shoot on ground units from very far away                                                |
|     | Fixed issue where GLA Stinger would shoot twice without any delay                                                     |
|     | Fixed issue where GLA Stinger would automatically attack enemy buildings                                              |
|     | Fixed wrong particle effect colors on Superweapon USA Particle Cannon                                                 |
|     | Fixed issue where China Carpet Bomber could not be used with the Command Center of another China sub faction          |
|     | Added missing air attack voices for various units                                                                     |
|     | Added missing air attack effects and animations for GLA Stringer                                                      |
|     | Fixed issue where Generals Powers would disappear from Infantry China Command Center after Mines upgrade              |
|     | Fixed issue where Generals Powers would disappear from Nuke China Command Center after Mines upgrade                  |
| Yes | Fixed issue where a Terrorist Car Bomb would stop working after attacking a moving vehicle                            |
|     | Removed EXP bonus from destroying a civilian Repair Pad (cut)                                                         |
|     | Removed EXP bonus from destroying a civilian Reinforcement Pad                                                        |
|     | Added missing muzzle flash for Vehicle Snipe ability of GLA Jarmen Kell on Combat Cycle                               |
|     | Fixed wrong muzzle flash location for Vehicle Snipe ability of GLA Jarmen Kell                                        |
|     | Added red bullet tracer effect to heroic GLA Jarmen Kell                                                              |
|     | Added red bullet tracer effect to heroic USA Pathfinder                                                               |
|     | Fixed issue where Fuel Bomb of USA Alpha Aurora would detonate before the bomb hit the ground                         |
|     | Fixed wrong muzzle flash location of Infantry China Minigunner                                                        |
|     | Fixed broken recoil animation of Infantry China Minigunner                                                            |
| Yes | Fixed incorrect air attack sound of Infantry China Minigunner                                                         |
|     | Fixed issue where China Overlord would turn chassis while Gattling Cannon aims on air units                           |
|     | Fixed issue where GLA Scud Storm could not damage itself                                                              |
|     | Added missing hit effects to USA Cargo Planes with Countermeasures upgrade                                            |
|     | Added missing hit effects to USA Rangers after Chemical Suits upgrade                                                 |
|     | Fixed issues with USA Spectre button, portrait and upgrade icons                                                      |
|     | Added missing Hellfire Drone icon to Boss Paladin                                                                     |
|     | Added missing Mines upgrade to China Speakertower                                                                     |
|     | Improved the 3D model of the Carpet Bomber and Aurora bomb object                                                     |
|     | Fixed various wrong object categories for World Builder                                                               |
|     | Fixed issue where Stealth GLA could not build Hijacker with VGLA Barracks                                             |
|     | Fixed issue where Nuke China could not build Nuke Cannon in VChina and Infantry China Warfactories                    |
|     | Fixed issue where Airforce USA could not build Stealth Fighters in non-Airforce Airfields                             |

## Balance changes currently applied

### Global Changes

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Emergency Repair | | | 240 | 120 |

### Global China

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Cash Hack                |      |      | 240 | 180 |
| Frenzy                   |      |      | 240 | 150 |
| Nuclear Missile          |      |      | 360 | 300 |
| Land Mines               |      |      |  20 |  16 |
| Neutron Mines            | 500  |  400 |  25 |  16 |
| Overlord Gattling Cannon | 1200 | 1000 |     |     |
| Internet Centre          | 2500 | 1750 |     |     |
| Satellite Hack One       | 1000 |  800 |     |     |
| Satellite Hack Two       | 2500 | 1200 |     |     |
| Nationalism              | 2000 | 1500 |     |     |
| NuclearTanks             | 2000 | 1500 |  60 |  40 |
| UraniumShells            | 2500 | 1500 |  60 |  40 |
| Gattling Cannon          | 1200 | 1100 |     |     |
| Neutron Shells           | 2500 | 2000 |  60 |  40 |
| Chain Guns               |      |      |  45 |  40 |
| Helix Napalm Bomb        |      |      |  20 |  10 |
| Inferno Cannons          |      |      |  15 |  14 |

### China

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Red Guard         |      |      | 10 |  9   |
| Tank Hunter       |      |      |  5 |  4.5 |
| Hacker            |  625 |  550 | 20 | 15   |
| Battlemaster      |  800 |  650 |    |      |
| Gattling Tank     |  800 |  700 |    |      |
| Dragon Tank       |  800 |  700 |    |      |
| ECM Tank          |  800 |  750 |    |      |
| Overlord          | 2000 | 1800 |    |      |
| Listening Outpost |      |      | 15 | 14   |
| Troop Crawler     | 1400 | 1200 |    |      |
| Inferno Cannon    |  900 |  800 |    |      |
| Nuke Cannon       | 1600 | 1400 | 20 | 18   |
| Helix             | 1500 | 1400 |    |      |

### Infantry China

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Para Drop        |      |      | 240 | 210   |
| Hacker           |  625 |  600 |  20 |  17.5 |
| Mig              | 1200 | 1350 |     |       |
| Helix            |      |      |  20 |  25   |
| Inferno Cannon   | 1100 | 1000 |  15 |  14   |
| Nuke Cannon      | 1600 | 1400 |  20 |  18   |
| Fortified Bunker |  700 |  750 |   8 |   9   |

### Nuke China

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Nuclear Missile   | 4500 | 5000 |    |    |
| Power Plant       | 1200 | 1100 |    |    |
| Isotope Stability |      |        60 | 40 |
| Red Guard         |  350 |  300 | 12 | 10 |
| Tank Hunter       |  350 |  300 | 7 | 5.5 |
| Hacker            |  625 |  550 | 20 | 15 |
| Black Lotus       | 1600 | 1500 |    |    |
| Listening Outpost |  900 |  850 | 15 | 14 |
| Troop Crawler     | 1400 | 1200 |    |    |
| Nuke Cannon       |      |        20 | 18 |
| Helix             | 1750 | 2000 |    |    |
| Helix Nuke Bomb   |      |        20 | 10 |

### Tank China

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Tank Drop         |      |      | 240 | 180 |
| Red Guard         |  375 |  300 |  12 |  10 |
| Tank Hunter       |  375 |  350 |   7 |   6 |
| Black Lotus       | 1875 | 1500 |     |     |
| Hacker            |  780 |  550 |  20 |  15 |
| Listening Outpost |  950 |  900 |  15 |  14 |
| Mig               | 1600 | 1500 |  12 |  10 |
| Helix             |                25 |  20 |

### Global USA

Composite Armour now gives 25% HP (fixed for all units)

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Composite Armour    | 2000 | 1750 |     |     |
| Paradrop            |      |      | 240 | 150 |
| AirField            | 1000 |  800 |     |     |
| Pathfinder          |  600 |  900 |  10 |  15 |
| Flashbang           |      |         30 |  25 |
| TOW Missile         |  800 | 1000 |     |     |
| Sentry Drone Gun    | 1000 |  500 |  30 |  10 |
| Rocket Pods         |  800 | 1000 |     |     |
| Bunker Buster Bombs | 1500 | 1200 |     |     |
| Stealth Fighter     |      |      |  25 |  20 |
| Scout Drone         |      |      | 100 | 150 |

### USA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Patriot Battery | 1000 |  700 | 25 | 30 |
| Crusader        |  900 |  850 |    |    |
| Paladin         | 1100 | 1000 | 12 | 10 |
| Ambulance       |  600 |  700 |    |    |
| Raptor          | 1400 |  900 |    |    |
| Comanche        | 1500 | 1350 |    |    |
| Stealth Fighter | 1600 |  900 |    |    |
| Aurora          | 2500 | 2000 |    |    |
| Sentry Drone    |  800 |  500 | 10 |  8 |

### Airforce USA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Early Emergency Repair |      |      | 240 | 120 |
| Carpet Bomb            |      |      | 240 | 360 |
| Patriot                | 1000 |  700 |  25 |  30 |
| Chinook                |  950 | 1200 |     |     |
| Combat Chinook         |      |      |  25 |  30 |
| Sentry Drone           |  850 |  500 |  10 |   8 |
| Stealth Fighter        | 1250 |  950 |     |     |

### Laser USA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Laser Crusader  |  900 |  850 |    |    |
| Ambulance       |  600 |  700 |    |    |
| Sentry Drone    |  800 |  500 | 10 |  8 |
| Raptor          | 1400 |  900 |    |    |
| Comanche        | 1500 | 1350 |    |    |
| Stealth Fighter | 1600 |  900 |    |    |
| Aurora          | 2500 | 2000 |    |    |

### Superweapon USA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Particle Uplink Cannon | 2500 | 3000 |    |    |
| Cold Fusion Reaction   |  900 |  800 |    |    |
| Advanced Control Rods  |  500 |  600 | 30 | 25 |
| Humvee                 |  850 |  800 |    |    |
| Sentry Drone           | 1000 |  500 | 10 |  8 |
| Tomahawk               | 1400 | 1200 |    |    |
| Raptor                 | 1400 |  900 |    |    |
| Stealth Fighter        | 1600 |  900 |    |    |
| Comanche               | 1800 | 1350 |    |    |
| Alpha Aurora Bomber    | 2000 | 2500 |    |    |

### Global GLA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Anthrax Beta        | 2500 | 1500 |  30 |  40 |
| BioBomb             |  500 |  300 |     |     |
| HighExplosiveBomb   |  500 |  400 |     |     |
| FortifiedStructures | 1000 | 1500 |     |     |
| Scud Storm          |      |      | 300 | 360 |
| Scud Launcher       |      |      |  15 |  14 |

### GLA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Booby Trap   | 1000 |  400 | 40 | 15 |
| Camouflage   | 2000 | 1000 | 60 | 30 |
| Hijacker     |      |      | 10 |  5 |
| Saboteur     |      |      | 15 | 10 |
| Bomb Truck   | 1200 | 1100 | 15 | 12 |
| Combat Cycle |  500 |  400 |    |    |

### Toxin GLA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Anthrax Gamma | 1500 | 2000 |     |     |
| Rebel Ambush  |      |      | 240 | 300 |
| Demo Trap     |  600 |  400 |   8 |   5 |
| Angry Mob     |  800 | 1000 |     |     |
| Technical     |  500 |  600 |     |     |
| Bomb Truck    | 1200 | 1100 |  15 |  12 |
| Scud Launcher | 1200 | 1000 |     |     |
| Radar Van     |  550 |  500 |     |     |
| Combat Cycle  |  550 |  450 |     |     |

### Demo GLA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Rebel Ambush        |     |      | 240 | 300   |
| Demolitions Ability |     |      |  30 |  45   |
| Demo Trap           | 200 |  300 |     |       |
| Angry Mob           | 800 | 1000 |     |       |
| Toxin Tractor       | 750 |  700 |     |       |
| Technical           | 600 |  550 |     |       |
| Bomb Truck          |     |      |  15 |  10   |
| Combat Cycle        | 500 | 600  |   5 |   6.5 |

### Stealth GLA

| ___________ Object ___________ | Old price ($) | New price ($) | Old time (s) | New time (s) |
|--------------------------------|--------------:|--------------:|-------------:|-------------:|
| Saboteur     |      |      | 15 | 10 |
| Bomb Truck   | 1200 | 1100 | 15 | 12 |
| Combat Cycle |  550 |  450 |    |    |
