"""
Test für den Download eines Produktbildes.
"""

from services.image_service import ImageService


def main():

    gtin = "3017620422003"

    service = ImageService()

    image_path = service.download_image(
        gtin,
    )

    print()

    if image_path is None:

        print("Kein Bild gefunden.")

    else:

        print("Bild gespeichert:")

        print(image_path)

    print()


if __name__ == "__main__":

    main()