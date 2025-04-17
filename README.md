# ⛄ Snowman Meltdown Game

A fun command-line Python game where you try to **save the snowman** by guessing the hidden word, one letter at a time. But be careful—each wrong guess melts the snowman more and more!

---

## 🧊 Gameplay

You’ll be shown a word with hidden letters (underscores). Guess one letter at a time:

- ✅ Correct guesses reveal letters.
- ❌ Wrong guesses melt the snowman step-by-step.
- 💧 You lose if the snowman fully melts before you guess the word.

---

## 🎮 How to Play

1. Make sure you have **Python 3.x** installed.
2. Clone or download this repository.
3. Run the game:

```bash
   python snowman_game.py
```

---

## 📁 File Structure
```bash
    ├── ascii_art.py       # Contains ASCII art for snowman stages (melting animation)
    ├── snowman_game.py    # Main game logic
    └── README.md          # This file
```

--- 

## 📷 Screenshots
### Early Stage
```yaml
"""
    , ,    ,      ,    ,     ,     ,   ,      ,     ,     ,      ,      ,     
,       ,     ,    ,       ,   .____. ,   ,     ,      ,       ,      ,     
 ,    ,   ,    ,     ,   ,   , |   :|         ,   , ,   ,   ,       , 
   ,        ,    ,     ,     __|====|__ ||||||  ,        ,      ,      ,    
 ,   ,    ,   ,     ,    , *  / o  o \  ||||||,   ,  ,        ,    ,
,   ,   ,         ,   ,     * | -=   |  \====/ ,       ,   ,    ,     ,    
   ,  ,    ,   ,           , U==\__//__. \\//    ,  ,        ,    , 
,   ,  ,    ,    ,    ,  ,   / \\==// \ \ ||  ,   ,      ,          ,  
 ,  ,    ,    ,     ,      ,|    o ||  | \||   ,      ,     ,   ,     ,     
,      ,    ,    ,      ,   |    o ""  |\_|B),    ,  ,    ,       , 
  ,  ,    ,   ,     ,      , \__  --__/   ||  ,        ,      ,     ,   
,  ,   ,       ,     ,   ,  /          \  ||,   ,   ,      ,    ,    ,
 ,      ,   ,     ,        |            | ||      ,  ,   ,    ,   ,  
,    ,    ,   ,  ,    ,   ,|            | || ,  ,  ,   ,   ,     ,  ,   
 ------_____---------____---\__ --_  __/__LJ__---------________-----___
"""
    Word: _ _ _ _ _
    ✏️ Guessed letters:
```

### Meltdown 😱

```yaml
"""
------_____---------____--___---___--__----___---------________-----___
"""
💧 The snowman has completely melted!
🫥 The word was: python
```

---

## 🔁 Play Again?
After each round, the game will ask:

```text
Do you want to play again? (y-n)
```
Type y or yes to play again, or n / no to quit.

---

## 🧠 Tips

- Only single-letter alphabetical inputs are accepted.
- Repeated guesses are ignored with a warning.
- The game uses ascii_art.py to gradually melt the snowman.
- 
---

## 🤝 Contribution

Feel free to submit new word lists, snowman art, or translations!

---

## 🙌 Credits

Made with ❤️ and snowflakes by Ehsan Mehrali.

The snowman design belongs to the website https://asciiart.cc.

---

## 🐍 Requirements
No external libraries needed. Only standard Python 3.

---