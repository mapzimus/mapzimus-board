"""Read headers from key CSV files for deeper idea extraction."""
import csv, sys, os, glob
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

files = [
    r"D:\raw_data\fbi\estimated_crimes_1979_2024.csv",
    r"D:\raw_data\fbi\territories_1995_2024.csv",
    r"D:\raw_data\fbi\lee_1960_2024.csv",
    r"D:\raw_data\fivethirtyeight\bad-drivers.csv",
    r"D:\raw_data\fivethirtyeight\hate_crimes.csv",
    r"D:\raw_data\fivethirtyeight\drinks.csv",
    r"D:\raw_data\fivethirtyeight\drug-use-by-age.csv",
    r"D:\raw_data\fivethirtyeight\recent-grads.csv",
    r"D:\raw_data\fivethirtyeight\biopics.csv",
    r"D:\raw_data\fivethirtyeight\airline-safety.csv",
    r"D:\raw_data\Sage_Data\Arrests by Race from the Arrests Database.csv",
    r"D:\raw_data\Sage_Data\Real Personal Income and Regional Price Parities from the Regional Personal Income and Employment Database.csv",
    r"D:\raw_data\Sage_Data\Total Vehicles Registered from the All Motor Vehicles  (Private + Public; Registered Vehicles) Database (1).csv",
    r"D:\raw_data\Sage_Data\Marijuana Use in the Past Month from the National Survey on Drug Use and Health (NSDUH), 2015-2019 [Archive] Database.csv",
    r"D:\raw_data\Sage_Data\Assessment by All Students from the National Assessment of Educational Progress (NAEP) Database.csv",
    r"D:\raw_data\worldcup\matches_1930_2022.csv",
    r"D:\raw_data\worldcup\fifa_ranking_2022-10-06.csv",
    r"D:\raw_data\Our World In Data\political-regime\political-regime.csv",
    r"D:\raw_data\Our World In Data\population\population.csv",
    r"D:\raw_data\Our World In Data\prison-population-rate\prison-population-rate.csv",
    r"D:\raw_data\Our World In Data\time-spent-with-relationships-by-age-us\time-spent-with-relationships-by-age-us.csv",
    r"D:\raw_data\Public_School_Characteristics_2022-23.csv",
    r"D:\raw_data\EconData\USCompanies.csv",
    r"D:\raw_data\Kaggle\archive (21)\global_prosperity_regions_politics.csv",
    r"D:\raw_data\Kaggle\archive (13)\asia_macro_economic_dataset.csv",
    r"D:\raw_data\Kaggle\FBRESULTS26\results.csv",
    r"D:\raw_data\fivethirtyeight\candy-data.csv",
    r"D:\raw_data\fivethirtyeight\divorce.csv",
    r"D:\raw_data\fivethirtyeight\women-stem.csv",
    r"D:\raw_data\fivethirtyeight\US_births_1994-2003_CDC_NCHS.csv",
    r"D:\raw_data\fivethirtyeight\fivethirtyeight_election_deniers.csv",
]

for fp in files:
    if not os.path.exists(fp):
        print(f"MISSING: {fp}")
        continue
    try:
        with open(fp, encoding='utf-8', errors='replace') as f:
            reader = csv.reader(f)
            header = next(reader)
            row1 = next(reader, None)
        name = os.path.basename(fp)
        print(f"\n{name} ({len(header)} cols)")
        print(f"  Headers: {header[:15]}")
        if row1:
            print(f"  Row1:    {row1[:15]}")
    except Exception as e:
        print(f"ERROR: {fp}: {e}")
