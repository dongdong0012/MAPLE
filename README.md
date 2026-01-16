# Multiscale Positive-Unlabeled Detection of AI-Generated Texts

<p align="left">
<a href="https://arxiv.org/abs/2305.18149" alt="arXiv">
    <img src="https://img.shields.io/badge/arXiv-2305.18149-b31b1b.svg?style=flat" /></a>
<a href="https://arxiv.org/pdf/2305.18149" alt="arXiv">
    <img src="https://img.shields.io/badge/Paper-PDF-b31b1b.svg?style=flat" /></a>
<a href="https://huggingface.co/spaces/yuchuantian/AIGC_text_detector" alt="Hugging Face Models">
    <img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-blue" /></a>
<a href="https://modelscope.cn/studios/YuchuanTian/AIGC_text_detector" alt="ModelScope Studio">
    <img src="https://img.shields.io/badge/ModelScope-Studio-blue" /></a>
<a href="https://github.com/YuchuanTian/AIGC_text_detector/blob/main/imgs/QR.jpg"><img src="https://img.shields.io/badge/微信-二维码加群-green?logo=wechat&amp"></a>
</p>  

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

## Training

The script for training is ```train.py```.

#### RoBERTa on HC3-English

Commands for seed=0,1,2:

```shell
CUDA_VISIBLE_DEVICES=0 python train.py --batch-size 32 --max-sequence-length 512 --train-data-file unfilter_full/en_train.csv --val-data-file unfilter_full/en_test.csv --model-name roberta-base --local-data data --lamb 0.4 --prior 0.2 --pu_type dual_softmax_dyn_dtrun --len_thres 55 --aug_min_length 1 --max-epochs 1 --weight-decay 0 --mode original_single --aug_mode sentence_deletion-0.25 --clean 1 --val_file1 unfilter_sent/en_test.csv --quick_val 1 --learning-rate 5e-05 --seed 0

CUDA_VISIBLE_DEVICES=0 python train.py --batch-size 32 --max-sequence-length 512 --train-data-file unfilter_full/en_train.csv --val-data-file unfilter_full/en_test.csv --model-name roberta-base --local-data data --lamb 0.4 --prior 0.2 --pu_type dual_softmax_dyn_dtrun --len_thres 55 --aug_min_length 1 --max-epochs 1 --weight-decay 0 --mode original_single --aug_mode sentence_deletion-0.25 --clean 1 --val_file1 unfilter_sent/en_test.csv --quick_val 1 --learning-rate 5e-05 --seed 1

CUDA_VISIBLE_DEVICES=0 python train.py --batch-size 32 --max-sequence-length 512 --train-data-file unfilter_full/en_train.csv --val-data-file unfilter_full/en_test.csv --model-name roberta-base --local-data data --lamb 0.4 --prior 0.2 --pu_type dual_softmax_dyn_dtrun --len_thres 55 --aug_min_length 1 --max-epochs 1 --weight-decay 0 --mode original_single --aug_mode sentence_deletion-0.25 --clean 1 --val_file1 unfilter_sent/en_test.csv --quick_val 1 --learning-rate 5e-05 --seed 2

```

#### BERT on HC3-English

Commands for seed=0,1,2:

```shell
CUDA_VISIBLE_DEVICES=0 python train.py --batch-size 32 --max-sequence-length 512 --train-data-file unfilter_full/en_train.csv --val-data-file unfilter_full/en_test.csv --model-name bert-base-cased --local-data data --lamb 0.5 --prior 0.3 --pu_type dual_softmax_dyn_dtrun --len_thres 60 --aug_min_length 1 --max-epochs 1 --weight-decay 0 --mode original_single --aug_mode sentence_deletion-0.25 --clean 1 --val_file1 unfilter_sent/en_test.csv --quick_val 1 --learning-rate 5e-05 --seed 0


CUDA_VISIBLE_DEVICES=0 python train.py --batch-size 32 --max-sequence-length 512 --train-data-file unfilter_full/en_train.csv --val-data-file unfilter_full/en_test.csv --model-name bert-base-cased --local-data data --lamb 0.5 --prior 0.3 --pu_type dual_softmax_dyn_dtrun --len_thres 60 --aug_min_length 1 --max-epochs 1 --weight-decay 0 --mode original_single --aug_mode sentence_deletion-0.25 --clean 1 --val_file1 unfilter_sent/en_test.csv --quick_val 1 --learning-rate 5e-05 --seed 1


CUDA_VISIBLE_DEVICES=0 python train.py --batch-size 32 --max-sequence-length 512 --train-data-file unfilter_full/en_train.csv --val-data-file unfilter_full/en_test.csv --model-name bert-base-cased --local-data data --lamb 0.5 --prior 0.3 --pu_type dual_softmax_dyn_dtrun --len_thres 60 --aug_min_length 1 --max-epochs 1 --weight-decay 0 --mode original_single --aug_mode sentence_deletion-0.25 --clean 1 --val_file1 unfilter_sent/en_test.csv --quick_val 1 --learning-rate 5e-05 --seed 2

```


## Acknowledgement

Our code refers to the following GitHub repo:

https://github.com/openai/gpt-2-output-dataset

We sincerely thank their authors for open-sourcing.


