# Datasets
# Generic Real Estate Consulting Project - Group 38
- The external data used within this project were all researched using data captured before 9 September as a baseline

- Domain Data
	- domain_data
		- sources：Domain Real Estate
		`data/landing/domain_data/apart.json`: This json file holds the internal feature of a property with an apartment type crawled from the domain website.
		`data/landing/domain_data/house.json`: This json file holds the internal feature of a property with an house type crawled from the domain website.
		`data/landing/domain_data/town_house.json`: This json file holds the internal feature of a property with an Town-House type crawled from the domain website.
	- domain_data_new
		What is saved in this folder is the same as what is saved in domain_data, but maybe the data will be different. This is because this folder holds the newly run data when the code is re-run. If you want to use the new dataset for your research, in the code we added comment, you can use the comment code

- Open Street Map Data
	- sources: Open Street Map
	`data/landing/osm_data`: This folder contains 8 csv files which contain information about different schools, parks and other public facilities.
- Other Data
	- source：data.gov.au
		- `data/landing/other_data/CG_POSTCODE_2021_SA2_2021.xlsx`: This xlsx holds the post code for the SA2region.
		- `data/landing/other_data/CG_SA2_2021_LGA_2022.csv`: This csv file holds the name of the SA2 region corresponding to the LGA region
		- `data/landing/Other_data/Quarterly_median_rent_March_2024.xlsx`: This xlsx file holds median rental prices by LGA region for each quarter from 1999-2024.
	- sources: Crime Statistics Agency 
		— `data/landing/other_data/Data_Tables_LGA_Criminal_Incidents_Year_Ending_March_2024`: This xlsx file holds the number of Criminal by LGA region.
	- sources: Public Transport a collection of PTV datasets
		- `data/landing/other_data/stops_datavic`:This folder stores information on all stations in Victoria.
- Region Data
	- source: Australian Bureau of Statistics
	- Long Run data
		`data/landing/region_data/long_run_data`: This folder contains 16 csv files containing the values of the 16 main features in different regions for different years.
	- Key Statistics
		`data/landing/region_data/KeyStatistics/all_region_key_data.csv`: This csv file holds the latest data for the different features of each region.
		`data/landing/region_data/KeyStatistics/all_region_key_data_new.csv`: This file saves the same content that all_region_key_data.csv saves, but the data is slightly different because this grabs the data while testing the code.
	- LGA dataset 
		- `data/landing/region_data/sa2_dataset/sa2_unzip`: This folder contains geographic information about Statistical Area 2 in Australia.
	- SA2 dataset
		- `data/landing/region_data/sa2_dataset/LGA_unzip`：This folder contains geographic information about Local Government Area in Australia.