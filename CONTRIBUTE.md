# How to contribute

To participate in conversations, simply create a GitHub Account and start posting. Please act professional.

To make content contributions, aka Pull Requests, either fork this repository and clone that fork, or just clone this repository if you are invited as a Contributor of the TheSuperHackers.

Various Generals modding documents are [located here](https://github.com/TheSuperHackers/GeneralsDocuments).

Various Generals modding tools are [located here](https://github.com/TheSuperHackers/GeneralsTools).


## Change Documentation

Every change for the game needs to be documented.

All documentation ideally is written in the present tense, and not the past.

Good:

> Fixes particle effect of USA Missile Defender

Bad:

> Fixed particle effect of USA Missile Defender

When a text refers to a faction unit, structure, upgrade or similar, then the unit should be worded without any abbrevations and should be prefixed with the faction name. Valid faction names are USA, China, GLA, Boss, Civilian. Subfaction names can be appended too, for example GLA Stealth.

Good:

> Fixes particle effect of USA Missile Defender

Bad:

> Fixes particle effect of MD


### 1. Script Changes and Documentation

Changes ideally are concise and only touch the lines of code that the change relates to. Any changes made to INI and STR files need to be accompanied by a comment where the change is made. The comment can be inlined or put at the begin of the changed block. It must be clear from the change description what has changed.

The expected comment format is

```
; Patch104p @keyword author DD/MM/YYYY A meaningful description for this change.
```

The `Patch104p` word and `@keyword` are mandatory. `author` and date can be omitted when preferred.

| Keyword          | Use-case                                                    |
|------------------|-------------------------------------------------------------|
| @bugfix          | Fixing a bug                                                |
| @feature         | Adding something new                                        |
| @fix             | Fixing something, but is not a user facing bug              |
| @performance     | Improving performance                                       |
| @refactor        | Moving or rewriting code, but does not change the behaviour |
| @tweak           | Changing some values or settings                            |

Block comment sample

```
  ; Patch104p @bugfix commy2 13/09/2021 Add missing upgrade icon for Anthrax Beta.

  UpgradeCameo1 = Upgrade_GLAAnthraxBeta
  UpgradeCameo2 = Upgrade_GLACamoNetting
```

Inline comment sample

```
ConditionState = REALLYDAMAGED RUBBLE NIGHT SNOW
  ...
  HideSubObject = Flag01A Flag01B Flag01C ; Patch104p @bugfix commy2 02/10/2022 Hides USA flag.
End
```


### 2. Pull Request Documentation

The title of a new Pull Request is prefixed either with `Fix:` for being a fix or `Change:` for being a change that is not a fix, followed by a descriptive title of the change. Documentation and maintenance pulls are exempt of this rule.

The text body begins with links to related issue report(s) and/or pull request(s) if applicable.

To write a link, use the following format:

```
* Relates to #555
* Follow up for #666
* Fixes #222
```

Some keywords are interpreted by GitHub. Read about it [here](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue).

The text body continues with a description of the change in appropriate detail. This serves to educate reviewers and visitors to get a good understanding of the change without the need to study and understand the associated changed files. If the change is controversial or affects gameplay in a considerable way, then a rationale text needs to be appended. The rationale explains why the given change makes sense.


### 3. Change Log Documentation

Every change needs to be accompanied with a yaml definition file for the change log generation. It is supposed to contain concise information for the change. The yaml file needs to be created inside the `Patch104pZH/Design/Changes` folder or the appropriate subfolder. There is a template.yaml file that can be used as a base. The name of the file begins with the number of the Pull Request and a few words to summarize the essence of the change, seperated by underscores. It is possible that a new change extends an existing yaml file instead of creating a new one. In that case a txt file with the same naming rules can be created to refer to the actual yaml file.
