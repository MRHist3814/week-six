READINGS

* I appreciated seeing such an easy to read and understandable, yet more professional, sort of note taking that we've been attempting in this class.

* There are still limitations, but it was interesting for me to compare my understanding of the reading to earlier weeks.

  * I could pretty easily track what Moravec was describing, the steps she was taking. I understood the general direction of her workflow clearer than I had with previous readings.
  
WORK

* After some browsing, I settled on the diaries of Lucy Copland. The writing-while-travelling aspect appealed to me, as I could already envision a map or at least a timeline as a visual presentation of data at the end of all of this.

* Now I have to try to decide which methods to use to explore the data.

  * My initial thoughts are the methods in Week 4. What does Lucy talk about on her travels? Do her topics change as time progresses? Does early travel excitement turn into homesickness?
  
* I started with Voyant, because I knew that was the direction I was heading. I collated a list of the urls to the diary entries and put it into Voyant.

  * A lot of the text on each page is irrelevant to my work, so I had to figure out a way to get rid of it.
  
  * I used regular expressions to focus only on the text after '1819' and before 'observations.' This cut out writings from the website team and focused solely on the diary text.
  
  * I also added some stopwords to get rid of repetitive and unecessary info (day names, month names, 1819, etc.).

* Unfortunately, Voyant didn't want to cooperate with the data set I was using. I think there was too much data, or too many URLs, and it constantly crashed, with no error messages to help rectify the situation.

* Sadly I abandoned my plans for Lucy Copland's diary and went to work on a different diary instead.

  * In browsing the list, I noticed the diaries of 'Thomas Ryan.' That's my brother's name, so I decided to give them a shot.

WGET

* It made most sense for me to start with WGET for this diary. I modified the python code from Week 2 to work with my chosen website and images. Surprisingly, it worked first time.

* I followed it with the standard wget command and successfully downloaded all 74 images of the diary. (Screenshot 1).

  * However, due to the URLs of the images (they all ended in 'default.png'), it named them all as 'default' rather than their file names, and then added numerical values on the end. The numerical values made it so that the png extension was obscured, so I manually had to rename and correct them all to the normal .png format.
  
* With all of the files fixed and named after each page of the dairy, I could move on to extracting information from them.

OCR

* The next logical step seemed to be OCRing the images to extract the text from them. The diaries are very legible, so at this stage I hope/think it'll be straightforward.

* Initially the code to use in RStudio didn't work, but I realized it was set to search for .jpg files and I'm using .png files. Eventually I got all of the images into .txt documents, though it took an hour and a half for RStudio to complete the process. (Screenshot 2).

VOYANT

* I put the OCR text documents into Voyant and generated an end product that can be found at the following URL:

  * https://voyant-tools.org/?corpus=dba48a189ff6b3319b6eb394dabefd9f

* The wordcloud and terms list had some rather apparent words with significant usage. (Screenshot 3).

  * Verbs were highly prevalent. Came, went, got, took, etc. This makes sense to me, it's a personal diary recounting actions taken each day.
  
  * There is also signficant emphasis on acquaintances and relatives. Susie, Walter, Rol, etc.
  
  * I noticed a trend of words that decrease in usage over time: drawing, band, carriage, room, riding, nixon, clarinet. (Screenshot 4).
    
  * Given that the trends are produced chronologically, I made the assumption that would be tied to the weather. Indoor activities (like drawing and clarinet) during the colder months, and therefore less mentions in later months of warmer weather.

ANTCONC

* I decided to take the next step in AntConc, to see the broader context of the words. I loaded up the OCR text files and searched some of the words on my shortlist.

* 'Band' apparently referred to the band room where the clarinet was practiced. (Screenshot 5). This is also the same source as the term 'room.'

* You can see 'Nixon' in some of those sentences, so I decided to search that term next. As it happens, Mr. Nixon was teaching Thomas how to play clarinet. (Screenshot 6).

* 'Carriage' and 'riding' were less definitive. However, looking up the terms 'snow' I did find information that perhaps links. 'Snow' is mentioned in tandem with riding a horse, and not having to walk through it. Perhaps there is merit in riding more frequently in the colder/snowier months? (Screenshot 7).

* The term 'car' was an interesting one. Though not explicitly tied to weather, you can see that the mentions occur mostly in later documents, correlating to the return to colder months. Did streetcar usage go up as colder weather came about? (Screenshot 8).

* I think this could be an interesting avenue to explore for research. How does the weather impact the writing of Thomas Ryan's diary? What patterns of word usage develop over the change in seasons?
