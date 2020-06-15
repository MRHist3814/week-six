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

* Unfortunately, Voyant didn't want to cooperate with the data set I was using. I think there was too much data, or too many URLS, and it constantly crashed, with no error messages to help rectify the situation.

* Sadly I abandoned my plans for Lucy Copland's diary and went to work on Carl Hunnius' diary instead.

WGET

* It made most sense for me to start with WGET for this diary. I modified the python code from Week 2 to work with my chosen website and images. Surprisingly, it worked first time.

* I followed it with the standard wget command and successfully downloaded all 87 images of the diary.
