# MAPLE: Multidimensional Adaptive-Prior PU Learning for Detecting AI-Generated Text

## Description
This repository provides the official implementation of **MAPLE**, a multidimensional adaptive-prior positive–unlabeled (PU) learning framework for detecting AI-generated text.  
MAPLE is designed to address the challenges of **short-text sparsity**, **distribution uncertainty**, and **cross-lingual generalization**, which commonly degrade the performance of existing detection methods.

The framework integrates multiple lightweight textual priors (e.g., length, perplexity, punctuation, and semantic cues) into a unified PU risk formulation, enabling robust and interpretable detection under real-world constraints.

---

## Dataset Information
This implementation relies on **publicly available datasets**.  
Due to GitHub file size limitations, datasets are **not included** in this repository and should be downloaded separately.

- **HC3 dataset**  
  https://huggingface.co/datasets/Hello-SimpleAI/HC3

- **TweepFake dataset**  
  https://github.com/tizfa/tweepfake_deepfake_text_detection

After downloading, please organize the datasets under the `./data` directory as follows:
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


**## Requirements**
The code is implemented in **Python 3.8+**.  
Please install the required dependencies using:

```bash
pip install -r requirements.txt
In addition, the following resources are required:

NLTK punkt tokenizer

import nltk
nltk.download('punkt')


Pre-trained language models, which will be automatically downloaded via the transformers library when running the code.

Usage Instructions
1. Prepare datasets

Download and place the datasets under the ./data directory following the structure described above.

2. Train the model

Run the training script:

python train.py


You may modify hyperparameters and settings in option.py as needed.

Methodology

MAPLE reformulates AI-generated text detection as a PU learning problem, where only positive (AI-generated) and unlabeled samples are available.
A multidimensional adaptive-prior mechanism is introduced to dynamically estimate class priors based on multiple textual attributes, which are then integrated into a constrained risk objective.
This design improves robustness against short-text uncertainty and enhances cross-domain and cross-lingual generalization.

Citation

If you use this code in your research, please cite the corresponding paper:
@article{Hu2025MAPLE,
  title={MAPLE: Multidimensional Adaptive-Prior PU Learning for Detecting AI-Generated Text},
  author={Hu, Jiaen and others},
  journal={Computing},
  year={2025}
}




