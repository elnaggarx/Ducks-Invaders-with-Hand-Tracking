# 🦆 Ducks Invaders: War of Fayoum

**Ducks Invaders: War of Fayoum** is a hilarious Egyptian parody of *Chicken Invaders* with a twist — you fight invading Fayoumi ducks with hand gestures, thanks to real-time **hand tracking** using your webcam.

---

## 🎮 Game Overview

The ducks of Fayoum have had enough...  
They've taken to the skies and are dropping **deadly eggs** on your spaceship.  
Your mission: **dodge, shoot, and survive** — using nothing but your **hand**.  
You’ll navigate and fire your spaceship using **your index and middle fingers** via your webcam!

---

## 🧠 Features

- 🖐️ **Hand Tracking Controls** using your real-life fingers
- 🦆 **Ducks** that drop eggs at randomized intervals
- 🚀 **Spaceship Movement** with index finger tracking
- 🔫 **Shooting** by raising both the index and middle fingers
- 🌌 Animated **starfield** background
- 🔊 **Background music** and future-ready for effects
- 😂 **Egyptian humor & cultural flavor**

---

## 🛠️ Tech Stack

| Tech         | Purpose                              |
|--------------|--------------------------------------|
| Python       | Game logic and backend               |
| Pygame       | Rendering, display, sound            |
| OpenGL       | 3D rendering (via PyOpenGL)          |
| OpenCV       | Access webcam and frame processing   |
| MediaPipe    | Real-time hand and finger detection  |

---

## 📁 Project Structure

DucksInvaders/

├── game.py # Main game logic

├── handTracking.py # Hand detection module

├── Duck.py # Duck behavior and egg drop logic

├── Egg.py # Egg class, falling animation

├── Spaceship.py # Spaceship drawing and shooting

├── geometricShapes.py # Helper functions for OpenGL shapes

├── assets/
│ ├── sounds/ # Background music, sfx
│ 
└── README.md # You're reading it!


---

## 🚀 Getting Started

### ✅ Prerequisites

Ensure Python 3.7+ is installed. Then install dependencies:

```bash
pip install pygame opencv-python mediapipe PyOpenGL

python game.py

```
##Controls

| Action         | How to Perform It                    |
| -------------- | ------------------------------------ |
| Move spaceship | Raise and move your **index finger** |
| Shoot          | Raise your **index + middle finger** |
| Quit           | Close the game window                |

🕹️ Gameplay Mechanics
Ducks appear randomly and drop eggs at different times.

Each duck drops 1 egg every 1–10 seconds independently.

Eggs fall vertically and must be dodged.

Stars twinkle in the background to simulate deep space.

Your hand is your joystick & trigger!

🤓 Credits
Developed by: Mohamed Amr
🎓 Computer Engineering Student
🔗 [Portfolio](https://mohamed-amr.netlify.app/)  | 📧 elnaggarx2003@gmail.com

📜 License
This game is open-source under the MIT License.
Feel free to fork it, enhance it, or replace the ducks with aliens or camels!
