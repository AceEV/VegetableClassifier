from util_files.get_vege_names import get_vegetables
from util_files.download_images_from_google import download_images

if __name__ == '__main__':
    # vegetables = get_vegetables('page.txt')
    # download_images(vegetables[:50], num=50)
    specific_vegetables = ["Cauliflower", "Olives", "Kale", "Ginger", "Squash", "Turnip", "Arugula"]
    if len(specific_vegetables) > 0 : download_images(specific_vegetables, num=50)

    print("\n\n")
    print("*"*50)
    print("DONE. Dataset Prepared.")
    print("*"*50)