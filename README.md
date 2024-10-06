# yt-snip

A simple cli tool to download and cut youtube videos.

# Usage

```bash
yt-chop <youtube-video-url> -s <starting-time> -e <ending-time>
```

The format of `starting time` and `ending time` must be
`hh:mm:ss`.

For example,

```bash
yt-chop https://www.youtube.com/watch?v=KeaXqgR5cvI -s '0:03' -t '0:14'
```

## Assumptions

- If only the `ending time` is supplied, then the
  `starting time` is assumed to be `0:00`.

- If only the `starting time` is provided, the ending time
  is assumed to be the time at which the video ends.

- If both starting and ending time are not supplied, then
  yt-chop just downloads the youtube video.

# Requirements

- Docker is required to run yt-chop.

# Setup

1. Clone the repo to an appropriate place on your machine.

2. Create a shell alias for `yt-snip`.

   ## zsh

   Include the following lines of code in your `~/.zshrc`
   file.

   ```bash
   ls
   ```

3. Source your shell's configuration file.

   ```bash
   source ~/.zshrc
   ```
