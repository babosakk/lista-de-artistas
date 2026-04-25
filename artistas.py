
favorite_artists = []


while True:
    artist = input("Qual é seu artista favorito? (ou 'sair' para parar): ")
    
    if artist.lower() == 'sair':
        break
    
    if artist.strip():
        favorite_artists.append(artist.lower())  


artist_count = {}

for artist in favorite_artists:
    if artist in artist_count:
        artist_count[artist] += 1
    else:
        artist_count[artist] = 1

print("\n--- Contagem de Artistas ---")
for artist, count in artist_count.items():
    print(f"{artist}: {count} vez(es)")


if artist_count:
    most_favorite = max(artist_count, key=artist_count.get)
    print(f"\nArtista mais votado: {most_favorite} ({artist_count[most_favorite]} votos)")
