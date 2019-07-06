# SpeechToTextApplication

In order to run the python file, after git cloning it, then install the following python libraries:

pip install SpeechRecognition
pip install PyAudio
-------------------------------------------------------------------------------------------------------------------------
If there is an error in installing the python library pyAudio in windows, then try the following:
"

The answer by Agian is already great and I just want to explain it in an step by step format for novice like myself:

    find your Python version by python --version mine is 3.7.3 for example
    the easiest way to check either you have 64 or 32 Python just open it in the terminal:


    find the appropriate .whl file from here, for example mine is PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl, and download it.
    go to the folder where it is downloaded for example cd C:\Users\foobar\Downloads
    install the .whl file with pip for example in my case:

pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl

"
[source: https://stackoverflow.com/questions/52283840/i-cant-install-pyaudio-on-my-python-how-to-do-it]

------------------------------------------------------------------------------------------------------------------------------
