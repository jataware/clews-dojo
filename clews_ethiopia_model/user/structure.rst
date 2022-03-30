===============
Model structure
===============

This section details the structure of the integrated CLEWS-Ethiopia model. 
It is divided into 3 sub-sections: energy, land-use, and water. Each sub-section provides
a snapshot of the underlying representation of the relevant sector in the CLEWS model. 

Below is a snapshot of the overall integrated structure of the model 

.. image:: /user/img/overall_structure.svg
   :class: with-shadow

Energy
======
The energy sector is represented by 
a set of input fuels (e.g. biomass, natural gas), 
transformation technologies (e.g. powerplants, electricity transmission), 
and sectoral demands (e.g. diesel in the agricultural sector, electricity in the industry sector). 
Below is a simplified schematic of the power sector representation in the model.

.. image:: /user/img/energy_sector.svg
   :class: with-shadow

Land-use
========

The land-use sector is represented as land allocated 
to 7 different uses/land cover types:

Agriculture, 
Barren land, 
Forests, 
Grassland & Woodland, 
Built-up land, 
Water bodies, 
and other land

Below is a schematic of the land-use sector representation in the CLEWS model.

.. image:: /user/img/land_use_overall.svg
   :class: with-shadow

Agriculture
-----------
* 43 technologies represent different crop combinations per region (e.g. LNDCP01NHR)
* 43 modes of operation (1 for each crop combination)
* 8 crop demands (at the national level)

.. image:: /user/img/land_use_basic.svg
   :class: with-shadow

Other land uses
---------------
6 additional technologies that represent other land uses:
* Barren land
* Forests
* Grasslands & woodland
* Built-up land
* Water bodies
* Other land

.. image:: /user/img/land_use_additional.svg
   :class: with-shadow

Water
=====

Agriculture
-----------

.. image:: /user/img/land_use_water.svg
   :class: with-shadow

Other land uses
---------------

.. image:: /user/img/land_use_additional_water.svg
   :class: with-shadow


