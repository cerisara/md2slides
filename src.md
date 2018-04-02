..TITLE1 Deep generative networks
..TITLE3 Christophe Cerisara

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

..IMG60 ffvin.png

- Feedforward models are not robust to insertions/deletions: "Le vin peut aussi être fait à partir de"

---

..TITLE4 AutoEncoder : generating self

..IMG50 ae.png

g() = generator

---

..TITLE4 Recurrent Neural Network Language Model (RNNLM)

..IMG50 rnnlm.png

- Memory-vector stores important words step by step
- Fewer parameters to train

---

..TITLE4 Greedy Generation

- Generate the next word
- slide the input window and add the generated word at the end
- Iterate

--

- Not globally optimal (past decisions can not be changed)

---

..TITLE4 Viterbi: global optimum

..IMG60 viterbi.jpg

$$\max_{\phi} \prod_t P(w_t|w_{t-d},\cdots,w_t)$$

---

..TITLE4 Intermediate algorithms

- Beam search: Keep N best hypothesis at each step
- A star: Estimate the score until the end, at each step

--

In practice: Greedy works well with RNN !

---

..TITLE4 Character-LSTM

- Andrej Karpathy https://karpathy.github.io/2015/05/21/rnn-effectiveness/
- Train on Shakespeare (4.4MB) 3 jours (GPU), 1 mois (CPU)

..QUOTE
PANDARUS:
Alas, I think he shall be come approached and the day
When little srain would be attain'd into being never fed,
And who is but a chain and subjects of his death,
I should not sleep.

Second Senator:
They are away this miseries, produced upon my soul,
Breaking and strongly should be buried, when I perish
The earth and thoughts of many states.
..QUOTE

---

..TITLE4 seq2seq: generating sequences

..IMG50 seq2seq.png

De facto standard for translation, summarization...

---

..TITLE4 Variational Auto-Encoder: variability in generation

..IMG40 ae.png

Z is a latent variable:
$$Z \sim N(\mu,\sigma)$$

---

..TITLE4 Variational Auto-Encoder: variability in generation

..COL ENCODER
- Transforms input into a Gaussian
- Before generation, we sample a point from this Gaussian

..COL DECODER
- Standard: generates from a point
- Must have high capacity to map a Gaussian into any possible distribution
..ENDCOL

---

..TITLE4 Variational Auto-Encoder: Differentiable ?

..IMG70 vae.png

---

..TITLE4 Generative Adversarial Networks

..IMG80 gan.jpg

