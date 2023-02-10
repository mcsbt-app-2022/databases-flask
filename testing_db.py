#%%

import sqlalchemy

engine = sqlalchemy.create_engine("sqlite:///paymepal.db")

with engine.connect() as connection:
    query = "SELECT * FROM transactions;"

    result = connection.execute(query)

    for row in result:
        print(row)

# %%
