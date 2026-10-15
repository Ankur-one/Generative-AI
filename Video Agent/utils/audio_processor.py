from pathlib import Path
import yt_dlp
from yt_dlp.utils import DownloadError

DOWNLOAD_DIR = Path(__file__).resolve().parent.parent / "downloads"
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)


def download_youtube_audio(url: str) -> str:
    if not url or not url.strip():
        raise ValueError("Please provide a valid YouTube URL.")

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(DOWNLOAD_DIR / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
            }
        ],
        "quiet": False,
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url.strip(), download=True)

            if not info:
                raise RuntimeError("Could not retrieve video information.")

            # Locate the converted WAV file.
            requested = info.get("requested_downloads") or []
            source_path = (
                requested[0].get("filepath")
                if requested else ydl.prepare_filename(info)
            )

            wav_path = Path(source_path).with_suffix(".wav")

            if not wav_path.exists():
                # Fallback: search for the generated WAV file.
                matches = list(DOWNLOAD_DIR.glob("*.wav"))
                if matches:
                    wav_path = max(matches, key=lambda p: p.stat().st_mtime)
                else:
                    raise FileNotFoundError(
                        "WAV file was not created. Check the FFmpeg output."
                    )

            print(f"Audio saved to: {wav_path.resolve()}")
            return str(wav_path.resolve())

    except DownloadError as exc:
        raise RuntimeError(f"YouTube download failed: {exc}") from exc


if __name__ == "__main__":
    video_url = input("Enter YouTube video URL: ").strip()

    try:
        audio_path = download_youtube_audio(video_url)
        print(f"\nDownload successful!\nFile: {audio_path}")
    except (ValueError, RuntimeError, FileNotFoundError) as exc:
        print(f"\nError: {exc}")