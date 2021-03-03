# ECE143-Final-Project
This is repository for ECE143 Group 7's Final Project. 



## Notebook for the test cases

Our notebook for the functional/validation tests is in the file `./test.ipynb`.





## Spatial Temporal analysis

Please enter the `HEATMAP_processing` directory and change the path as instructed below. (If you utilize our default repository setting, you should be able to directly run the command.)

Change the `world_path` to the path to store all the geopandas data and change `sentiment_score_file_path` to the path storing the csv file with preprocessed sentiment scores and change `vaccine_file_path` to the path storing the original csv file which will be utilized to extract country information.

After changing the path, please run the flollowing command

```bash
python heat_map.py
```

If you want to generate the gif, please utilize the `generateGif()` function. And you would get the `gif` as below:

![img](./HEATMAP_processing/1.gif)

