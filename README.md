# AI-lab

Här finns instruktion för att komma igång med labbar på Öjn!

## Gör detta innan avfärd

### Ladda hem detta repo
Ladda hem detta repo med några färdiga script. 

### Installera python 3 (version 3)

**Windows**

Mitt tips är att installera anaconda när du vill köra python på windows. 
Den pakteringen av python fungerade mycket smidagare för mig när jag körde windows.
Försöker hjälpa till med lite instruktioner för båda.

Jag har här antagit att man godkänner att anaconda lägger python3.exe i din path.
Dock verkar anaconda rekommendera motsatsen men jag har tidigare sagt ja på den frågan.

https://docs.anaconda.com/anaconda/install/windows/


**Linux**

Brukar vara installerat från start (beroende på dist).
Om inte så får ni använda pakethanteraren för er dist.


**Mac**

Har ingen erfarenhet av att köra Mac tyvärr. Kanske vettigt att Googla from bara.

Som t.ex. den här: https://docs.python-guide.org/starting/install3/osx/


### Verifiera installationen
Verifiera att du har python installerat:

1. Gå till en terminal

2. `python3 --version` -> Python 3.9.*

3. `pip3 --version` eller `conda --version` -> pip *.*.*

### Installera python paket
Precis som med alla moderna språk har även python en pakethantater som heter pip.

Jag har preppat en fil med paket vi behöver.

**Mac och Linux**

`pip3 install -r requirements.txt --upgrade`

**Windows**

`conda install --file requirements.txt`


### Kör pre-lab.py
För att ladda hem så mycket som möjligt innan vi är på Öjn.

`python3 lab-setup.py`


## Labbar

https://scikit-learn.org/stable/auto_examples/index.html

