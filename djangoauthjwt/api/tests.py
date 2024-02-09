from django.test import TestCase

# Create your tests here.
def string_to_set(text):
    return set(text.replace(","," ").strip().split())

# print(string_to_set("hello"))
# print(string_to_set("hello, buddy"))
# print(string_to_set("hello, I'm, here"))


def NoiseReduction(audio_file, noise_file = None):
    pass
    # rate, data = wavfile.read(audio_file)
    
    # if noise_file is not None:
    #     rate_noise, noise_data = wavfile.read(noise_file)
    #     # performming noise reduction with noise file
    #     reduced_noise = nr.reduce_noise(y=data, sr=rate, y_noise=noise_data)
    # else:
    #     # performming noise reduction without noise file
    #     reduced_noise = nr.reduce_noise(y=data, sr=rate)
    
    # wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)

NoiseReduction("d:/Downloads/file_example_MP3_700KB.wav")