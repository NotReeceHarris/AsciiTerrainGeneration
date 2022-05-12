# ⛰️ Procedural Terrain Generation Algoriths

[![Ascii Output](https://github.com/NotReeceHarris/NotReeceHarris/blob/main/cdn/topo.png?raw=true)](https://tinyurl.com/yckkbd8w)
<!--
```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░#### ┃  // Highest to Lowest
┃ ▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░###### ┃  Level 6 : ▓
┃ ▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░######## ┃  Level 5 : ▒
┃ ▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░########## ┃  Level 4 : ░
┃ ▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░############ ┃  Level 3 : #
┃ ▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░############## ┃  Level 2 : =
┃ ▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░##############== ┃  Level 1 : ~
┃ ▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░##############==== ┃  Level 0 : -
┃ ▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░##############====== ┃
┃ ▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░##############======== ┃  // Algorithm Settings
┃ ▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░##############========== ┃  Seed    : -38456256574
┃ ▒▒▒▒▒▒░░░░░░░░░░░░░░##############============ ┃  Coords  : X: 42 ,Y: 12
┃ ▒▒▒▒░░░░░░░░░░░░░░##############============== ┃
┃ ▒▒░░░░░░░░░░░░░░##############==============~~ ┃  // Generation Info
┃ ░░░░░░░░░░░░░░##############==============~~~~ ┃  Time    : 0.83 /ms
┃ ░░░░░░░░░░░░##############==============~~~~~~ ┃  Size    : 46 x 19
┃ ░░░░░░░░░░##############==============~~~~~~~~ ┃
┃ ░░░░░░░░##############==============~~~~~~~~~~ ┃
┃ ░░░░░░##############==============~~~~~~~~~~~~ ┃
┃ ░░░░##############==============~~~~~~~~~~~~~~ ┃
┃ ░░##############==============~~~~~~~~~~~~~~~- ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```
-->
> On the journey of expanding my knowledge, I decided to create procedural topography generation algorithms in every language possible. Topography generation is not a very common algorithm however it is a core element for a lot of data analytic and game map generation.

## Helpfull Research
- Perlin noise
  - [Perlin noise wiki](https://en.wikipedia.org/wiki/Perlin_noise)
  - [How Procedurally Generated Terrain Works](https://www.youtube.com/watch?v=JdYkcrW8FBg)
  - [A Parallel Algorithm Using Perlin Noise Superposition Method for Terrain
Generation Based on CUDA architecture](https://www.researchgate.net/profile/Huailiang-Li-2/publication/301431773_A_Parallel_Algorithm_Using_Perlin_Noise_Superposition_Method_for_Terrain_Generation_Based_on_CUDA_architecture/links/5d5900d245851545af4c2067/A-Parallel-Algorithm-Using-Perlin-Noise-Superposition-Method-for-Terrain-Generation-Based-on-CUDA-architecture.pdf)
- Simplex noise
  - [Simplex noise wiki](https://en.wikipedia.org/wiki/Simplex_noise)
- Opensimplex noise
  - [Opensimplex noise wiki](https://en.wikipedia.org/wiki/OpenSimplex_noise)
- Other
  - [Make some noise with Python and generate terrain (Michael McHugh)](https://www.youtube.com/watch?v=O33YV4ooHSo)
