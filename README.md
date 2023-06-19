# le-diecey
A python script/program that rolls dice. (Also for D&amp;D)

<br>
<br>

# Updates
> 06/19/23
Updated:

- Randomness is now generated via atmospheric noise instead of math. Should be as close to random as one could get.

- Bug fixes with custom rolling has been fixed.
__ __

<br>
<br>

# Extra Info
When rolling a d10 die, it is formatted as `0-9`. The percentile die is `00-90`. When they are rolled in tandem, you will get something like `d10: 7` & `d10p: 60`. This should be read as `67`. If the d10 rolls a "0", it should be read as a `10`. If you get "00" for the percentile die, your percentile roll is whatever the d10 shows. If the d10 also rolls a "0", giving you `0`:`00`...then it should be treadted as `100`.

However, if you would like to do percentile rolls a different way, you can just pick `custom` in the d&d menu and roll 2 d10s and do it that way. (I have seen/heard that is another way of doing percentile rolls). I am not sure how common it is to roll 2 d10s, but hey..it's an option.

> Note: All of this "extra info" is just from what I have read on forums, blogs, and reddit.
__ __

<br>
<br>


# Install & Play
```
git clone https://github.com/therealOri/le-diecey.git
cd le-diecey
virtualenv dceENV
source dceENV/bin/activate
pip install -r requirements.txt
python le-diecey.py
```
> If you don't have `virtualenv` you can install it via **pip**. `pip install viartualenv`.
__ __

<br>
<br>

# Demo
[![asciicast](https://asciinema.org/a/wY23og3yHZ6S3a8v24HQYQBej.svg)](https://asciinema.org/a/wY23og3yHZ6S3a8v24HQYQBej)
> As of (update) 06/19/23 - The results may look a bit different but the menu and options are still the same.
__ __

<br />
<br />
<br />


# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)
