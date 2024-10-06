# yt-snip

A simple cli tool to download and cut youtube videos.

# Usage

```bash
yt-snip <youtube-video-url> -s <starting-time> -e <ending-time>
```

The format of `starting time` and `ending time` must be
`hh:mm:ss`.

For example,

```bash
yt-snip https://www.youtube.com/watch?v=KeaXqgR5cvI -s '0:03' -t '0:14'
```

## Assumptions

- If only the `ending time` is supplied, then the
  `starting time` is assumed to be `0:00`.

- If only the `starting time` is provided, the ending time
  is assumed to be the time at which the video ends.

- If both starting and ending time are not supplied, then
  yt-snip just downloads the youtube video.

# Requirements

- Docker is required to run yt-snip.

# Setup

1. Clone the repo to an appropriate place on your machine.

2. Create a shell alias for `yt-snip`.

   ## zsh

   Include the following lines of code in your `~/.zshrc`
   file.

   ```bash
    yt-snip() {

      # Create a directory named yt-snips in the shell's current working directory
      # and bind mount it into the Docker container. The program running inside the
      # container will save the trimmed video to the yt-snips directory.

      if [ ! -d './yt-snips' ]; then
        mkdir './yt-snips'
      else
        # If the directory already exists, bind mount it as is, including any files it may
        # contain. This ensures the container can only access the yt-snips folder and
        # nothing else on your host machine.
        echo "The 'yt-snips' directory already exists."
        echo "The 'yt-snips' directory may contain confidential files that you might not want to share with the container."
        echo "Do you wish to share it with the container? (y/n)"
        read -r response
        if [[ $response == "y" ]]; then
            echo "You chose to share the 'yt-snips' directory with the container."
            # Add the code to bind mount the directory here
        else
            echo "You chose not to share the 'yt-snips' directory with the container."
            echo "exiting!"
            return
        fi
      fi

      docker-compose -f ~/scripts/yt-snip/docker-compose.yml run --rm yt-snip "$@"
    }
   ```

3. Source your shell's configuration file.

   ```bash
   source ~/.zshrc
   ```
