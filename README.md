This is a program that turns a input of anki subdeck names and ther overall structure into a set of anki deck names. For example, this:\
\
1	GCSE Science\
1.1	Chemistry\
1.1.1	Paper 1\
1.1.1.1	1 - Atomic structure and the periodic table\
1.1.1.1.1	1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes\
1.1.1.1.1.1	1 - Atoms, elements and compounds\
1.1.1.1.1.1	2 - Mixtures\
1.1.1.1.1.1	3 - The development of the model of the atom (common content with physics)\
1.1.1.1.1.1	4 - Relative electrical charges of subatomic particles\
1.1.1.1.1.1	5 - Size and mass of atoms\
1.1.1.1.1.1	6 - Relative atomic mass\
1.1.1.1.1.1	7 - Electronic structure\
1.1.1.1.1	2 - The periodic table\
1.1.1.1.1.2	1 - The periodic table\
1.1.1.1.1.2	2 - Development of the periodic table\
1.1.1.1.1.2	3 - Metals and non-metals\
1.1.1.1.1.2	4 - Group 0\
1.1.1.1.1.2	5 - Group 1\
1.1.1.1.1.2	6 - Group 7\
1.1.1.1.1	3 - Properties of transition metals (chemistry only)\
1.1.1.1.1.3	1 - Comparison with Group 1 elements\
1.1.1.1.1.3	2 - Typical properties\
1.1.1.1	2 - Bonding, structure, and the properties of matter\
1.1.1.1.2	1 - Chemical bonds, ionic, covalent and metallic\
1.1.1.1.2.1	1 - Chemical bonds\
1.1.1.1.2.1	2 - Ionic bonding\
1.1.1.1.2.1	3 - Ionic compounds\
1.1.1.1.2.1	4 - Covalent bonding\
1.1.1.1.2.1	5 - Metallic bonding\
1.1.1.1.2	2 - How bonding and structure are related to the properties of substances\
\
turns to this:\
\
GCSE Science\
GCSE Science::Chemistry\
GCSE Science::Chemistry::Paper 1\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::1 - Atoms, elements and compounds\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::2 - Mixtures\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::3 - The development of the model of the atom (common content with physics)\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::4 - Relative electrical charges of subatomic particles\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::5 - Size and mass of atoms\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::6 - Relative atomic mass\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::1 - A simple model of the atom, symbols, relative atomic mass, electronic charge and isotopes::7 - Electronic structure\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::1 - The periodic table\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::2 - Development of the periodic table\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::3 - Metals and non-metals\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::4 - Group 0\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::5 - Group 1\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::2 - The periodic table::6 - Group 7\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::3 - Properties of transition metals (chemistry only)\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::3 - Properties of transition metals (chemistry only)::1 - Comparison with Group 1 elements\
GCSE Science::Chemistry::Paper 1::1 - Atomic structure and the periodic table::3 - Properties of transition metals (chemistry only)::2 - Typical properties\
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter\
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic\
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::1 - Chemical bonds\
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::2 - Ionic bonding\
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::3 - Ionic compounds\
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::4 - Covalent bonding\
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::1 - Chemical bonds, ionic, covalent and metallic::5 - Metallic bonding\
GCSE Science::Chemistry::Paper 1::2 - Bonding, structure, and the properties of matter::2 - How bonding and structure are related to the properties of substances\
Example input and output files are given.\
This program required the input to be in the format {hierarchy level}{tab space}{(sub)deck name}\
