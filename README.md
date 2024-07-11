experiment using UML to keep LLM on the rails while it generates a text based rpg of progressevly increasing complexity.

to run app:
1. python3 app.py
2. launch web browswer with url: 127.0.0.1:5000
3. get your dragon on!

to recreate llm session:

> = Prompts for Claude 3.5 Sonnet

>Let’s co-design a text adventure game in PlantUML and python 3.​​​​​​​​​​​​​​​​

>This will be a high fantasy dragon riding adventure with a faction based mission system​​​​​​​​​​​​​​​​.


Here's a brief explanation of each class:

1. Game: The main class that manages the game state.
2. Player: Represents the player character.
3. Dragon: The player's dragon companion.
4. Location: Represents different locations in the game world.
5. Faction: Different factions the player can interact with.
6. Mission: Quests or tasks provided by factions.
7. Item: Objects the player can collect and use.

> Let’s enumerate the core use cases for the game​​​​​​​​​​​​​​​​ formatted as “actor takes an action on target object” when possible​​​​​​​​​​​​​​​​.
 Here's the revised list of use cases formatted as "actor takes an action on target object" where applicable, with asterisks (*) marking the ones included in our use case UML diagram:

1. * Player creates character
2. * Player bonds with dragon
3. * Player explores world
4. * Player rides dragon
5. * Player engages in combat with enemies
6. * Player manages inventory
7. * Player crafts items
8. * Player brews potions
9. * Player interacts with factions
10. * Player completes quests
11. * Player develops skills
12. * Player trades with NPCs/economy system
13. * Player experiences weather effects
14. * Player interacts with ecosystem
15. * Player shapes story through choices
16. * Player builds and modifies world
17. * Player manages in-game time
18. * Player customizes dragon
19. * Player negotiates between factions
20. * Player discovers new recipes
21. * Player experiences dynamic events
22. * Player engages in dialogue with NPCs
23. * Player saves/loads game
24. Player joins or creates guild
25. Player participates in guild quests
26. Player contributes to guild activities
27. Player levels up guild
28. Guild leader manages guild membership
29. Player engages in PvP combat
30. Player participates in dragon tournaments
31. Player builds and customizes housing
32. Player discovers and empowers magical artifacts
33. Player participates in seasonal festivals
34. Player breeds dragons
35. Player manipulates weather (high-level ability)
36. Player travels to alternate dimensions
37. Player rebuilds and develops world areas
38. Player forms alliances with NPCs
39. Player manages personal reputation
40. Player solves environmental puzzles

This formatted list provides a clearer picture of the actor (usually the player) and the action they're taking, along with the target of that action when applicable. The asterisks indicate which use cases are currently represented in our UML use case diagram.​​​​​​​​​​​​​​​​

> Let’s create a PlantUML sequence diagram for each use case above.

> next update our uml class diagram to include each use case above.

> let's also update our uml use case diagram to include all of these new sequences.

This use case diagram represents all the main functionalities (use cases) that we've identified for our dragon-riding adventure game. It shows the Player as the primary actor interacting with all these use cases.

The diagram also includes some relationships between use cases:

- "Ride Dragon" extends "Explore World"
- "Craft Items" and "Brew Potions" include "Manage Inventory"
- "Complete Quests" includes "Interact with Factions"
- "Trade and Economy" includes "Manage Inventory"
- "Shape the Story" includes both "Complete Quests" and "Engage in Dialogue"
- "Build and Modify World" extends "Explore World"
- "Negotiate Between Factions" extends "Interact with Factions"
- "Discover New Recipes" extends both "Craft Items" and "Brew Potions"
- "Experience Dynamic Events" extends "Shape the Story"

These relationships help to show how different aspects of the game are interconnected and how some use cases build upon or extend others.​​​​​​​​​​​​​​​​

