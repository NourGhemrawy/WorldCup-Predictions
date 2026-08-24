# FIFA World Cup 2030 Prediction

End-to-end data science pipeline: historical data → cleaning → EDA → features → models →
match probabilities → tournament Monte Carlo simulation → World Cup 2030 champion probabilities.

**Status: Phase 1 of ~8 complete** (data collection + cleaning). See `data/DATA_SOURCES.md` for
full source documentation and `notebooks/` for the executed, reproducible pipeline so far.

## Structure
```
world-cup-2030-prediction/
├── data/
│   ├── raw/            # untouched downloads, + provenance log
│   ├── processed/       # cleaned datasets
│   └── external/        # for your Elo CSV upload
├── notebooks/            # numbered, run in order
├── src/                  # reusable modules (team name mapping, etc.)
├── models/                # (empty until phase 4)
├── visualizations/        # saved charts
└── data/DATA_SOURCES.md    # full dataset provenance & comparison
```

## Progress
- [x] **01_data_collection.ipynb** — downloads real match-results (49,520 matches, 1872–2026) and
      FIFA ranking (62,424 rows, 1992–2020) data from verified public sources
- [x] **02_data_cleaning.ipynb** — data understanding, duplicate/outlier checks, team-name
      standardization (13 confirmed mismatches fixed, 127 correctly left as non-FIFA entities),
      chronological sort, documented missing-value policy → `data/processed/*_clean.csv`
- [ ] 03_eda.ipynb
- [ ] 04_feature_engineering.ipynb (needs your Elo CSV in `data/external/`)
- [ ] 05_model_training.ipynb
- [ ] 06_model_evaluation.ipynb
- [ ] 07_explainability.ipynb
- [ ] 08_world_cup_2030_simulation.ipynb

## Next step
Drop your Elo ratings CSV into `data/external/elo_ratings.csv`, and we'll move on to EDA (03) —
happy to keep going right after.
