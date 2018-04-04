..TITLE2 Basic text generative models
<br>
<br>
<br>
..TITLE4 Christophe Cerisara

---

..TITLE4 Neural networks as discriminative classifiers

..COL Principle
- Take as input observations X
- Output labels Y
- Final softmax converts into probabilities:
$$P(Y|X;\theta)$$

..COL Applications
- Text classification: sentiment, language...
- Phrase/Word classification: NER, dialog acts...
- Other: entailnment, Q&A...
..ENDCOL

---

..TITLE4 Neural networks as generative models

..COL Principle
- Take as input noise, class Y or some continuous representation
- Output words/image X
$$P(X|Y;\theta)$$

..COL Applications
- Translation, summarization...
- Chat bot...
..ENDCOL

---

..TITLE4 Generating word by word

$$P(W) = \prod_t P(w_{t}|w_{t-d,\cdots,t-1})$$

..COL Advantages
- Unsupervised ? No manual annotations apart from writing the text.
- Language Model: decomposes the difficult problem of evaluating whether a sentence belongs to the language or not

..COL Extensions
- Can also be used with characters (char-LM)
- Generate the 4 words around (Skipgram W2V)
..ENDCOL

---

..TITLE4 Feedforward to generate next word

..IMG60 https://www.researchgate.net/profile/Hamid_Hosseini12/publication/287209604/figure/fig4/AS:307959503572995@1450434675333/Multilayer-perceptron-neural-network-model-1-5-8-7-7-4.png

- Feedforward models are not robust to insertions/deletions: "Le vin peut aussi être fait à partir de"

---

#### Use standard markdown for headers

..COL

- Easy to add image on the right
- Don't forget to type Crtl+ or Ctrl- to increase/decrease font size

..COL
..IMG50 https://www.nobelprize.org/nobel_prizes/physics/laureates/1921/einstein.jpg
..ENDCOL

