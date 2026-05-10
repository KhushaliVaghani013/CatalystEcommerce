from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import get_db, engine

# ✅ Create FastAPI instance named 'app'
app = FastAPI(title="Catalyst API")

# ✅ THIS LINE WAS MISSING - creates all tables on startup
Base.metadata.create_all(bind=engine)


@app.post("/products")
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):

    new_product = models.Product(
        name=product.name,
        description=product.description,
        price=product.price,
        image=product.image
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product


# =============================
# GET PRODUCTS
# =============================

@app.get("/products")
def get_products(db: Session = Depends(get_db)):

    products = db.query(models.Product).all()

    return products


# =============================
# PLACE ORDER
# =============================

@app.post("/orders/{user_id}")
def place_order(
    user_id: int,
    order: schemas.OrderCreate,
    db: Session = Depends(get_db)
):

    user = db.query(models.User).filter(
        models.User.id == user_id
    ).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    new_order = models.Order(
        user_id=user_id,
        total_amount=order.total_amount,
        status="Placed"
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {
        "message": "Order placed successfully",
        "order_id": new_order.id
    }