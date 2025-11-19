# Asteroids Game 🚀

Classic arcade-style Asteroids implemented in Python using Pygame. Pilot your spaceship, destroy asteroids, and survive as long as possible!

## 🎮 Controls
Action	Key
Rotate Left	A
Rotate Right	D
Move Forward	W
Move Backward	S
Shoot	SPACEBAR
## 🪐 Features

Large asteroids split into smaller, faster asteroids

Small asteroids disappear when destroyed

Smooth movement with frame-rate independent physics

Shooting cooldown to prevent spamming

Collision detection between player and asteroids

Event logging for "player_hit" and "asteroid_split"

##⚡ Quick Start
git clone <repository-url>
cd asteroids-game
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
pip install pygame
python main.py

## 🗂️ File Structure

main.py – Game initialization and main loop

player.py – Player movement, rotation, and shooting

asteroid.py – Asteroid behavior, splitting, and drawing

shot.py – Projectile class

asteroidfield.py – Manages multiple asteroids

constants.py – Game constants (speeds, screen size, colors)

logger.py – Event logging

## 📌 Notes

Uses pygame.Vector2 for movement and collision calculations

Shooting and movement are time-based (dt) for consistent gameplay

Asteroids split into random directions when destroyed

## 📜 License

Educational project – free to use and modify for learning purposes. made with boot.dev course
