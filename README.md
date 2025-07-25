Notes
-----

ROCm installation:
```
pip install --ignore-installed torch --index-url https://download.pytorch.org/whl/rocm6.1

HSA_OVERRIDE_GFX_VERSION=10.3.0 python main.py classifier -t
```

To run the application it is necessary to copy `example.config.py` and rename it to `config.py`.

The work which is supposed to be done is defined in `main.py` with explicit mention of generator functions.

The ontology has several versions:
1. Raw version without interface to interact (without class restrictions and with messy object properties),
1. Same version with interface,
1. New version of ontology (`ontology2`) which has class restrictions, less amount of object properties and more meaningful ones.

- The `ontology` folder contains ontology scheme and interface,
- The `ontology2` folder contains ontology2 scheme and interface,
- The `queries` folder in `ontology` and `ontology2` contains queries` definitioins,
- The `resources` folder contains query results, datasets, generated ontologies.
- The `annotations_builder` folder contains algorithms for ontology creation with provided annotations,
- The `classifier_builder` folder contains algorithms for automatic ontology creation,
- The `manual_builder` folder in `ontology` and `ontology2` contains manually created ontologies,
- The `docs` folder contains documentation for the ontology.


Health care applications
------------------------

Device|Application|Policy link|Device link
------|-----------|-----------|-----------
CareSens N Plus Bluetooth Blood Glucose Monitor Kit|CareSense|https://www.caresense.com/privacypolicy|https://www.amazon.com/CareSens-Bluetooth-Diabetes-Monitoring-Coding/dp/B08B86TM6R/ref=sr_1_1?crid=3SCEBW1XS8LRY&keywords=smart+glucometer&qid=1674337696&sprefix=smart+glucometer%2Caps%2C244&sr=8-1 
DARIO Blood Glucose Monitor Kit|Dario Health|https://mydario.com/privacy-policy/|https://www.amazon.com/Dario-Glucose-Diabetes-Testing-Disposable/dp/B07G3BNXR6/ref=sr_1_2?crid=3SCEBW1XS8LRY&keywords=smart+glucometer&qid=1674337696&sprefix=smart+glucometer%2Caps%2C244&sr=8-2 
Amazfit Band 5 Activity Fitness Tracker|Zepp (formerly Amazfit)|https://upload-cdn.huami.com/tposts/8191|https://www.amazon.com/Amazfit-Fitness-Monitoring-Tracking-Resistant/dp/B08DKYLK4D/ref=sr_1_1?crid=1UR7G6LWBRWTH&keywords=fitness%2Btracker&qid=1674337956&sprefix=fitness%2Btracke%2Caps%2C204&sr=8-1&th=1 
RENPHO Smart Scale for Body Weight|Renpho|https://renpho.com/pages/renpho-privacy-policy|https://www.amazon.com/RENPHO-Bluetooth-Bathroom-Composition-Smartphone/dp/B01N1UX8RW/ref=sr_1_1?crid=35N1TK1ULC5HM&keywords=smart%2Bweights&qid=1674338323&sprefix=smart%2Bweight%2Caps%2C309&sr=8-1&th=1


Cites
-----

This ontology constructor uses dataset iot-dataset and OPP-115 (which is cited below):

*Wilson S., Schaub F., Dara A., et al. The Creation and Analysis of a Website Privacy 
Policy Corpus. // Proceedings of the 54th Annual Meeting of the Association for 
Computational Linguistics. – Berlin, Germany, 2016. – pp. 1330-1340.*
