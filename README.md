- Install requirement packages:

```shell
pip install -r requirements.txt
```

- Download datasets to directory: ```./data``` 

- Download nltk package punct (This step could be done by ```nltk``` api: ```nltk.download('punkt')```)

- Download pretrained models (This step could be automatically done by ```transformers```)


Before running, the directory should contain the following files:

```
├── data
│   ├── unfilter_full
│   │   ├── en_test.csv
│   │   └── en_train.csv
│   └── unfilter_sent
│       ├── en_test.csv
│       └── en_train.csv
├── README.md
├── corpus_cleaning_kit.py
├── dataset.py
├── multiscale_kit.py
├── option.py
├── pu_loss_mod.py
├── prior_kit.py
├── requirements.txt
├── train.py
└── utils.py
```

Our code refers to the following GitHub repo:

https://github.com/openai/gpt-2-output-dataset

We sincerely thank their authors for open-sourcing.




