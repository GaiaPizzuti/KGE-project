# Introduction
This repository contains the project created for the course "Knowledge Graph Engineering" at the University of Trento during the academic year 2024/2025, the title of the project is "International Digital University".
The project aims to create a knowledge graph that represents the collaborations between universities, in terms of projects, publications and staff. In order to achieve this goal the iTelos methodology has been used, which is a methodology divided in different phases whose result is the final knowledge graph.

# Phase 1
In the first phase different aspects of the project are defined:
- Informal Purpose
- Domain of Interest
- Scenarios
- Personas
- Competency Questions
- ER model

Some examples will be provided in the following subsections, a more comprehensive explanation of each element can be found in the PDF report.
## Personas 
The personas are the people who will use the knowledge graph, some examples are:
| Name | Age  | Role |
| :--- | :--- | :--- |
| Dr. Maria Rossi | 28 | Researcher at University of Trento|
| Prof. Bat Erdene | 41 | Senior Lecturer at National University of Mongolia|
## Competency Questions

Competency questions are used to define how the different personas will use the knowledge graph, some examples are:

| Personas                | Field                  | Question                                                     |
| ----------------------- | ---------------------- | ------------------------------------------------------------ |
| Maria Rossi, Bat Erdene | Research Collaboration | Who are the researchers from both universities that have worked together on a  specific project or paper? |
| Bat Erdene              | Researcher Information | Which students are pursuing a PhD in Computer Science?       |

## ER model

![er_updated.drawio](./Phase 4 - Knowledge Definition/er_updated_protege.drawio.svg)

# Phase 2

The second phase of the methodology is the **Information Gathering phase**, the objective of this phase is to collect the data needed to create the Knowledge Graph and answer the competency questions. The sources we used are:

- UNITN’s LiveData Platform
- UniTN's Website
- NUM's LiveData Platform

The LiveData Platforms provide high quality datasets which are suitable for the use in a Knowledge Graph, on the other hand the Website uses APIs to get information and show it to the user. In order to get a dataset out of the Website we used a python script to automatically access the APIs and extract the data. A complete list of the gathered datasets can be found in the [sources.md](https://github.com/GaiaPizzuti/KGE-project/blob/main/Phase%202%20-%20Information%20Gathering/sources.md) file.

# Phase 3

The third phase of the methodology is the **Language Definition phase**. During this phase, starting from the work performed during the first two phases, a formalized domain-specific language is created. Since the project handles data from both the University of Trento (located in Italy) and the National University of Mongolia (located in Mongolia) it was important to handle the language differences in the data. This was done thanks to the creation of a **Language Resource**. Moreover since the Mongolian language uses the Cyrillic alphabet, before translating these terms it was also necessary to transliterate the characters to the Latin alphabet, this was achieved by using the [cyrtranslit](https://pypi.org/project/cyrtranslit/) python library.

# Phase 4

The fourth phase of the methodology is the **Knowledge Definition phase**. This phase requires the modeling of the:

- **Ontology**: which is used to formalize the relationship between entities;
- **Teleology**: which gives a definition and a purpose to the entities;
- **Teleontology**: which is a combination of the **Ontology** and the **Teleology**. The advantage of the **Teleontology** is that it leverages the rigidity of the Ontology and the flexibility of the Teleology.

To create this elements the tool [Protége](https://protege.stanford.edu/) is used, in the following section some examples of the modeling created using this tool will be shown.

## Examples

![etypes](./Phase 4 - Knowledge Definition/etypes.png)

![data](./Phase 4 - Knowledge Definition/data.png)

## Teleontology visualization

The Teleontology was visualized using [WebVOWL](https://github.com/VisualDataWeb/WebVOWL)

![teleontology](./Phase 4 - Knowledge Definition/teleontology.png)
