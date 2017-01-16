# DeMON

DeMON studies patterns of 1.6 million reviews for 63000 electronics provided by Amazon,
visualizes and tries to mine them for fake and genuine reviews. This goes ahead hand in hand
with estimating how reliable amazon reviews can be before making buying decisions. DeMON
using a python and R duo, successfully pinpoints 49 products which are highly likely to be fake
ones using a combination of Cosine Similarity for reviews and studying anomalies in posting
times per product.

Instructions to run the complete program:

1. Get complete data set in MongoDB using bash. (not necessary, but helps to visualize the dataset)
	a. Run MongoServer
	b. In a new terminal run DeMON>load+preprocess+process>bashimportJSONtoMONGO.sh using: ./bashimportJSONtoMONGO.sh
	c. This will import all Cellphones and Electronics and metadata Dataset to the mongodb named: Individ_DeMON
	
2. Set up Python Environment
	a. It is better to use and IDE such as Pycharm, but the terminal will work fine as well.
	b. Make sure you have python installed.
	c. Make sure you have all python packages installed mentioned in requirements.txt

** For the first run, make sure lines:
	import nltk
	nltk.download()
   are uncommented. Once run, look for the PunkT Corpus and download that aswell.
	
3. In Pycharm, (NOTE: CAN TAKE UPTO 9 HOURS)
	a. Load DeMON>Main.py
	b. Make sure you're using Python 2.7 Interpretter
	c. Run script. It wil do all analysis and create both Cosine Similarity Analysis and Date Time Analysis Result CSVs in DeMON>output
	d. Review Dumps and Time Dumps will also be created in DeMON>output

3. In Terminal (NOTE: CAN TAKE UPTO 9 HOURS)
	a. Navigate to folder scripts
	b. Run main using: python main
	c. CSA and DTA Result CSVs will be created in DeMON>output
	d. Review Dumps and Time Dumps will also be created in DeMON>output

4. Create a Metadata CSV from JSON
	a. Metadata was imported into mongo in step 1. 
	b. In a new terminal run DeMON>load+preprocess+process>bashexportMONGOtoCSV.sh using: ./bashexportMONGOtoCSV.sh
	c. Use metaDATA.csv created in DeMON>output in Step 5.

5. Open CSVs in R for visualizations.
	a. Run GenerateFakenessPDFReport.R to generate an html table of all products identified using fake reviewing services in DeMON>output. To convert html to pdf, use: 'wkhtmltopdf tableFinalFake.html tableReport.pdf' in the terminal after navigating to DeMON>output
	b. Run PlotBarChartOf46FakeProdsByCategories.R to see a plot chart of the identified products' categories in DeMON>output.
	c. Run FakeReviewsWordCloud.R to generate a wordcloud of terms often used in fake reviews in DeMON>output.
	d. Run PlotResultsForAllCS&TD.R to generate a Cosine Distance vs. Time Score plot for all products from Step 3 in DeMON>output.

* I have included my dataset from Step 1 in the DeMON>data folder.

Addendum:
* The Python script is configured to save data in a mongo db running on localhost on port 27017. For different settings, configure it accordingly.
* The Bash scripts are configured to work in my paths. Reconfigure paths accordingly.
