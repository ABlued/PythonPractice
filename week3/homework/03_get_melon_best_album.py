genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # result = []
    # genreDict = {}
    # for i in range(len(genre_array)):
    #     if genre_array[i] in genreDict : genreDict[genre_array[i]] += play_array[i]
    #     else : genreDict[genre_array[i]] = play_array[i]
    #
    # reverse_genreDict= dict(map(reversed, genreDict.items()))
    # while len(genreDict) != 0 :
    #     maxPlays = max(genreDict.values())
    #     maxGenre = reverse_genreDict[maxPlays]
    #     for j in range(0,2):
    #         maxIndex = 0
    #         maxPlays = 0
    #         for i in range(len(genres)):
    #             if genre_array[i] == maxGenre :
    #                 if maxPlays < play_array[i] :
    #                     maxIndex = i
    #                     maxPlays = play_array[i]
    #         result.append(maxIndex)
    #         play_array[maxIndex] = 0
    #     del genreDict[maxGenre]
    #
    # return result

    genre_total_play_dict = {}
    genre_index_play_array_dict = {}
    n = len(genre_array)
    for i in range (n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else :
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play])

    print(genre_index_play_array_dict)
    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda  item: item[1], reverse=True)
    print(sorted_genre_play_array)
    result = []
    for genre, _value in sorted_genre_play_array:
        index_play_array = genre_index_play_array_dict[genre]
        sorted_index_play_array = sorted(index_play_array, key=lambda item:item[1], reverse=True)

        for i in range(len(sorted_index_play_array)):
            if i > 1:
                break;
            result.append(sorted_index_play_array[i][0])

    return result
print(get_melon_best_album(genres, plays))  # ????????? [4, 1, 3, 0] ??? ?????? ?????????!