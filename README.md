![rave_logo](docs/rave.png)

# RAVE: Realtime Audio Variational autoEncoder

Official implementation of _RAVE: A variational autoencoder for fast and high-quality neural audio synthesis_ ([article link](https://arxiv.org/abs/2111.05011)) by Antoine Caillon and Philippe Esling.

If you use RAVE as a part of a music performance or installation, be sure to cite either this repository or the article ! 

## Installation

RAVE needs `python 3.9`. Install the dependencies using

```bash
pip install -r requirements.txt
```

## Preprocessing

RAVE comes with two command line utilities, `resample` and `duration`. `resample` allows to pre-process (silence removal, loudness normalization) and augment (compression) an entire directory of audio files (.mp3, .aiff, .opus, .wav, .aac). `duration` prints out the total duration of a .wav folder.

## Training

Both RAVE and the prior model are available in this repo. For most users we recommand to use the `cli_helper.py` script, since it will generate a set of instructions allowing the training and export of both RAVE and the prior model on a specific dataset.

```bash
python cli_helper.py
```

However, if you want to customize even more your training, you can use the provided `train_{rave, prior}.py` and `export_{rave, prior}.py` scripts manually.

## Reconstructing audio

Once trained, you can reconstruct an entire folder containing wav files using

```bash
python reconstruct.py --ckpt /path/to/checkpoint --wav-folder /path/to/wav/folder
```

You can also export RAVE to a `torchscript` file using `export_rave.py` and use the `encode` and `decode` methods on tensors.

## Realtime usage

**AVAILABLE ON APRIL 4th**

RAVE and the prior model can be used in realtime on live audio streams, allowing creative interactions with both models. **Realtime export is not available yet**, but models trained today **will** be compatible with the realtime interfaces.

### [nn~](https://github.com/acids-ircam/nn_tilde)

RAVE is compatible with the **nn~** max/msp and PureData external.

![max_msp_screenshot](docs/maxmsp_screenshot.png)

An audio example of the prior sampling patch is available in the `docs/` folder.