Use Case Diagram
<img src="https://www.plantuml.com/plantuml/svg/VPFHRfim58RlUOgZthV3K22PggXhaasHrgfhEktw34w9DMD7nYHbqzvz9e4AUqcleY__P-lujxcj3MhJL28Gz6B0AD2yt1WekARSS2K3p8tIy2Ym9Hq4tRyeIq5miT1OAWbFlE2oX4_5ZgHfDC4NhEW2_WG0JKqvrbQTQq93CD-WnjoGlW2iuVkSZPqx9GlOSxE1uyQz4usTvUjMA4tmGsbHz48y5kmmvAw_TjRB4ai2Bc6kgfzeUYSPE_SeEsSbk_CetVPEwfu7RLahGrNTnvbp54rxU5HTVKC-6UShQQWhudZSpvYFpUdOj6Dk1Hc2RmtLPb1OE7OMj2EXjh3-nOLuKvnkdpKM16WBNkPAggeTBBzTqfnaRWicD1lIWnQVdzvkMBUrRM9mdSBN6zmIsArWFUgI9KvR3HV5ORXxLV2NrhbTbfwucsTUqP1dJbrDRLJ5VtjlW3djFr2f34T3S4TcJoJz6s1JfrvUvsf76Xve3q-KyoqDOXIUgM_HIgnu3ilk3RtPxFHJN70Kgcneq2AdGDpHXwyAYyDdDIXny3S8ZfyaN5xEkfbTZ5oCNRnsCN4nTJ5pSUBYr1iZz9Xv77aSUtpjSU9nwd7cySHZRxuezDZlBV8u3WBR5rnTTHJ3HxYveLT3igXdCvjaVP8U4YvpqHHqZ2Rd8nRssVH45hspBkap5huJHj69C3rx13PrXXb7qJ1dTZwQ_1-nOSh4osxjRrE9Vm00">

Class Diagram
<img src="https://www.plantuml.com/plantuml/svg/bLLDJzmm4Btlhx0uXLAazfeJ2AeAYLOK3ZqWPCqwizbH7Jkr9mlRgl-zoNZNcn2Gu89tvit7c-TnE8iCWRl6Bk8lSYq4Q9In4ECvSw1bntXblBkZFwW-BHQ2gA_GeFgxKEgqjR35KAeREGVFem-sAjNFuHZiFdb5TQakoN1ldsXDZbZhudYmh8TAfv3a43RQuQEkeS4YrTUk_rsgoE6ZCci8OBXt2XVnvb8fAHM23OxCDdY3CUe-bRmhqf6I3zngP4dHaO6ns2F_zdEdAMNoaqnfC5uY9PnmWxPKvAGyFhKO29t1x5eZM5vdim47sUXheAj7Q8LFZ85ucptzWTPIFQb9ReEEVUZ3hYdo_HLZyp2H_YroijSL6Iv6ygo2RvAp0eRaFyvtdrMIgq_hORs1GUYOWk-bvVNE-I3hqOM0ZlK-KWXCoBwJZNJFP7Ap5owjmcW2jPEknZk7Xh7IcRgeADHV5V5vfUD3_q7yD_RUWEtIBRwfZtWEEI9J5x6OFiaHbSi0jNUtL96hlu63Uh_AZUySwqhWQVhGKzpbBbkwL1JVcPAVtyfIlMPDhksuaByoo9xyhgA69LdYhNvSayK-QTjJBdREKfsd7wFHBdop19uCDQX7mAYDO3EIwB3fQtqPZWd55Az3Fs5L218mUhl9bSPz0wpukPm13RMutvjRiMHrp12jYR6PiKavfKhHMMLmRF7bZC5PodgD-FpeC4vbW0sGXQL5_Nl0zgmaK4Y1OTgyYjReC03lyC9un_Z4uzTyxhOFwVhQAWVgNimwO8mpsWANYUXuDmcihpkysqR6vjaDLZjmLiorfbJVRox6zvUZjLbxCbYau_0kvP_NqUSZTNegHoesSyjtPEQTlw5vvdWPv-XqPUQuAFCQE9Lf8Hmp_k4eV-qMQQWnT3KaBCxGLLrZ_mC0">
