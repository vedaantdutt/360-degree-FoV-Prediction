# 360 degree FOV prediction

This project is aimed at predicting and analyzing features in a 360-degree field of view (FOV). It leverages advanced preprocessing pipelines, machine learning models, and visualization techniques tailored for equirectangular projections (ERP)

 
Download the project folder, unzip it and "cd Final_year_ARIMA"

## Folder Descriptions
		
		|
		|__ Baseline/          --> Contains the implementions of the baseline algorithms that we tested PARIMA against
		|   |
		|   |__ Clust/
		|   |__ NABA/
		|   |__ PanoSalnet/
		|
		|__ creme/              --> Modifications to the source code of the library to enable multi-frames prediction.
		|
		|__ PanoSaliency/       --> Contains the procedures to convert the head movement data from quaternion format to coordinates in an equirectangular frame
		|
		|__ Prediction/         --> Contains the implementation of PARIMA. Check 'Prediction/README.md` for further details.
		|
		|__ Preprocess/         --> Codes to perform the one-time video preprocessing at the Server end. Check `PreProcess/README.md` for further details
		|   |
		|   |__ FrameProjector/
		|   |__ YOLO/
		|   |__ ObjectTrack/
		|
	

## Requirements
Use `python3` for all the codes. Install the dependencies by running `pip install -r requirements.txt`.  

After the installation, source code for the package `creme` needs to be modified. For the same, go to the location(say, `PATH`) in your system where `creme` library source codes are stored(eg, `~/anaconda3/lib/python3.7/site-packages/creme/`) and copy the file `creme/linear_model/pa.py` into the appropriate subdirectory in `PATH`. 


## Datasets
In our experiments, we have particularly used two popular datasets containing several 360-degree videos of different categories along with head tracking log. 

1. Xavier Corbillon, Francesca De Simone, and Gwendal Simon. [2017]. *360-Degree Video Head Movement Dataset.* In Proceedings of the ACM MMSys 2017. 
It includes five videos freely viewed by 59 users each with each video watched for 70 seconds. The dataset is available from [http://dash.ipv6.enstb.fr/headMovements/](http://dash.ipv6.enstb.fr/headMovements/)
2. Chenglei Wu, Zhihao Tan, Zhi Wang, and Shiqiang Yang. [2017]. *A Dataset for Exploring User Behaviors in VR Spherical Video Streaming.* In Proceedings of the ACM MMSys 2017. 
It has nine popular videos watched by 48 users with an average view duration of 164 seconds. The dataset is available from [https://wuchlei-thu.github.io/](https://wuchlei-thu.github.io/)


## Pipeline
	Install Requirements and modify the source code (creme/)
					|
	Preprocess the video and store the object trajectories (Preprocess/)
					|
	Transform the quaternion format of the Head Movement Logs to Equirectangular form (PanoSaliency/)
					|
	Run PARIMA and calculate the QoE of a video (Prediction/)

**Note:** Follow the `README.md` inside each of the directories to get the details of the execution.
 

## License
The project is licensed under the terms of MIT License.
