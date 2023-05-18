import pyaudio
import numpy as np

A2 = 110
As2 = 116.54
B2 = 123.47
G3 = 196
Gs3 = 207.65
A3 = 220
As3 = 233.08
B3 = 246.94
C4 = 261.63
Cs4 = 277.18
D4 = 293.66
Ds4 = 311.13
E4 = 329.63
F4 = 349.23
Fs4 = 369.99
G4 = 392.00
Gs4 = 415.30
A4 = 440.00
As4 = 466.16
B4 = 493.88
C5 = 523.25
Cs5 = 554.37
D5 = 587.33
Ds5 = 622.25
E5 = 659.25
F5 = 698.46
Fs5 = 739.99
G5 = 783.99
Gs5 = 830.61
A5 = 880.00
As5 = 932.33
B5 = 987.77
C6 = 1046.50


def play(cancion, bpm):
    # Configuración de parámetros de audio
    formato = pyaudio.paFloat32
    canales = 1
    tasa_muestreo = 44100

    # Crear una instancia de PyAudio
    p = pyaudio.PyAudio()

    # Abrir el stream de audio
    stream = p.open(format=formato,
                    channels=canales,
                    rate=tasa_muestreo,
                    output=True)

    # Reproducir los datos de audio

    for frecuencia, duracion in cancion:
        duracion = (60 / bpm) * duracion
        # Generar los datos de audio para la frecuencia especificada
        tiempo = np.linspace(0, duracion, int(duracion * tasa_muestreo),
                             endpoint=False)
        datos = np.sin(2 * np.pi * frecuencia * tiempo).astype(np.float32)
        stream.write(datos.tobytes())

    # Detener y cerrar el stream de audio
    stream.stop_stream()
    stream.close()

    # Terminar PyAudio
    p.terminate()


starfox = [
    (D4, .5),
    (D5, .5),
    (C5, 2),
    (B4, 0.3),
    (A4, 0.33),
    (B4, 0.34),

    (0, .33),
    (G4, .67),
    (G5, 3),

    (Fs5, .33),
    (Fs5, .33),
    (Fs5, .34),
    (G5, 0.5),
    (G4, 0.5),
]

mario = [
    (G3, .33),
    (C4, .33),
    (E4, .34),
    (G4, .33),
    (C5, .33),
    (E5, .34),
    (G5, 1),
    (E5, .5),
    (37, .5),

    (Gs3, .33),
    (C4, .33),
    (Ds4, .34),
    (Gs4, .33),
    (C5, .33),
    (Ds5, .34),
    (Gs5, 1),
    (Ds5, .5),
    (37, .5),

    (As3, .33),
    (D4, .33),
    (F4, .34),
    (As4, .33),
    (D5, .33),
    (F5, .34),
    (As5, 1),
    (As5, .33),
    (As5, .33),
    (As5, .34),

    (C6, 4),
]

kirby = [
    (C5, .5),
    (D5, .5),
    (E5, .5),
    (Fs5, .5),
    (E5, .5),
    (Fs5, .5),

    (G5, 1),
    (D5, .5),
    (B4, 1),
    (D5, .5),

    (C5, 1),
    (B4, .5),
    (A4, 1),
    (B4, .5),

    (G4, 1.5),
    (G5, 1.5),
]

finalfantasy = [
    (C5, 1/3),
    (C5, 1/3),
    (C5, 1/3),
    (C5, 1),
    (A4, 1),
    (B4, 1),

    (C5, 1/3),
    (0, 1/3),
    (B4, 1/3),
    (C5, 3),
]

fallguys = [
    (Fs4, 1/2),
    (E4, 1/2),
    (Fs4, 1/2),
    (A4, 1),
    (Fs4, 1/2),
    (A4, 1/2),
    (B4, 1),
    (A4, 1/2),
    (B4, 1/2),
    (E5, 1),
    (Cs5, 1/2),
    (E5, 1),
    (Fs5, 1),
]

play(starfox, 150)
play(mario, 150)
play(kirby, 260)
play(finalfantasy, 120)
play(fallguys, 170)
