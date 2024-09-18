# Anki deck tools

In this is a set of programs that aids with anki, a spaced repetirion flascard program's usage.

---

## Program 1: Deck generator.py

This is a program that turns a input of anki subdeck names and ther overall structure into a set of anki deck names. For example, this:

```
1 GCSE Science
1.1 Chemistry
1.1.1 Paper 1
1.1.1.1 1 - Atomic structure and the periodic table
1.1.1.1.1 1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes
1.1.1.1.1.1 1 - Atoms, elements and compounds
1.1.1.1.1.1 2 - Mixtures
1.1.1.1.1.1 3 - The development of the model of the atom (common content with physics)
1.1.1.1.1.1 4 - Relative electrical charges of subatomic particles
1.1.1.1.1.1 5 - Size and mass of atoms
1.1.1.1.1.1 6 - Relative atomic mass
1.1.1.1.1.1 7 - Electronic structure
1.1.1.1.1 2 - The periodic table
1.1.1.1.1.2 1 - The periodic table
1.1.1.1.1.2 2 - Development of the periodic table
1.1.1.1.1.2 3 - Metals and non-metals
1.1.1.1.1.2 4 - Group 0
1.1.1.1.1.2 5 - Group 1
1.1.1.1.1.2 6 - Group 7
1.1.1.1.1 3 - Properties of transition metals (chemistry only)
1.1.1.1.1.3 1 - Comparison with Group 1 elements
1.1.1.1.1.3 2 - Typical properties
1.1.1.1 2 - Bonding, structure, and the properties of matter
1.1.1.1.2 1 - Chemical bonds, ionic, covalent and metallic
1.1.1.1.2.1 1 - Chemical bonds
1.1.1.1.2.1 2 - Ionic bonding
1.1.1.1.2.1 3 - Ionic compounds
1.1.1.1.2.1 4 - Covalent bonding
1.1.1.1.2.1 5 - Metallic bonding
1.1.1.1.2 2 - How bonding and structure are related to the properties of substances
```

turns to this:

```
GCSE Science
GCSE Science::Chemistry
GCSE Science::Chemistry::Paper 1
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::1 - Atoms, elements and compounds
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::2 - Mixtures
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::3 - The development of the model of the atom (common content with physics)
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::4 - Relative electrical charges of subatomic particles
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::5 - Size and mass of atoms
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::6 - Relative atomic mass
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::7 - Electronic structure
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::1 - The periodic table
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::2 - Development of the periodic table
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::3 - Metals and non-metals
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::4 - Group 0
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::5 - Group 1
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::6 - Group 7
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::3 - Properties of transition metals (chemistry only)
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::3 - Properties of transition metals (chemistry only)::1 - Comparison with Group 1 elements
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::3 - Properties of transition metals (chemistry only)::2 - Typical properties
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::1 - Chemical bonds
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::2 - Ionic bonding
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::3 - Ionic compounds
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::4 - Covalent bonding
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::5 - Metallic bonding
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::2 - How bonding and structure are related to the properties of substances

```

Example input (raw deck names.txt) and output (anki decks and subdeck names) files are given.
This program required the input to be in the format {hierarchy level}{tab space}{(sub)deck name}

---

## Program 2: deck-name-prep.py

This program takes an input that you would normally get from directly copying an edexcel specification like:

```
4.5.1


Public expenditure

4.5.2


Taxation

4.5.3
Public sector finances

4.5.4
Macroeconomic policies in a global context

```

containing whitespace charecters at ends of lines and uneven spacing between number-dot identifiers and deck names into something cleaner like:

```
1.2.4.5.1 1 - Public expenditure
1.2.4.5.2 2 - Taxation
1.2.4.5.3 3 - Public sector finances
1.2.4.5.4 4 - Macroeconomic policies in a global context
```

It is highly customisable, making importing specifications into spaced repetition software easier

---

## Program 3: folder-from-decks.py

This program takes the output from program 2 and uses it to create a set of local directories for easy local note categroisation. For example, it turns this:

```
1.1 Microeconomics
1.1.1 1 - Introduction to markets and market failures
1.1.1.1 1 - Nature of economics
1.1.1.1.1 1 - Economics as a social science
1.1.1.1.2 2 - Positive and normative economic statements
1.1.1.1.3 3 - The economic problem
1.1.1.1.4 4 - Production possibility frontiers
1.1.1.1.5 5 - Specialisation and the division of labour
1.1.1.1.6 6 - Free market economies, mixed economy and command economy
1.1.1.2 2 - How markets work
1.1.1.2.1 1 - Rational decision making
```

Into a directory structure like this, providing similiar visuals in safe mode:

```
└── Economics
    ├── Microeconomics
        ├── Introduction to markets and market failures
            ├── Nature of economics
                ├── Economics as a social science
                ├── Positive and normative economic statements
                ├── The economic problem
                ├── Production possibility frontiers
                ├── Specialisation and the division of labour
                ├── Free market economies, mixed economy and command economy
            ├── How markets work
                ├── Rational decision making
```

**Warning: programs have hardcoded file input positions of which some are not present in this repo. When running programs, be careful to ensure that files aren't taken/ put into random places**
