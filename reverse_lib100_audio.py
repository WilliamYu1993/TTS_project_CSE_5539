

# reverse the audio
#import ffmpeg
import pdb
import torch
import torchaudio
#from pydub import AudioSegment
#from pydub.playback import play
"""
def reverse_and_export_flac_audio(path: str) -> None:
  song = AudioSegment.from_file(path, "flac")
  pdb.set_trace()
  backwards = song.reverse()
  backwards.export(path, format="flac")
"""

def reverse_and_export_flac_audio(path: str) -> None:
    audio, sr = torchaudio.load(path)
    reverse_audio = torch.flip(audio,(0,1))
    #pdb.set_trace()
    rpath = path.replace("train-clean-100", "train-clean-100_reversed") 
    torchaudio.save(rpath, reverse_audio, sr)

import os, fnmatch
for root, dirnames, filenames in os.walk("/fs/scratch/PAS2400/TTS_baseline_cpy/training_data/LibriSpeech/train-clean-100/"):
    for filename in filenames:
        if filename.endswith("flac"):
            #pdb.set_trace()
            isExist = os.path.exists(root.replace("train-clean-100", "train-clean-100_reversed"))
            if not isExist:
                os.makedirs(root.replace("train-clean-100", "train-clean-100_reversed"))
            reverse_and_export_flac_audio(os.path.join(root, filename))
