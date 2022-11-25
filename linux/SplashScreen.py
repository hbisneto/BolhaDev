## SplashScreen File
## This file contains information about your project

from datetime import date

CurrentYear = date.today().year
SoftwareName = "BolhaDev"
Version = "1.0"
CopyrightName = "Bisneto"

print("Name:", SoftwareName)
print("Version:", Version)
print("Created By:", CopyrightName)

if CurrentYear == 2022:
   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")
else:
   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")

print("="*80)
print(f'[{SoftwareName} for Linux] - Running...')
print("="*80)
print()
