import pandas as pd

def content_type(title):
    if isinstance(title, str):
        if "THIS STATION WILL CONTINUE AFTER THIS BREAK" in title:
            return "break"
        if "Listen.FM - Listen.FM" in title or "Kickin' Kountry@Listen.FM" in title:
            return "station_id"
        return "song"

def clean_data():
    input_file = "radio_tracks.csv"
    output_file = "radio_tracks_clean.csv"

    df = pd.read_csv(
        input_file,
        header=None,
        names=["datetime", "title", "duration"],
        engine="python",
        on_bad_lines="skip"
    )

    df["datetime"] = pd.to_datetime(
        df["datetime"].astype(str).str.lstrip("s"),
        format="%Y-%m-%d %H:%M:%S", errors="coerce"
    )

    df["duration"] = pd.to_numeric(df["duration"], errors="coerce")
    df = df.dropna(subset=["datetime", "duration"])
    df = df[df["duration"] > 0]

    df["duration"] = df["duration"].astype(int)

    df["content_type"] = df["title"].apply(content_type)

    songs = df["content_type"] == "song"
    df = df[~songs | ((df["duration"] >= 50) & (df["duration"] <= 600))]

    df = df.sort_values("datetime")
    df.to_csv(output_file, index=False)

clean_data()