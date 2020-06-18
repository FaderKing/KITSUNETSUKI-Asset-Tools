#!/usr/bin/env python3
# Copyright (c) 2020 kitsune.ONE team.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse

from kitsunetsuki.cardmaker import CardMaker


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--frames', type=str, help='comma separated frame groups')
    parser.add_argument(
        '--fps', type=int, help='frames per second rate')
    parser.add_argument(
        '--scale', type=float, help='object scale')
    parser.add_argument(
        '--output', type=str, help='output file')
    parser.add_argument(
        '--type', type=str, help='spritesheet file type')
    parser.add_argument(
        '--input', type=str, help='input files', nargs='+')
    parser.add_argument(
        '--empty', type=str, help='empty frame file')
    return parser.parse_args()


def main():
    args = parse_args()

    animations_frames = map(int, args.frames.split(','))

    kwargs = {}
    if args.fps:
        kwargs['fps'] = args.fps
    if args.scale:
        kwargs['scale'] = args.scale
    if args.type:
        kwargs['type'] = args.type
    if args.empty:
        kwargs['empty'] = args.empty

    cm = CardMaker(animations_frames, args.input, **kwargs)
    cm.make(args.output)


if __name__ == '__main__':
    main()
