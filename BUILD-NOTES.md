# Build notes — The Router Confesses

## The brief

One line, at most 200 characters, spoken by a home Wi-Fi router excusing
itself for dropping the connection at the exact climax of a movie. A
pairwise AI judge picks the funnier excuse, weighing on-topic router voice
first, then the laugh and the twist, then a single breath, then freshness.
The judge explicitly rewards dodging the obvious buffering, bandwidth and
firmware-update jokes.

## Cliche radar

The lane almost every entrant will take is the generic apology: sorry for
buffering, too many devices, needs a restart, firmware update, the
neighbour stole the bandwidth. All of those lose on the freshness
criterion, so none of them were used.

## Concepts considered

Concept A, the mercy kill: the router cut the connection on purpose
because the ending was so bad it took the blame to spare the viewer.
Warm and protective, but the bad-ending mercy joke is a familiar shape.

Concept B, the grudge: the router finally stood up for itself after
months of blinking in the corner unthanked, and took the climax for
itself. Strong voice, but the unappreciated-appliance complaint is a
common appliance joke.

Concept C, the film-noir confession: the router is the twist villain. It
read the script, hated the ending, and pulled its own plug. This won:
the hook lands in the first two words, the twist reframes the whole
movie, the voice is smug and secretive, and it reads in one breath.

## The entry

Plot twist: the killer was me. I read the script, hated the ending, and
pulled my own plug.

Ninety-one characters, one line, no trailing newline in the output file.
The program validates the line before writing it: single line, between 1
and 200 characters, no leading or trailing whitespace.

## Scoring of the concepts

Hook, originality, sponsor fit, clarity, each out of ten. Concept A
scored 7, 7, 9, 9 for 32. Concept B scored 8, 8, 8, 8 for 32. Concept
C scored 9, 9, 9, 9 for 36 and was built.

## Verification

A fresh run of the program writes the same bytes to the output file, and
the kit check shows the expected pattern of four passes, one expected
failure for transcripts, and fourteen skips.
