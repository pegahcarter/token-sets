# Split a dataframe into rolling windows


def split_df(df, overlap, window_len):

    _split_df = []

    for x in range(0, len(df) - window_len + 1, overlap - 1):
        _split_df.append(df[x:x+window_len])

    return _split_df
