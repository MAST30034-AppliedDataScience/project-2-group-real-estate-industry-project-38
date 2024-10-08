# Project Title: **Generic Real Estate Consulting Project - Group 38**

## Research Goal

Our research goal is to determine the appropriate level of rent for an online real estate company, identify the most important internal and external features in predicting rental prices, find the top 10 suburbs with the highest predicted growth rate, and identify the most liveable and affordable suburbs.

## Timeline

The dataset used for this research covers the time range from 1999 - 2027.

## Overview

This project involves downloading, preprocessing, merging, and analyzing various datasets, including open street maps, crime data, domain data, and rental data. The project focuses on analysing growth trends and influencial factors, creating a liveability index by property and region, and performing geo-spatial visualizations for rental data.

## Features
- Data scraping and downloading from various sources (OSM, crime, domain, transport, rent)
- Preprocessing and merging datasets to create distance-based features
- Analysis of important factors, growth conclusions, liveability index, and scoring system
- Geo-spatial visualizations for historical and current rent data

## Installation

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies using the following command:
   ```bash
   pip install -r requirements.txt


## Project Structure and Running the Project

The project is organized into three main phases: downloading & scraping data, preprocessing & merging data, and modeling & analyzing data. To run the pipeline, please visit the `notebooks` and `models` directory and run the files follow this sequence of steps:

1. **Downloading and Scraping Data**
   - **notebooks**:
     - `01_1_osm_data_downloading.ipynb`: Download Open Street Map data.
     - `01_2_crime_data_scraping.ipynb`: Scrape crime data.
     - `01_3_domain_data_scraping.ipynb`: Scrape domain data.
     - `01_4_region_boundary_downloading.ipynb`: Download region boundary data.
     - `01_5_region_data_crawling.ipynb`: Crawl region data.
     - `01_6_transport_data_downloading.ipynb`: Download transport data.
     - `01_7_rent_data_downloading.ipynb`: Download rental data.

2. **Preprocessing and Merging Data**
   - **notebooks**:
     - `02_1_range_data_preprocessing.ipynb`: Preprocess region range data.
     - `02_2_domain_data_merging_and_preprocessing.ipynb`: Merge and preprocess domain data.
     - `02_3_osm_data_preprocessing.ipynb`: Preprocess OSM data.
     - `02_4_osm&transport_data_merging.ipynb`: Merge OSM and transport data.
     - `02_5_domain_data_preprocessing_with_distance_features.ipynb`: Add distance-based features to domain data.
     - `02_6_region&rent_data_merging.ipynb`: Merge region and rental data.

3. **Modelling and Analyzing Data**
   - **notebooks**:
     - `03_Q1_important_factors.ipynb`: Analyze important factors for rental price.

   - **models**:
     - `03_Q2_regression_model.ipynb`: Run regression models to predict future rental data.
     - `03_Q2_time_series_model.ipynb`: Run time series models to predict future trends.

   - **notebooks**:
     - `03_Q2_growth_conclusion.ipynb`: Draw conclusions on growth trends.
     - `03_Q3_liveability_index_by_property.ipynb`: Calculate liveability index by property.
     - `03_Q3_scoring_system_by_region.ipynb`: Implement a scoring system by region.
     - `03_visual_1_historial_rent.ipynb`: Visualize historical rent data.
     - `03_visual_2_rent_geo_spatial.ipynb`: Perform geo-spatial visualizations for rent data.


## Special Notices

1. **Data Download Date**: All datasets were downloaded as of **September 9th**.
2. **New Datasets**: Any new datasets that you download will be saved with the suffix `_new` in the file names.
3. **Long Running Notebooks**: Running the notebooks `01_5_region_data_crawling.ipynb` and `01_3_domain_data_scraping.ipynb` will take a significant amount of time (approximately **1-2 hours**).
4. **New Datasets Impact**: If you choose to use the newly downloaded datasets for analysis, note that the results will differ from what is presented in the summary notebook and presentation.

### Notes for Specific Notebooks:

- In **`02_2_domain_data_merging_and_preprocessing.ipynb`**:
  - Under the "Read files" section:
    > **Important!** If you change to `domain_data_new`, all subsequent domain-related data will be processed using the latest domain data. **Results will differ!** This impacts the model results, so be cautious! You can change to new dataset by modifying the following codes in this notebook:
    ```python
    # Base directory for JSON files
    landing_base_directory = "../../data/landing/domain_data"
    # If you want to use the newest domain data, uncomment the line below and comment the above line.
    # landing_base_directory = "../../data/landing/domain_data_new"
    ```

  - Under the "Files" section:
    > **Important!** If you change to `all_region_key_data_new`, all subsequent region data merged with domain data will use the latest ABS region data. **Results will differ!** This may affect the accuracy of models in Q1 but not Q2 or Q3.  You can change to new dataset by modifying the following codes in this notebook:

- In **`03_Q1_important_factors.ipynb`**:
  - Under the "Read files" section:
    > **Important!** If you change to `new`, all subsequent property-related data will be processed using the latest distance-calculated data. **Results will differ!**  This may affect the accuracy of models in Q1 but not Q2 or Q3. You can change to new dataset by modifying the following codes in this notebook:
    ```python
    rental_model_data = pd.read_csv("../../data/curated/properties_data4.csv")
    # If you want to use the newest output rental data, uncomment the line below and comment the above line.
    # rental_model_data = pd.read_csv("../../data/curated/properties_data4_new.csv")
    ```

5. **API Key Quota**: Another important issue to note is that the API key may exceed its quota if overused. If this happened, try to run the code after 24 hours, or switch to an alternative key by uncommenting the following line and commenting out the current key in  `02_5_domain_data_preprocessing_with_distance_features.ipynb`.

    ```python
    # client = Client(key='5b3ce3597851110001cf6248a027188a61b345eeb77761e0521405ba')
    client = Client(key='5b3ce3597851110001cf62489c86d07e1db14afbbf6fece88bfe6afe')
    ```

### Data Update Impact:
- **Region Data**: The region data downloaded from the website has been updated, as has the OSM data. Due to these updates, the results will slightly differ from what is presented in the summary notebook and presentation.

