# music-theory
Here's where I will discuss some of my ideas on music theory, as well as attempt to write code that illustrates different aspects of music theory.

# 2023-01-26 {

# First thoughts: why does standard music notation not have everything spaced apart by semi-tones? (0)
The first response will be, "Because we don't typically play atonal music: usually we take 7 or so of possible 12 semitones, so it makes sense that this would be integrated into the notation so that a pianist (for example) can more easily see which of the 7 possible semitones (and at what octave) they must hit on the keyboard."  But the reason I have thought that a lines-spaced-by-semitones notation system is better is because the musician, whether a singer or an instrumentalist, will always know the exact intervals between any two notes, at a glance.  As a long-time choral ensemble member, I have often struggled to sight read.  I know the difference between going up a semitone or two semitones, but when there is a "whole step" up or down in the scale, I don't know whether it's one or two semitones.  Of course, there are systems that address these problems, like do-re-mi-fa-so-la-ti-do, but whenever a song has accidentals, it puts a wrench into the gear of that system.  There are remedies, like doing "ri" instead of "re" when it's sharpened, and "ra" instead of "re" when it's flattened, but to, at a glance, know the interval between "ri" and "so" is not something that I think is easy.  So instead of "do-re-me-fa-so-la-ti-do" I propose "zer-one-two-three-four-five-six-se'en-eight-nine-ten-'le'en-twelve-thirt" or "0-1-2-3-4-5-6-7-8-9-10-11-12-13".  Having 0 as the root note instead of 1 has the advantage that you can have negative number versions of all the "sols": "none-nwo-nree-nour-nive-nix-ne'en-neight-nene-nen-n'le'en" (clearly, the negative number versions are not as readable as the positive number versions, but the system works very well without using any negative numbers).

So if we are dealing with numbers instead of "words" (whatever you would call "do", "re", "mi", etc), and we want to be able to gauge the intervals by simple subtraction, we would want a notation system where each "up" equals up one semitone and each "down" equals down one semitone.  I will give a rudimentary visualization of this system here, rather than trying to whip something up on Google Draw, for example.
```
                                                                        -------D--
                                                                          C#
                                                                   --C-------
                                                                B
-----------------------------------------------------------A#-------------------------------------------------------------------
                                                      A
-------------------------------------------------G#-----------------------------------------------------------------------------
                                            G
---------------------------------------F#---------------------------------------------------------------------------------------
                                  F    
-----------------------------E--------------------------------------------------------------------------------------------------
                        D#   
-------------------D------------------------------------------------------------------------------------------------------------
              D#   
---------C----------------------------------------------------------------------------------------------------------------------
```
Or, with numbers:
```
                                                                        -------D--
                                                                          1 [or "13"]
                                                                   --12-------
                                                                11
-----------------------------------------------------------10-------------------------------------------------------------------
                                                      9
-------------------------------------------------8------------------------------------------------------------------------------
                                            7
---------------------------------------6----------------------------------------------------------------------------------------
                                  5    
-----------------------------4--------------------------------------------------------------------------------------------------
                        3   
-------------------2------------------------------------------------------------------------------------------------------------
              1   
----------0----------------------------------------------------------------------------------------------------------------------
```

[IDEA: make a new music notation system, and write code to convert music in the traditional system (e.g., they have XML versions of a music score) into your new system.  Then, if any fellow musicians wanted to try your new notaion system on one of their favorite pieces of music, they could easily do so.]

