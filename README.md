(De)composite Collections
=========================

![White man](images/sample_01.jpg)

Bernardo Fontes, source code repository, 2021.

»(De)composite Collections« is an ongoing investigation into the formation and updates of the colonialist gaze in museum collections. Developed in the context of the intelligent.museum residency, its starting point are artistic collections organized in the first half of the 20th century.

This code has been developed by Bernardo Fontes, as part of the [»The Intelligent Museum«](#the-intelligent-museum). 
Funded by the Digital Culture Programme of the Kulturstiftung des Bundes (German Federal Cultural Foundation). 
Funded by the Beauftragte der Bundesregierung für Kultur und Medien (Federal Government Commissioner for Culture and Media).
Supported by the Faculty of Architecture and Urbanism of the University of São Paulo (FAU-USP) C4Ai – INOVA-USP and GAIA.

For information on usage and redistribution, and for a DISCLAIMER OF ALL WARRANTIES, see the file, [LICENSE.txt](LICENSE.txt), in this repository. 
BSD Simplified License.

Description
-----------

### Summary

This README has the purpose to cover the required technical efforts in order to generate the results analyzed by the project.
You can find a more detailed and conceptualized explanation about it in ZKM website, both in [German](https://zkm.de/de/decomposite-collections) or [English](https://zkm.de/en/decomposite-collections) versions.

The overall technical goal was to train a dozen [GAN models](https://en.wikipedia.org/wiki/Generative_adversarial_network) to synthesize new images using the catalog 2 important Brazilian museums as the train dataset.
The museums are the Museu Paulista (MP USP) and the Contemporary Art Museum (MAC – USP).
Each GAN was trained with dataset composed by grouped cuts from the original artworks from each museum. Each group represent a category we would like to investigate and experiment on top of.
The list of categories used in this work are:

- Sky
- Flora
- Fauna
- Black Women
- White Women
- Black Men
- White Men
- Indigenous

Unfortunately, due to copyright requirements, we're not allowed to share the museums' catalog and neither the resulted datasets with the cuts grouped by these categories.
So, this documentation will try to cover all the steps we needed to go through in order to have the final GAN models trained and to generate results from it.

### Step 1 - Organizing the artworks information

### Step 2 - Creating the dataset

### Step 3 - Training the GANs

### Step 4 - Generating results

The Intelligent Museum
----------------------

An artistic-curatorial field of experimentation for deep learning and visitor participation

The [ZKM | Center for Art and Media](https://zkm.de/en) and the [Deutsches Museum Nuremberg](https://www.deutsches-museum.de/en/nuernberg/information/) cooperate with the goal of implementing an AI-supported exhibition. Together with researchers and international artists, new AI-based works of art will be realized during the next four years (2020-2023). They will be embedded in the AI-supported exhibition in both houses. The Project „The Intelligent Museum” is funded by the Digital Culture Programme of the [Kulturstiftung des Bundes](https://www.kulturstiftung-des-bundes.de/en) (German Federal Cultural Foundation) and funded by the [Beauftragte der Bundesregierung für Kultur und Medien](https://www.bundesregierung.de/breg-de/bundesregierung/staatsministerin-fuer-kultur-und-medien) (Federal Government Commissioner for Culture and the Media).

As part of the project, digital curating will be critically examined using various approaches of digital art. Experimenting with new digital aesthetics and forms of expression enables new museum experiences and thus new ways of museum communication and visitor participation. The museum is transformed to a place of experience and critical exchange.

![Logo](images/Logo_ZKM_DMN_KSB.png)

Supporters
----------

![FAU-USP](images/fauusp.jpg)
![C4Ai- INOVA-USP](images/center_for_artificial_intelligence.jpg)
![GAIA](images/out-gaia.jpg)

