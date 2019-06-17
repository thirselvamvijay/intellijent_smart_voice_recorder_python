import os
import wave
import pyttsx3
from gtts import gTTS

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from voice_recorder.forms import AudioForm
from voice_recorder.models import Audio, UpdatedAudio
import time as t
# from  ReduceNoiseService import Red
from voice_recorder.services.DeleteFolderService import DeleteFolderService
from voice_recorder.services.FindEnergyOfTheVoice import FindEnergyOfTheVoice
from os import path
from pydub import AudioSegment
import glob

name = ""
dst = ""
sound = ""
updateddst = ""
updatedAudio = ""

engine = pyttsx3.init()


@csrf_exempt
def welcomeApi(request):
    text = """<h1>Welcome to voice recorder API.</h1>"""
    return HttpResponse(text)


@csrf_exempt
def uploadAudio(request):
    try:

        saved = False

        if request.method == "POST":
            # Get the posted form
            audioForm = AudioForm(request.POST, request.FILES)

            if audioForm.is_valid():
                global updateddst
                global updatedAudio

                audio = Audio()
                updatedAudio = UpdatedAudio()
                audio.audio = audioForm.cleaned_data["audio"]
                updatedAudio.updated_audio = audioForm.cleaned_data["audio"]
                global name
                name = str(audio.audio.name)
                name = name[:-4]
                global dst
                dst = 'upload/convertedAudio/' + name + '.wav'
                updateddst = 'upload/updated_audios/' + name + '.wav'
                print(name)
                print(dst)
                print(updateddst)

                global sound

                sound = AudioSegment.from_file(audio.audio) # converting audio files to wav file.
                sound.export(dst, format="wav") # saving wav files to converted audio folder
                updatedAudio.updated_audio = 'upload/updated_audios/' + name + '.wav'
                audio.audio.file = audio.audio.file
                print(name)
                print(audio.audio.name)
                print(audio.audio.name)
                # audio.save()
                saved = True
                t.sleep(3)

                print("energy: ", FindEnergyOfTheVoice.findEnergyOfTheVoice(dst))

                if FindEnergyOfTheVoice.findEnergyOfTheVoice(dst) > 97:  # services
                    sound.export(updateddst, format="wav")
                    updatedAudio.save()


                else:
                    print("no voice")

                # print(audio.audio.name)
                # ReduceNoiseService.reduce_noise(audio.audio.name)

                # AudioAnalysis.audio_analysis(audio.audio.name)

                return HttpResponse('successfully saved!')
        else:
            audioForm = AudioForm()

        status_code = 500
        message = "The request is not valid."
        explanation = "bad credentials"
        return JsonResponse({'message': message, 'explanation': explanation}, status=status_code)
    except ConnectionResetError:
        status_code = 417
        message = "connection reset..."
        explanation = "client connection lost"
        return JsonResponse({'message': message, 'explanation': explanation}, status=status_code)


# @csrf_exempt
# def start_audio(request):
#
#     if FindEnergyOfTheVoice.findEnergyOfTheVoice(dst) > 97:
#         sound.export(updateddst, format="wav")
#         updatedAudio.save()
#
#
#     else:
#         print("no voice")
#
#     return ""


@csrf_exempt
def stop_audio(request):
    global name
    print(glob.glob('upload/updated_audios/*.wav'))
    file_data = glob.glob('upload/updated_audios/*.wav')
    file_data.sort(key=os.path.getmtime)
    outfile = "upload/output_files/" + name + ".wav"

    with wave.open(outfile, 'wb') as wav_out:
        for wav_path in file_data:
            with wave.open(wav_path, 'rb') as wav_in:
                if not wav_out.getnframes():
                    wav_out.setparams(wav_in.getparams())
                wav_out.writeframes(wav_in.readframes(wav_in.getnframes()))
    DeleteFolderService.deleteFolder()  # delete updated audio files
    DeleteFolderService.deleteFolderConverted_audio()
    return HttpResponse('stopped audio')


@csrf_exempt
def start_audio_library(request):
    try:

        saved = False

        if request.method == "POST":
            # Get the posted form
            audioForm = AudioForm(request.POST, request.FILES)

            if audioForm.is_valid():
                global updateddst
                global updatedAudio
                audio = Audio()
                updatedAudio = UpdatedAudio()
                audio.audio = audioForm.cleaned_data["audio"]
                updatedAudio.updated_audio = audioForm.cleaned_data["audio"]
                global name
                name = str(audio.audio.name)
                name = name[:-4]
                global dst
                dst = 'upload/convertedAudio/' + name + '.wav'
                updateddst = 'upload/updated_audios/' + name + '.wav'
                print(name)
                print(dst)
                print(updateddst)

                global sound

                sound = AudioSegment.from_file(audio.audio)
                sound.export(dst, format="wav")
                updatedAudio.updated_audio = 'upload/updated_audios/' + name + '.wav'
                audio.audio.file = audio.audio.file
                print(name)
                print(audio.audio.name)
                print(audio.audio.name)
                # audio.save()
                saved = True
                t.sleep(3)

                print("energy: ", FindEnergyOfTheVoice.findEnergyOfTheVoice(dst))

                if FindEnergyOfTheVoice.findEnergyOfTheVoice(dst) > 95:
                    os.system("espeak 'please silent students do not disturb other students'")


                else:
                    print("no voice")

                # print(audio.audio.name)
                # ReduceNoiseService.reduce_noise(audio.audio.name)

                # AudioAnalysis.audio_analysis(audio.audio.name)

                return HttpResponse('successfully saved!')
        else:
            audioForm = AudioForm()

        status_code = 500
        message = "The request is not valid."
        explanation = "bad credentials"
        return JsonResponse({'message': message, 'explanation': explanation}, status=status_code)
    except ConnectionResetError:
        status_code = 417
        message = "connection reset..."
        explanation = "client connection lost"
        return JsonResponse({'message': message, 'explanation': explanation}, status=status_code)


@csrf_exempt
def stop_record_library(request):
    DeleteFolderService.deleteFolder()  # delete updated audios
    DeleteFolderService.deleteFolderConverted_audio()
    return HttpResponse('stopped audio')

# @csrf_exempt
# def library_service(request):
#     if FindEnergyOfTheVoice.findEnergyOfTheVoice(dst) > 94:
#         os.system("espeak 'please silent students do not disturb other students'")
#     else:
#         print("no voice")
#
#     return "success"
