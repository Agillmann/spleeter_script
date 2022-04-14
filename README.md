# Spleeter Script

## About Spleeter by deezer

Spleeter is Deezer source separation library with pretrained models written in Python and uses Tensorflow. It makes it easy to train source separation model (assuming you have a dataset of isolated sources), and provides already trained state of the art model for performing various flavour of separation :

- Vocals (singing voice) / accompaniment separation (2 stems)
- Vocals / drums / bass / other separation (4 stems)
- Vocals / drums / bass / piano / other separation (5 stems)

2 stems and 4 stems models have high performances on the musdb dataset. Spleeter is also very fast as it can perform separation of audio files to 4 stems 100x faster than real-time when run on a GPU.

## Description

The goal of this repository is to spleet sound from a file or a directory

---

## Needed

- Python version: `3.8` [download](https://www.python.org/downloads/)
- Conda version: `4.12.0` [download](https://docs.conda.io/en/latest/miniconda.html)
- Spleeter version: `2.30.0` [repo](https://github.com/deezer/spleeter)

---

## Installation

- Download and install python : [download](https://www.python.org/downloads/)

- Download and install miniconda : [download](https://docs.conda.io/en/latest/miniconda.html)

- Create conda env

```bash
  conda create --name spleeter_script python=3.8 &
  conda activate spleeter_script
```

- Install deps

```bash
  conda install -c conda-forge ffmpeg libsndfile &
  pip install spleeter
```

---

## Running

- Show help

```bash
  python main.py -h
```

- Process a file

```bash
  python main.py -f /path/to/audio_example.mp3 -s 2 # -s for stems
```

- Process a directory

```bash
  python main.py -f /path/to/audio_folder -s 2 # -s for stems
```
