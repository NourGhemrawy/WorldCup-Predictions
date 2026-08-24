"""
Team name standardization between the match-results dataset (martj42) and the
FIFA ranking dataset (cnc8 / fifa.com scrape).

This mapping was built by DIFFING the two real datasets (not guessed):
    matches_teams - ranking_teams  ->  140 unmatched names
Most of the 140 are genuinely non-FIFA entities (Catalonia, Isle of Man,
Kurdistan, historic/defunct teams, etc.) that will never appear in a FIFA
ranking and are correctly left unmapped. The subset below are real naming
convention differences between the two sources, confirmed by inspecting the
ranking dataset's actual country_full values.

Keys = name as it appears in results.csv (martj42)
Values = name as it appears in fifa_ranking.csv (cnc8 / fifa.com)
"""

MATCHES_TO_RANKING = {
    "United States": "USA",
    "South Korea": "Korea Republic",
    "North Korea": "Korea DPR",
    "Ivory Coast": "Côte d'Ivoire",
    "Cape Verde": "Cabo Verde",
    "China": "China PR",
    "DR Congo": "Congo DR",
    "Iran": "IR Iran",
    "Brunei": "Brunei Darussalam",
    "Eswatini": "Swaziland",  # ranking source predates the 2018 rename in this mirror
    "Saint Kitts and Nevis": "St. Kitts and Nevis",
    "Saint Lucia": "St. Lucia",
    "Saint Vincent and the Grenadines": "St. Vincent / Grenadines",
}


def standardize_team_name(name: str) -> str:
    """Map a team name from the match-results dataset to the ranking dataset's convention."""
    return MATCHES_TO_RANKING.get(name, name)
