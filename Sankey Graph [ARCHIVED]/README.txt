Created By Lex Baker, 11/10/21

Biggest Change:
Added a class to graphics.py, utilizing the Label widget in Tkinter. This allows for text to be aligned beyond the center. However, this presents an issue that seems to be permanently broken.
ISSUE = The background of all text is white. This can be changed, but seemingly not to transparent
(https://www.generacodice.com/en/articolo/4220126/how-to-make-a-tkinter-label-background-transparent)

Therefore, continue to use Text() unless alignment is required. I created Label() to be a mirror of Text(), so switching between the two is a matter of a single word change, and the addition/removal of .setAlign().

Optional Tasks:

-Help Menu ✓