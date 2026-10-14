# Lab 06 — Courtyard Office

Xuan Zhu · Ronan83

A simple two-storey office with an L-shaped footprint and an open courtyard. I kept the details limited to windows, floor borders, a flat roof, and one entrance canopy.

![Courtyard office](images/building_hero.png)

## Base project

The generator follows the tutorial's main workflow:

1. A floor multiparm controls the width, depth, and storey count of each block. Two extra dimensions define the return wing of the L shape.
2. SideFX Labs Align and Distribute stacks the floor blocks along Y.
3. Wall, roof, and base faces are labeled by their normals. Each wall is split into floors and evenly fitted bays.
4. Window, blind, storefront, and door modules are prepared in local space. A Copy to Points SOP selects modules by `name` and uses `N`, `up`, and `scale` to place them on every wall.

The default model has **two storeys and 68 facade cells**. The ground floor uses taller glazing; one courtyard-facing cell is the entrance.

## Advanced project

- **Randomize placement, 27:07:** a seed and probability choose between a standard window and a window with blinds. The result is repeatable.
- **Borders, 35:22:** thin perimeter strips follow the L-shaped floor boundaries and update when the building dimensions change.

## Color and simple extras

The geometry has terracotta walls, blue glazing, and dark frames. A small flat canopy with two posts marks the entrance. There are no external textures, plants, rooftop equipment, or additional scene assets to install.

![Entrance](images/building_entrance.png)

## Open the project

Open **`lab06.hipnc`** and select **`/obj/COURTYARD_OFFICE/BUILDING_GENERATOR`**. The parameters control the floors, courtyard dimensions, facade, randomization, and borders. Dive inside to inspect the numbered nodes.

The custom building HDA and **Labs Align and Distribute 2.0** are **embedded in the HIP file**. The Labs asset is from the official **22.0.429 Production** release, matching Houdini **22.0.429** used for this project.

`source/` contains readable copies of the Python SOP code; these files are not needed to open the HIP. `validation.json` records parameter and saved-file checks. Images are Karma CPU renders of the submitted geometry, with the Apprentice watermark retained.

## Reference and submission

- [Simon Houdini tutorial](https://www.youtube.com/watch?v=uIe97023sDk)
- [SideFX Labs 22.0.429](https://github.com/sideeffects/SideFXLabs/releases/tag/22.0.429), with license in `THIRD_PARTY_LICENSE.md`.

Submit **`lab06.hipnc`** to Canvas together with the course PR link.

---

# CIS 5660 Lab 06 Procedural Buildings

## Project Overview
In this lab, you will follow a Houdini tutorial on using shape grammars to make procedural buildings. The tutorial is linked here: 
https://www.youtube.com/watch?v=uIe97023sDk&t=979s&ab_channel=SimonHoudini 

### Setup
The tutorial requires some nodes from `SideFX Labs`. If you haven’t already installed the Labs packages, you can do so at the “Labs/Packages” tab of the Houdini Launcher.
Make sure that the version of `Labs` that you install is __not__ newer than your overall Houdini install (e.g. if you have Houdini 21.544,
don't install `Labs` 22.650). Use the Production version of `Labs`, not the Daily.

### Base Project
Follow the tutorial up through the Placing Assets section (ending at about 27 minutes). Create a simple office-style building with procedurally-placed windows.

### Advanced Project
Choose any of the tutorial segments *after* the 27-minute mark. Implement at least one of them to make your building more interesting.

### Extra Credit
Give your building color/textures/additional components!

## Submission
- Update your README with screenshots or renders of your building.
- Create a pull request to this repository
- Submit your Houdini file to Canvas along with a link to your pull request 
- IMPORTANT NOTE: make sure your HDA is either embedded in the HIP file or included with your submission. Creating an HDA saves a .hda file at the location you specify with the definition of your HDA. 
Alternatively, when you save your HDA you can choose the “Embedded in HIP File” option (rather than specifying the path), and the hda definition will be automatically embedded in your hip file (and no additional files will be needed with submission).
