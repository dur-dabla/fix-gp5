# -*- coding: utf-8 -*-

import argparse
import json
import mmap
import os.path
import shutil
import sys
from pathlib import Path


def main():
    # Declare parser and options
    parser = argparse.ArgumentParser(description='Fix drum tracks in .gp5 files')
    parser.add_argument('input_path',
                        help=".gp5 file to fix")
    parser.add_argument('--output', '-o', dest='output_path', default=None,
                        help="path of the result file (defaults to input file)")
    parser.add_argument('--track', '-t', dest='track', default=None,
                        help="name of the drums track to fix")
    args = parser.parse_args()

    # Determinate input
    input_path = Path(args.input_path)
    if input_path.suffix != '.gp5':
        print("The track extension must be '.gp5'")
        sys.exit(1)

    # Determinate output
    if args.output_path is None:
        output_path = input_path
    else:
        output_path = Path(args.output_path)
        shutil.copy2(input_path, output_path)

    # Determinate track(s) to look for
    if args.track is not None:
        tracks = [args.track]
    else:
        drums_file = os.path.abspath(os.path.join(__file__, '..', 'drums-tracks.json'))
        with open(drums_file, encoding='utf-8') as fd:
            tracks = json.load(fd)['tracks']

    # Look for track and change it if needed
    found = False
    with output_path.open('r+b') as fd_out:
        for track_name in tracks:
            track_name_bytes = bytes(track_name, 'utf-8')
            mm = mmap.mmap(fd_out.fileno(), 0)
            track_name_pos = mm.find(track_name_bytes)
            if track_name_pos != -1:
                found = True
                # Go two bytes prior to the found track name
                mm.seek(track_name_pos - 2)
                current_value = mm.read_byte()
                if current_value == 8:
                    # Fix the drums byte
                    mm.seek(track_name_pos - 2)
                    mm.write_byte(9)
                elif current_value == 9:
                    print("The drums track information for {track_name} was already correct")
                else:
                    print(f"Unknown track information byte {current_value} for {track_name}, aborting")
                    sys.exit(1)

        if not found:
            print("Could not find any drum track in the .gp5 file")
            sys.exit(1)


if __name__ == '__main__':
    main()
