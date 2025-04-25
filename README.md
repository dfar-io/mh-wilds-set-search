# mh-wilds-set-search

***I've archived this project in favor of just using the WikiDB Set Searcher (https://mhwilds.wiki-db.com/sim/?hl=en)***

Set Searcher for Monster Hunter Wilds

## Getting Started

1. Create codespace.
2. Change `search_criteria` in source code to match desired armor skills and rank.
3. Run `python3 main.py`

## Creating JSON files

1. Add raw data into `raw_armor.json`.
2. Run `python3 generate_armor_data.py`

## Basic Search Algorithm

*Just notes on how the general algorithm works*

1. Filter eligible armor pieces by search criteria
	1. Rank
	2. Armor pieces with desired skills
	3. Armor pieces with eligible slots (later)
2. Get combinations for all eligible pieces
	1. Get combined skills
	2. See if it matches search criteria
		1. How do we handle slots? Slots are just flexible armor skills
		2. Might use some math to determine if slots can overcome missing skills from combination
3. Sort by defense descending
