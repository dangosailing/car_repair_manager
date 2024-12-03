### Activate venv on windows
.\venv\Scripts\activate

### Misc
Must remove the db file after modifications to tables/db etc before running main again

### Checklist
- Figure out way to make pattern serach possible on car make, model, year search without triggering incorrect binding error
- Add better handling of repair order customer_id/car_id input (maybe show list of available customers and cars with associated IDs?)
- Overall polish and refactorisation (can pattern searches for year/make/model be combined into overall int/string searches with the respective column names as a parameter?)