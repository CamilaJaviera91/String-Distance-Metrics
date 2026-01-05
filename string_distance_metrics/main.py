from cleaning import normalize_string
from distances import levenshtein_distance
from generators import generate_realistic_typo

original = "El camión pasó rápido"

typo_text = generate_realistic_typo(original)
print(f"Original: '{original}' | Con Typo: '{typo_text}'")

dist_raw = levenshtein_distance(original, typo_text)
print(f"Distancia bruta: {dist_raw}")

norm_orig = normalize_string(original)
norm_typo = normalize_string(typo_text)
dist_clean = levenshtein_distance(norm_orig, norm_typo)

print(f"Comparación Normalizada: '{norm_orig}' vs '{norm_typo}'")
print(f"Distancia post-limpieza: {dist_clean}")