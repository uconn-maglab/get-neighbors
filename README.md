# get_neighbors.py

>Python script to find the phonological neighbors of a list of words, using the deletion, addition, substitution rule ("DAS," Luce & Pisoni, 1998).

This uses the [IPhOD2 database](http://iphod.com) (Vaden, Halpin, & Hickok,
2009), but any corpus can be used, as long as it contains only the phonological
transcriptions, one per line. (See uconn-maglab/words-only if you need to 
isolate the phonological forms).

## Requirements & Dependencies

* Python 3 (written in 3.5, not tested on other versions)
* pandas
* json (recommended, included with the Python standard library)
* A corpus of only phonological word forms, one per line (see 
uconn-maglab/words-only for help with this). Currently set up to support the
use of [IPhOD](http://iphod.com), but any corpus of phonological transcriptions
will work.

## Usage

The script is in `get_neighbors.py`.

At the bottom of the script, there is a commented-out section, starting with 
`if __name__ == "__main__"`. You may wish to un-comment this section and update
it according to your needs. Alternatively, you could load the module in an
interactive Python session and run it there.

You will first need to make a `NeighborHunt` object that points to the word 
list and corpus file (replace the "path"s with the actual paths to your files):

```py
my_hunt = NeighborHunt(words="path/to/wordlist.txt", 
		       corpus="path/to/corpus.txt", sep=".")
```

The `sep` argument refers to the character(s) used to separate phonemes in the
phonetic alphabet you are using. If each character is one phoneme, and there is
no separator, you can use `sep=""` to split the words into individual characters.

Next, you need to actually run the finder:

```py
my_hunt.find(debug=True)
```

When `True`, the `debug` option prints the current word and all candidate 
neighbors to the console. It defaults to `False`, but if you feel better seeing
the progress, I recommend that you set it to `True`. It can take a while to run.

The results of the hunt will be stored in a dictionary as 
`NeighborHunt.neighbors`. The easiest and possibly most portable way to save
it is as a JSON string. (The `indent` is optional, but makes it easier to read.)

```py
with open("path/to/optput/file.json", "w") as f:
    json.dump(my_hunt.neighbors, f, indent=4)
```

You should check the output file to make sure everything looks right before 
closing out of your Python session (if you're running interactively), but other
than that, you should be all set!

## License

This project is licensed under the terms of the MIT license, copyright (c) 2016
R Steiner. **You are welcome to use, modify, and distribute this program with
proper attribution.** See `LICENSE` for more details.

## References

Luce, P. A., & Pisoni, D. B. (1998). Recognizing spoken words: The neighborhood 
activation model. *Ear and Hearing, 19*(1), 1.

Vaden, K.I., Halpin, H.R., Hickok, G.S. (2009). Irvine Phonotactic Online 
Dictionary, Version 2.0. [Data file]. Available from http://www.iphod.com.
