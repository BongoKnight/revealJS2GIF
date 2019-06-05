# Reveal2gif

## What is RevealJS and what is pandoc?
RevealJS allow you to make nice HTML/CSS slides. Personaly I use pandoc to make these slides.
Pandoc allows you to write numbers of docs in markdown and to convert them in different formats. PDF, HTML, RTF, DOCX and... RevealJS.

## Why ?
For having nice GIF to put on Twitter.

## How it works?
It use geckodriver and selenium to open the slides in Firefox. Then take screenshots and reassemble them into a GIF.

```bash
pip3 install selenium, imageio
```

## Example of pandoc doc used in this case
A typical pandoc YAML header will be something like that :

```md
---
title: Slide
author: BongoKnight
date: 2019-06-05
revealjs-url: https://revealjs.com
theme: solarized
---

# In the morning

- Eat eggs
- Drink coffee

# Vertical

---

## Image
![](https://thispersondoesnotexist.com/image){width=40%}

- thispersondoesnotexist.com

---

## Generate false face
- GAN
- Learning




# In the evening

- Eat spaghetti
- Drink wine

# Conclusion

- And the answer is...
- $f(x)=\sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x-a)^n$      
```

## Demo

![GIF](./Slides.gif)

## Usage

```bash
python3 ./reveal2gif.py -p ~/Desktop/slide.html -d ./geckodriver -o ./
```

> It's possible to add a -k option in second line for 2D slides show. RRRDD will press Right arrow three time then Down arrow two time and take a screenshot each time.

The default use just press Right arrow until it's not possible anymore.

For simplicity of use geckodriver is shipped inside the repository. But you may have to update it.
