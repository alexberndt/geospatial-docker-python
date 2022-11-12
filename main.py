import rasterio

from geo_analysis.core import core_function

def main() -> None:
    print("hello mah boi!")
    print(f"Core function: {core_function()}")
    print(rasterio.__version__)

if __name__ == "__main__":
    main()
