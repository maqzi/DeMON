# DeMON: Deception Miner for Opinions & Notions

DeMON mines 1.6 million reviews for 63000 electronics collected from Amazon and made openly available  by Dr. McAuley [1][2], visualizes and tries to mine them for fake and genuine reviews. This goes ahead hand in hand with estimating how reliable amazon reviews can be before making buying decisions. DeMON
using a python and R duo, successfully pinpoints 49 products which are highly likely to be fake
ones using a combination of Cosine Similarity [3][4] for reviews and studying anomalies in posting
times per product.

## Instructions

1. Get complete data set in MongoDB using bash. (not necessary, but helps to visualize the dataset)
	- Run MongoServer
	- In a new terminal run DeMON>load+preprocess+process>bashimportJSONtoMONGO.sh using: ./bashimportJSONtoMONGO.sh
	- This will import all Cellphones and Electronics and metadata Dataset to the mongodb named: Individ_DeMON
	
2. Set up Python Environment
	- It is better to use and IDE such as Pycharm, but the terminal will work fine as well.
	- Make sure you have python installed.
	- Make sure you have all python packages installed mentioned in requirements.txt

** For the first run, uncomment the "import nltk" and "nltk.download()" lines in main.py and follow the instructions to download the PunkT Corpus. **
   
3. In Pycharm, (NOTE: CAN TAKE UPTO 9 HOURS)
	- Load DeMON>Main.py
	- Make sure you're using Python 2.7 Interpretter
	- Run script. It wil do all analysis and create both Cosine Similarity Analysis and Date Time Analysis Result CSVs in DeMON>output
	- Review Dumps and Time Dumps will also be created in DeMON>output

4. Create a Metadata CSV from JSON
	- Metadata was imported into mongo in step 1. 
	- In a new terminal run DeMON>load+preprocess+process>bashexportMONGOtoCSV.sh using: ./bashexportMONGOtoCSV.sh
	- Use metaDATA.csv created in DeMON>output in Step 5.

5. Open CSVs in R for visualizations.
	- Run GenerateFakenessPDFReport.R to generate an html table of all products identified using fake reviewing services in DeMON>output. To convert html to pdf, use: 'wkhtmltopdf tableFinalFake.html tableReport.pdf' in the terminal after navigating to DeMON>output
	- Run PlotBarChartOf46FakeProdsByCategories.R to see a plot chart of the identified products' categories in DeMON>output.
	- Run FakeReviewsWordCloud.R to generate a wordcloud of terms often used in fake reviews in DeMON>output.
	- Run PlotResultsForAllCS&TD.R to generate a Cosine Distance vs. Time Score plot for all products from Step 3 in DeMON>output.

** I have included my dataset from Step 1 in the DeMON>data folder. **

## Addendum

* The Python script is configured to save data in a mongo db running on localhost on port 27017. For different settings, configure it accordingly.
* The Bash scripts are configured to work in my paths. Reconfigure paths accordingly.
* The complete report for DeMON is present in Report.pdf.

## References
	[1] Image-based recommendations on styles and substitutes. J. McAuley, C. Targett, J. Shi, A. van den Hengel. SIGIR, 2015.
	[2] Inferring networks of substitutable and complementary products. J. McAuley, R. Pandey, J. Leskovec. Knowledge Discovery and Data Mining, 2015.
	[3] Introduction to Information Retrieval. Manning, Christopher. 2009.
	[4] Sentiment Analysis and Opinion Mining. Liu, Bing. 2012. 
