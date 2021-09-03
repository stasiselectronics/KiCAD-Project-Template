# {ProjectName}

Welcome to the source files!

Here you can find all the files and folders needed to replicate or redesign this project!

{ProjectDescription}

# Current Status

{StatusUpdate}

# Documentation

{DocumentationDescription}

# Licenses

The design files for this project are covered under 

CERN-OHL-S
Cern Open Hardware License - Strongly Reciprocal
https://ohwr.org/cern_ohl_s_v2.pdf


# Using this as a template

This project structure was created using the Stasis Electronics KiCAD Template. It's what I use to help me focus on building circuit boards and writing firmware. 

The goal is to reduce the workload needed to keep and maintain good documentation that stays useful for years to come.

I hope it helps you as well!

## Folder Structure

The project is separated into main categories at the root of the project folder. I use "Hardware Files" to hold all of the printed circuit board design files. I also use some other descriptive names and keep them consistent amongst projects:

- **Enclosure Files** : 3D printed or somehow otherwise fabricated. All the files needed for the box the project might end up in.
- **Firmware Files** : The code for any microcontrollers that might end up on the boards. 
- **Mechanical Files** : Any CAD files for fabricating parts for the project. 

## Use as a template

[Use as a template!](https://github.com/stasiselectronics/KiCAD-Project-Template/generate)

I think that would work to create a template, I need to test this. [Create an issue](https://github.com/stasiselectronics/KiCAD-Project-Template/issues/new/choose) if it, or anything else doesn't work!

## Renaming the project

KiCAD as of writing doesn't have an easy way to rename a project. A shocker I know. I dream of a future where KiCAD has all the features we could ever want. 

So instead there's a python script to rename the project after creating you own:

    renameProject.py

It will look for the project name in the directory and ask for a new one.

You'll need python to execute the script, but you should have that, [right](https://www.python.org/)?

It will go and search through the directories and replace the string of the project's name everywhere that matters. 

## Libraries

The KiCAD project has a project specific library that can be used for keeping the custom designed footprints and symbols.

By default it isn't a global library, so if you would like to use the footprints or symbols in another project be sure to change it to a "global" library.


## Use Github Pages to deploy a static documentation website

Included in the project is a Jekyll static site written to provide more space to document the technical design. This way it keeps the discussion outside of the design files, but can be used to reference them and expand their information.

The site exists as a separate branch to this repository, and is titled "gh-pages"

You can view the [template's github page](https://stasiselectronics.github.io/KiCAD-Project-Template/) to get a better understanding of where to get started.

The site is using the [Minimal Mistakes](https://mmistakes.github.io/minimal-mistakes/about/) theme for jekyll. It is designed, developed, and maintained by [Michael Rose](https://mademistakes.com/about/) from Buffalo New York.
