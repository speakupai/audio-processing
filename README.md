# audio-processing

This repository contains python scripts to manipulate and convert raw audio to low resolution, noisy and messy compression\EQ.

The boilerplate scripts are inspired by: https://github.com/vbelz/Speech-enhancement

it's been modified to work with latest version of Librosa

To run it locally:

0. Prerequisites:
   - install librosa
   - Some clean voice data and noise data have been provided in the train folder. You can add your own voice and noise data.  Voice and noise data must have the same sample rate. (The provided data has 8000 sample rate)

1. Open args.py in scripts folder and update default paths to your local paths for the following arguments: 

- parser.**add_argument**('--noise_dir', default='local_path/train/noise', type=**str**) 
- parser.**add_argument**('--voice_dir', default='local_path/train/clean_voice', type=**str**) 
- parser.**add_argument**('--path_save_spectrogram', default='local_path/train/spectrogram/', type=**str**)
- parser.**add_argument**('--path_save_time_serie', default='local_path/train/time_series/', type=**str**)
- parser.**add_argument**('--path_save_sound', default='local_path/train/sound/', type=**str**) 
- Change --nb_samples default value to specify your desired output length. 50 frames = 50 seconds.
- Change --sample_rate default value to input voice/noise data sample rate

2. Run python main.py --mode='data_creation'

   

3. You will see generated audio, spectrogram, and time_series in tne train folder

