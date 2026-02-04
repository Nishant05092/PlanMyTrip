import csv
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.places import Place


def ingest_csv(db: Session, file_path: str):
    # 🔒 Prevent duplicate ingestion
    already_exists = db.query(Place).first()
    if already_exists:
        print("📌 Places already exist. Skipping CSV ingestion.")
        return

    try:
        with open(file_path, "r", encoding="utf-8") as csvfile:
            csvreader = csv.DictReader(csvfile)

            places = []

            for row in csvreader:
                place = Place(
                    zone=row.get("Zone"),
                    state=row.get("State"),
                    city=row.get("City"),
                    name=row.get("Name"),
                    type=row.get("Type"),
                    establishment_year=(
                        str(row.get("Establishment Year"))
                        if row.get("Establishment Year")
                        else None
                    ),
                    time_needed=(
                        float(row.get("time needed to visit in hrs"))
                        if row.get("time needed to visit in hrs")
                        else None
                    ),
                    google_rating=(
                        float(row.get("Google review rating"))
                        if row.get("Google review rating")
                        else None
                    ),
                    entrance_fee=(
                        float(row.get("Entrance Fee in INR"))
                        if row.get("Entrance Fee in INR")
                        else None
                    ),
                    airport_nearby=row.get("Airport with 50km Radius"),
                    weekly_off=row.get("Weekly Off"),
                    significance=row.get("Significance"),
                    dslr_allowed=row.get("DSLR Allowed"),
                    num_reviews=(
                        float(row.get("Number of google review in lakhs"))
                        if row.get("Number of google review in lakhs")
                        else None
                    ),
                    best_time=row.get("Best Time to visit"),
                )

                places.append(place)

            # 🚀 Bulk insert (FASTER on PostgreSQL)
            db.bulk_save_objects(places)
            db.commit()

            print(f"✅ Successfully ingested {len(places)} places")

    except IntegrityError:
        db.rollback()
        print("❌ Integrity error while ingesting CSV")

    except Exception as e:
        db.rollback()
        print(f"❌ Error ingesting CSV: {e}")
