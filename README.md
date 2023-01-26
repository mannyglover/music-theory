# music-theory
Here's where I will discuss some of my ideas on music theory, as well as attempt to write code that illustrates different aspects of music theory.

# First thoughts: why does standard music notation not have everything spaced apart by semi-tones?
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
