from args import parser
import os
from prepare_data import create_data

if __name__ == '__main__':

    args = parser.parse_args()

    mode = args.mode

    # Initialize all modes to zero
    data_mode = False
    training_mode = False
    prediction_mode = False

    # Update with the mode the user is asking
    if mode == 'prediction':
        prediction_mode = True
    elif mode == 'training':
        training_mode = True
    elif mode == 'data_creation':
        data_mode = True

    if data_mode:
        #Example: python main.py --mode='data_creation'

        #folder containing noises
        noise_dir = args.noise_dir
        #folder containing clean voices
        voice_dir = args.voice_dir
        #path to save time series
        path_save_time_serie = args.path_save_time_serie
        #path to save sounds
        path_save_sound = args.path_save_sound
        #path to save spectrograms
        path_save_spectrogram = args.path_save_spectrogram
        # Sample rate to read audio
        sample_rate = args.sample_rate
        # Minimum duration of audio files to consider
        min_duration = args.min_duration
        #Frame length for training data
        frame_length = args.frame_length
        # hop length for clean voice files
        hop_length_frame = args.hop_length_frame
        # hop length for noise files
        hop_length_frame_noise = args.hop_length_frame_noise
        # How much frame to create for training
        nb_samples = args.nb_samples
        #nb of points for fft(for spectrogram computation)
        n_fft = args.n_fft
        #hop length for fft
        hop_length_fft = args.hop_length_fft

        create_data(noise_dir, voice_dir, path_save_time_serie, path_save_sound, path_save_spectrogram, sample_rate,
        min_duration, frame_length, hop_length_frame, hop_length_frame_noise, nb_samples, n_fft, hop_length_fft)
