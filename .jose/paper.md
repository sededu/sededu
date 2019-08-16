---
title: 'SedEdu: a suite of sediment-related educational modules'
tags:
- Python
- geology
- sedimentology
- hydrology
authors:
- name: Andrew J. Moodie
  orcid: 0000-0002-6745-036X
  affiliation: 1
- name: Brandee Carlson
  affiliation: 1
- name: Brady Z. Foreman
  orcid: 0000-0002-4168-0618
  affiliation: 2
- name: Jeffrey Kwang
  affiliation: "3, 4"
- name: Kensuke Naito
  orcid: 0000-0001-8683-0846
  affiliation: "3, 5"
- name: Jeffrey A. Nittrouer
  orcid: 0000-0002-4762-0157
  affiliation: 1
affiliations:
- name: Rice University (Houston, TX, USA)
  index: 1
- name: Western Washington University (Bellingham, WA, USA)
  index: 2
- name: University of Illinois at Urbana-Champaign (Urbana, IL, USA)
  index: 3
- name: now at University of Massachusetts Amherst (Amherst, MA, USA)
  index: 4
- name: now at Universidad de Ingeniería y Tecnología (Lima, Peru)
  index: 5
date: 17 July 2019
bibliography: paper.bib
---

# Summary
SedEdu is a suite of computer-based interactive educational activities for sedimentology and stratigraphy courses.
SedEdu comprises modules which are coupled with activities that guide students through a concept, incrementally introducing components of the concept, and testing for understanding and retention throughout the activity.
The modules are computational and quantitative, but the code is abstracted through a graphical user interface (GUI), through which the user interacts with aspects of the computational model.
This paper describes the high level functionality of the SedEdu software package, includes a statement of need for this software package, and provides a brief example of how a module has been integrated into a classroom.

![SedEdu main screen and category page.](figures/sededu_main_and_category.png)

The SedEdu framework organizes modules into five categories (Figure 1, left): "Rivers and deltas", "Landscapes", "Deserts", "Coasts", and "Stratigraphy".
Clicking on a category button brings the user to that category page, where the available modules (and associated metadata and activities) are listed (Figure 1, right).
Pressing the button "Run module" will launch the module selected, and "Open activity" will open the activity on the users computer (typically a `.pdf` file).

SedEdu itself is a framework that packages and delivers content, with the goal of making it convenient for users to install, access, and interact with the software. 
To this end, SedEdu is free, platform-agnostic, fully open source, and available from common software repositories (e.g., `pip`, `conda`).
Modules rely on existing Python libraries, which minimizes the burden of development and maintenance for SedEdu contributors. 
SedEdu is modular: modules are developed and maintained by individuals, and are only collated into the framework during building for a new release.
The SedEdu framework is independent of the underlying content material, such that the framework could be adapted (i.e., forked) for use in other fields or communities.
The SedEdu software framework was developed by Andrew J. Moodie, and modules and/or activities have been contributed by Brandee Carlson, Brady Foreman, Andrew Moodie, Kensuke Naito, Jeffrey Kwang, and Jeffrey Nittrouer; there are 7 modules and 7 activities/worksheets in the (current) version v1.1.6, and SedEdu is actively seeking developers of modules and activities.


# Statement of need
Active learning strategies improve student exam performance, engagement, attitudes, thinking, writing, self-reported participation and interest, help students become better acquainted with one another, and reduce the achievement gap that exists between underrepresented minority (URM) students and non-URM students [@prince_does_2004; @haak_increased_2011]. 
Active learning is broadly considered any strategy that breaks up traditional lecture-format teaching with engaging activities that focus on developing students' higher-order cognitive skills [@haak_increased_2011; @karahoca_computer_2010].
Ideal active learning strategies minimize financial thresholds for entry and maximize availability [@tekian_review_2004; @haak_increased_2011].
Thus, on-line and computer-based learning coupled with in-person lessons, called "blended learning", is a promising avenue to integrate active learning into the classroom [@garrison_blended_2004].

Research and education integration is a core strategy in the U.S.A. National Science Foundation program design [@nsf_merit_2002], so grant writers frequently develop active learning strategies as part of their broader research impacts.
When developed, these active learning materials are often ineffectively disseminated, and so they are underutilized.
SedEdu offers a framework to organize these activities in one place, thereby increasing availability and utilization of externally-funded active learning materials.

SedEdu provides an active learning tool which can be readily integrated into classrooms.
SedEdu is great for educators because it provides high-quality active learning materials to the educators to easily bring into their classrooms, and provides an alternative non-traditional method for educators working under universal design for instruction principles [@scott_universal_2003].
SedEdu is great for researchers because it provides a tractable pathway for broader research impacts, and developing activities for computer-based active learning takes advantage of existing knowledge and skills they are likely to already have.


# Using SedEdu in the classroom
*rivers2stratigraphy* (*r2s*, Figure 2) is an example of a SedEdu module that illustrates basin-scale development of fluvial (i.e., river) stratigraphy via a real-time, rules-based model.
The model simplifies a real-world system so to run efficiently, and yet produces realistic stratigraphic patterns. 
In the module GUI, the students may change system parameters that represent the types of boundary conditions interpreted by geologists when evaluating the rock record (e.g., channel water discharge, avulsion timescale, and basin subsidence rates). 
Thus, hypotheses regarding how certain conditions influence stratigraphic patterns over time and space can be sequentially tested. 

![*rivers2stratigraphy* module after adjusting the subsidence rate of the basin to produce variable channel stacking patterns over the stratigraphic height. Color of channels indicates subsidence rate while that channel-body was deposited (purple$\rightarrow$yellow for slow$\rightarrow$fast).](figures/rivers2stratigraphy_demo.png){width=400px}

This interactive approach improves on traditional static instruction methods taught in laboratories, wherein students are provided an outcrop photograph and asked to measure properties including channel stacking, sand-body thickness, and cross-cutting relationships. 
In these situations, interpretations are subjective and typically vary; moreover, this style requires spatial abstraction and visualization skills, even before students learn about how dynamic boundary conditions and various geological processes impact stratigraphic patterns. 
However, in the SedEdu *r2s* module, these hurdles are eliminated because the students interact in real-time with the key boundary conditions, evaluating how stratigraphy is influenced, which enables students to more quickly and efficiently learn.


# References
