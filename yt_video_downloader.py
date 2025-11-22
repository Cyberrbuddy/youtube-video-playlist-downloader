import yt_dlp

# ------------------------------------------------------
# LIST FORMATS
# ------------------------------------------------------
def list_formats(video_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'ignoreerrors': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        formats = info.get('formats', [])

        video_formats = []

        for f in formats:
            if f.get('vcodec') != 'none' and f.get('acodec') != 'none':
                height = f.get('height')
                fps = f.get('fps')

                if not height:
                    continue

                # Display like: "1080p60", "720p30", etc.
                display = f"{height}p{fps if fps else ''}"

                video_formats.append({
                    'format_id': f.get('format_id'),
                    'display': display,
                    'height': height,
                    'fps': fps if fps else 0,
                    'ext': f.get('ext', '')
                })

        # Remove duplicates, keep highest fps per resolution
        unique = {}
        for f in video_formats:
            key = f['height']
            if key not in unique or f['fps'] > unique[key]['fps']:
                unique[key] = f

        # Sort: highest resolution first, then highest fps
        sorted_formats = sorted(
            unique.values(),
            key=lambda x: (x['height'], x['fps']),
            reverse=True
        )

        return sorted_formats


# ------------------------------------------------------
# DOWNLOAD FUNCTION
# ------------------------------------------------------
def download(url, format_id=None, is_playlist=False):
    outtmpl = (
        'Downloaded_Playlist/%(playlist_index)s - %(title)s.%(ext)s'
        if is_playlist else
        'Downloaded_Videos/%(title)s.%(ext)s'
    )

    ydl_opts = {
        'format': format_id if format_id else 'best',
        'outtmpl': outtmpl,
        'ignoreerrors': True,
        'progress_hooks': [
            lambda d: print(
                f"Downloading: {d.get('filename', '')} ({d.get('_percent_str', '0%')})"
            ) if d['status'] == 'downloading' else None
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# ------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------
def main():
    choice = input("Single Video (1) or Playlist (2)? Enter 1 or 2: ").strip()

    if choice not in ['1', '2']:
        print("Invalid choice!")
        return

    url = input("Enter the YouTube URL: ").strip()
    is_playlist = (choice == '2')

    # Single video
    if not is_playlist:
        print("Fetching available video qualities...")
        formats = list_formats(url)

        if not formats:
            print("No combined video+audio formats found. Downloading best available...")
            download(url)
            return

        print("\nAvailable Qualities:")
        for i, f in enumerate(formats, 1):
            print(f"{i}. {f['display']} ({f['ext']}) - ID: {f['format_id']}")

        selected = input("\nEnter option number (Enter = Best): ").strip()

        if selected.isdigit():
            idx = int(selected) - 1
            if 0 <= idx < len(formats):
                chosen = formats[idx]['format_id']
                print(f"Downloading {formats[idx]['display']}...")
                download(url, chosen)
            else:
                print("Invalid choice. Downloading best...")
                download(url)
        else:
            print("Downloading best quality...")
            download(url)

    # Playlist download
    else:
        print("Downloading playlist in best quality...")
        download(url, is_playlist=True)

    print("\nDownload completed!")


if __name__ == "__main__":
    main()
