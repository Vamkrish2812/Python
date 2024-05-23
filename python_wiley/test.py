from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, MetaData, Table, Column, String, Numeric, DateTime
from sqlalchemy.orm import sessionmaker
import datetime

app = FastAPI()

# Assuming convert_crypto function is defined elsewhere and correctly returns a dictionary with 'converted_price'

@app.get("/add_crypto_to_orderbook")
async def add_crypto_to_orderbook(symbol: str) -> dict:
    """
    Coded by: Vamsi Krishna
    This endpoint uses the `convert_crypto` function to get the price of a cryptocurrency
    and inserts that currency and price into the orderbook database.
    """
    try:
        # Call the convert_crypto function to get the price of the cryptocurrency
        crypto_price = await convert_crypto(symbol, "USD")  # Assuming we want the price in USD
    except Exception as e:
        print(f"Error converting crypto: {e}")
        raise HTTPException(status_code=500, detail="Error converting cryptocurrency")

    # Database connection string
    db_url = 'mysql+pymysql://wiley:wiley123@orderbookdb/orderbook'
    
    try:
        # Connect to the database
        engine = create_engine(db_url)
        metadata = MetaData()
        
        # Define the Product table
        product_table = Table('Product', metadata,
            Column('symbol', String(16), primary_key=True),
            Column('price', Numeric(precision=15, scale=2)),
            Column('productType', String(12)),
            Column('name', String(128)),
            Column('lastUpdate', DateTime)
        )
        
        # Create the table if it doesn't exist
        metadata.create_all(engine)
        
        # Create a new session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        try:
            # Insert the new cryptocurrency into the database
            session.execute(product_table.insert().values(
                symbol=symbol, 
                price=crypto_price['converted_price'], 
                productType='crypto', 
                name=symbol, 
                lastUpdate=datetime.datetime.now()
            ))
            session.commit()
            return {"insert_report": "success", "symbol": symbol, "price": crypto_price['converted_price']}
        except Exception as e:
            session.rollback()
            print(f"Error inserting into database: {e}")
            raise HTTPException(status_code=400, detail="An error occurred while inserting the cryptocurrency")
        finally:
            session.close()
    except Exception as e:
        print(f"Database connection error: {e}")
        raise HTTPException(status_code=500, detail="Database connection error")
