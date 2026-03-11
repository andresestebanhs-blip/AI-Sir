import numpy as np
import unicodedata
import string

def tokenize(sentence):
    """
    Divide la oración en palabras, eliminando puntuación simple.
    """
    # Normalizar (quitar tildes para facilitar coincidencia)
    s = ''.join(c for c in unicodedata.normalize('NFD', sentence)
                if unicodedata.category(c) != 'Mn')
    
    # Reemplazar puntuación por espacios
    for char in string.punctuation:
        s = s.replace(char, ' ')
        
    return s.lower().split()

def bag_of_words(tokenized_sentence, words):
    """
    Crea el array de bag of words (1 si la palabra está, 0 si no)
    """
    # Usamos set para búsqueda rápida
    sentence_words = set(tokenized_sentence)
    bag = np.zeros(len(words), dtype=np.float32)
    
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1
            
    return bag
