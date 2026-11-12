import re
import pandas as pd

text = """Addressing the Long-Term Effects of the COVID-19 Pandemic on Children and Families National Academies of Sciences, Engineering, and Medicine. 2023. 

Addressing the Long-Term Effects of the COVID-19 Pandemic on Children and Families. Washington, DC: The National Academies Press. Tumaini Rucker Coker, Jennifer Appleton
Gootman, and Emily P. Backes, Editors

Committee on Addressing the Long-Term
Impact of the COVID-19 Pandemic on
Children and Families

Board on Children, Youth, and Families

Division of Behavioral and Social Sciences
and Education
National Academies of Sciences, Engineering, and Medicine. 2023. Addressing the Long-Term Effects of the COVID-19 Pandemic on Children and Families. Washington, DC: The National Academies Press. 

NATIONAL ACADEMIES PRESS 500 Fifth Street, NW Washington, DC 20001

This activity was supported by contracts between the National Academy of Sciences and the Administration for Children and Families, a division of the U.S. Department of Health and Human Services, (#75N98021C00032) and the Robert Wood Johnson Foundation (#78561). Any opinions, findings, conclusions, or recommendations expressed in this publication do not necessarily reflect the views of any organization or agency that provided support for the project.

International Standard Book Number-13: 978-0-309-69695-1
International Standard Book Number-10: 0-309-69695-X
Digital Object Identifier: https://doi.org/10.17226/26809
Library of Congress Control Number: 2023939024

This publication is available from the National Academies Press, 500 Fifth Street, NW, Keck 360, Washington, DC 20001; (800) 624-6242 or (202) 334-3313; http://www.nap.edu.

Copyright 2023 by the National Academy of Sciences. National Academies of Sciences,
National Academies of Sciences, Engineering, and Medicine. 2023. Addressing the Long-Term Effects of the COVID-19 Pandemic on Children and Families. Washington, DC: The National Academies Press. https://doi.org/10.17226/26809.

Engineering, and Medicine and National Academies Press and the graphical logos for each are all trademarks of the National Academy of Sciences. All rights reserved.

Printed in the United States of America.

Suggested citation: National Academies of Sciences, Engineering, and Medicine. 2023. Addressing the Long-Term Effects of the COVID-19 Pandemic on Children and Families. Washington, DC: The National Academies Press. https://doi.org/10.17226/26809.
National Academies of Sciences, Engineering, and Medicine. 2023. Addressing the Long-Term Effects of the COVID-19 Pandemic on Children and Families. Washington, DC: The National Academies Press. https://doi.org/10.17226/26809.

"""

words = re.sub(r"[^\w\s]", "", text.lower()).split()
word_series = pd.Series(words)
counts = word_series.value_counts()
frequencies = word_series.value_counts(normalize=True)

df = pd.DataFrame(
    {"Count": counts, "Frequency (Relative)": frequencies}
)

df.index.name = "Word"
df = df.reset_index()

print(df.head(10))