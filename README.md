# spike-prime-api
The unofficial stubbed MicroPython API for SPIKE Prime, including both hub and spike modules

## Purpose
I've created this for the First Lego League Challenge team that I'm coaching (FLL51093 Lightning TECH) to enable IntelliSense under Visual Studio Code while working on Lego SPIKE Prime projects, which makes their coding experience more convienent and fun.
I hope this kit would be helpful for other fellow FLL teams as well

## Usage
This kit is meant to work with VSC extension [PeterStaev.lego-spikeprime-mindstorms-vscode](https://marketplace.visualstudio.com/items?itemName=PeterStaev.lego-spikeprime-mindstorms-vscode).
To use it, simply download and place both hub and spike folders and place them under your project, to make your code structure looks like this:
  <br>\>hub
  <br>\>spike
  <br>yourcode.py

## Credits
spike module is based on https://github.com/sanjayseshan/spikeprime-tools/blob/master/spiketools/hub/spike.py, which was created by @jeffdamp and @sanjayseshan (Thanks!)<br>
hub module is created by myself based on the document shared at https://lego.github.io/MINDSTORMS-Robot-Inventor-hub-API/