Now, of course, "if it ain't broke, don't fix it", so I see no reason to change the system of notation that denotes the note's duration.  So, here's another example, but with asterisks (\*) representing the notes (let's say they are quarter notes):
```
                                                                                    --------*--
                                                                                        *
                                                                    ----------------*-------
                                                                        *     
---|--------------------------|-----------------------|-------------*---------|-------------------------------------------------
   |                          |                       |         *             |
---|--------------------------|-----------------------|-----*-----------------|-------------------------------------------------
   |                          |                 *     |                       |
---|--------------------------|-------------*---------|-----------------------|-------------------------------------------------
   |                          |         *             |                       |
---|--------------------------|-----*-----------------|-----------------------|-------------------------------------------------
   |                    *     |                       |                       |
---|---------------*----------|-----------------------|-----------------------|-------------------------------------------------
   |          *               |                       |                       |
---|-----*--------------------|-----------------------|-----------------------|-------------------------------------------------
```

[IDEA: have a "markdown" for music notation.  In other words, make a notation software where the ascii file specifying the music is also human-readable.]

Now, here's an example where we go up the C major scale
```                                                                                        
                                           --------*-----|
                                              *          |                      
---|--------------------------|--------------------------|-----------------------|-------------------------------------------------
   |                          |          *               |                       |
---|--------------------------|--------------------------|-----------------------|-------------------------------------------------
   |                          |     *                    |                       |
---|--------------------------|--------------------------|-----------------------|-------------------------------------------------
   |                    *     |                          |                       |
---|---------------*----------|--------------------------|-----------------------|-------------------------------------------------
   |                          |                          |                       |
---|----------*---------------|--------------------------|-----------------------|-------------------------------------------------
   |                          |                          |                       |
---|-----*--------------------|--------------------------|-----------------------|-------------------------------------------------
```
## 2023-01-27 {
# First thoughts: why does standard music notation not have everything spaced apart by semi-tones? (1)
## Andrew's Lego song, in my new notation system
Today, I'm going to try to articulate Andrew's Lego song in my new notation.  Before I do that, I am tempted to write a little Python program to convert from a list of 2D tuples--where each 2D tuple consists of a note (e.g., "C#") and a duration (e.g., "2" for a half note, "4" for a quarter note, etc).  Before I begin to write such a program, I will think out loud about what the program should output and how.

* The program should be able to handle all durations, from a whole note to a sixty fourth note.
    * The program should allow spaces between each note, at least up until thirty second notes.
        * It may be okay to have no spaces between sixty fourth notes.

[INTERJECTION: As my right wrist/hand are hurting when I type, I shall continue thinking out loud about this with old fashioned pen and paper.]

I have started on a Python program to be able to express music in "standard megic notation".  The program takes a sequence of `(note, duration)` tuples as its input, and it will output ascii characters that represent the melody in "standard megic notation".  I have decided that I will model only notes of duration within [1/64, 1/1].  If I use the two digit numbering system that I have devised (but not necessarily decided upon, an example of a melody [(C,4),(E,4),(G,2)] can be depicted as follows:
1. First, I will show the decimal numbers, split into 100's, 10's, and 1's, to make it easy to see where key columns like 64 and 128 are.
```
100's place: 00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111
 10's place: 00000000001111111111222222222233333333334444444444555555555566666666667777777777888888888899999999990000000000111111111122222222
  1's place: 01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567
```
2. Now, I will do the same for binary.
```
128'splace: 000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001
64's place: 000000000000000000000000000000000000000000000000000000000000000011111111111111111111111111111111111111111111111111111111111111110
32's place: 000000000000000000000000000000001111111111111111111111111111111100000000000000000000000000000000111111111111111111111111111111110
16's place: 000000000000000011111111111111110000000000000000111111111111111100000000000000001111111111111111000000000000000011111111111111110
8's  place: 000000001111111100000000111111110000000011111111000000001111111100000000111111110000000011111111000000001111111100000000111111110
4's  place: 000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110000111100001111000011110
2's  place: 001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110011001100110
1's  place: 010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010
```                                                                                                                                          
3. The lines above are so that I can figure out where to put the measure lines and line up the notes correctly.  [(C,4),(E,4),(G,2)] can now be depectied as:
```                                                                                                                                         
-----------|---------------------------------------------------------------------------------------------------------------------------------|
           |                                                                                                                                 |
-----------|---------------------------------------------------------------------------------------------------------------------------------|
           |                                                                                                                                 |
-----------|----------------------------------------------------------------02...............................................................|
           |                                                                                                                                 |
-----------|---------------------------------------------------------------------------------------------------------------------------------|
           |                                                                                                                                 |
-----------|--------------------------------04..............................-----------------------------------------------------------------|
           |                                                                                                                                 |
-----------|---------------------------------------------------------------------------------------------------------------------------------|
           |                                                                                                                                 |
-----------|04..............................-------------------------------------------------------------------------------------------------|
           |                                                                                                                                 |
```
## 2023-01-27 }
# 2023-01-26 }
