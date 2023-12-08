## Aalto University project. Authors: Oskari Mattila, Annina Toimela, Mikaela Rautavirta, Eemeli Kokkonen
# Kohinanpoisto

This project utilizes a noise reduction algorithm called RNNoise, from https://gitlab.xiph.org/xiph/rnnoise. The main component of the project is a demo  Jupyter notebook script found at ./Demo/demo.ipynb. The purpose of the demo is to provide a stress testing functionality to measure the performance of RNNoise noise reduction capabilites. The demo provides the means to record and audio clip, add noise to it with desired SNR and run it through the RNNoise algorithm.

Additional tools used: 
https://github.com/google/visqol for measuring the similarity between clean and denoised audio data
https://github.com/Sato-Kunihiko/audio-SNR to easily mix noise to the clean audio files