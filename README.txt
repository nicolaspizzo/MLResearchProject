README

Thank you for downloading this distribution of a Machine Learning Project.  This is a compiled folder of all files and scripts needed to run our first ML attempts.


Folders: 
	1) Basic_Model_Implementations
		a) LDA_Pandas.ipynb
		The first ML script we tried.  This utilises pandas as the primary machine learning algorithm, and implements an LDA model.

		b) Preprocessing.ipynb
		Preprocessing notebook goes through punctuation removal, tokenization, stemming using both Porter and Snowball (they seem to work about the same) and also removes words which are 1 or 2 characters long.
	
	2) Data_Sets
		a) Questions.csv
		This is the CSV file that comes from Questions.txt.  This is used as the dataset for all of our scripts.

		b) questions_james_email.csv
		This file was provided by James Davenport as part of the repository http://web-cat.org/questionbank/
		
		c) Raw_Format
		Contains all raw data files
			i) Questions.txt
			This file is the original questions document we needed to use for our scripts. This has been obtained for the Data structure and Algorithms course at the University of Bath, 
			taught and tutored by two of the collaborators

		d) Extra_Data_Sets
		Contains extra data sets that were found/used in our research project to understand the above mentioned models.
			i) papers.csv 
			This file was obtained from https://www.kaggle.com/benhamner/nips-papers?select=papers.csv
	
	3) Misc_Programs
	Miscellaneous programs created and used in our research project.
		a) textToCSV.py
		The script used to convert the txt documenet to csv.

