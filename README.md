# Vegetable Classifier

### Motivation and Objective

This classifier is built to identify most vegetables using **Image Classification**.

This project was built after being inspired by Jeremy Howard in first 2 [video lectures]( https://course.fast.ai/videos/ ) on FastAI. 

The main objective of the project was to get a feel for the complete process of development and deployment of an Deep Learning Model.

This project has been deployed on [Render](vegecalssifier.onrendoer.com) following the official tutorial on the FastAI website. 

### Model Description

- This is a simple CNN model using the ResNet34 Architecture. This model can be found prebuilt in FastAI and can be imported directly.
  - The choice of ResNet was made as it is a good default Image Classifier. Used the weights of the model pre-trained on ImageNet, i.e. implemented Transfer Learning.
  - The 34 layer variant was chosen simply because the using a higher layer variant was too taxing on the resources and the 34 layer model was good enough to capture the differences in vegetables.
- Finetuning of hyper parameters was done based off the top-losses, and using the `lr_find()` function and the `lr recodered graph`.



### The complete process (start -> finish)

1. First, scraped [this](https://www.ranker.com/crowdranked-list/the-most-delicious-vegetables-v1 ) website to get a list of the popular vegetables, using _Regular Expressions_. The Python script is on [this file]( https://github.com/AceEV/VegetableClassifier/blob/master/util_files/get_vege_names.py ).
2. Then, I started collecting images to build the dataset. I used the `googleimagesearch` Python library to scrap images from Google of each vegetable.[[source\]]( https://github.com/AceEV/VegetableClassifier/blob/master/util_files/download_images_from_google.py )
   1. Used 50 images per vegetable as a rough start. On hindsight, going for much fewer, close to 25 _good_ images would have worked as well if not better, thanks to Data Augmentation.
   2. These images were put into a `downloads` folder, where each vegetable had its own folder, inside which the images were stored. These folder names act as the labels for the images.
3. I used Google Colab to work no this project this has a better compute power than my local machine. I imported the dataset pretty easily as `ImageDataBunches`.
4. Next, I built the `CNN_Learner` - ResNet34 Model with ImageNet weights and performed the few preliminary epochs to test out the learner and the dataset. My training stopped abruptly as some images were corrupted.
   1. Used the `verify_images()` function to clean the dataset and re-ran the learning.
5. Once, done, I plotted the top losses and found that a lot of the images were too vague. Example : images labelled as Avocado were in-fact guacamole, or images labeled as mushrooms were mushroom soup images :laughing:
   1. FastAI has a widget to help clean these images that allow you to delete these images -[image_clearner()]( https://docs.fast.ai/widgets.image_cleaner.html ) but unfortunately, widget do not seem to work on Google Colab, so I had to do the image cleaning task manually.
   2. The `image_cleaner()` does not actually delete the images in the dataset, rather creates a `cleaned.csv` file with the images that can be used in the dataset, and the once to be omitted do not have an entry in it. I decided to manually replicate this process and ended up removing around 400 images. I decided to still leave a few dirty images as a part of the understanding working of the CNN Models.
6. I got better results on this new dataset, both in training and validation dataset.
7. I then used methods like [lr_find()]( https://docs.fast.ai/basic_train.html#lr_find ) to find better Learning Rate and altered the batch_sizes to get a better accuracy.
8. On plotting top_losses, most fails happened due to the fact the some images had either off-center images, vegetables were shown shredded and looked similar even to the human eye etc. A lot of this can be attributed to the quality of the dataset. I tried having it predict some pictures I clicked from the local supermarket and it made good predictions.
9. I chose to stop the project here but I can very easily be improved, simply by training for more epochs, **cleaning the dataset** more(major cause) and adding small changes like tweaking the regularization etc.
10. I followed this [official documentation]( https://course.fast.ai/deployment_render.html ) to host the classifier as a WebApp. [Try it out :smile:](vegeclassifier.onrender.com)!

The main Notebook is [vege_classifier.ipynb]( https://github.com/AceEV/VegetableClassifier/blob/master/vegetable_classifier.ipynb ). I used a `vege_classifier_train.ipynb` to do some initial analysis.



### Future Improvements

- Adding Fruits to the mix
- Cleaning Dataset



Please reach out with any improvements, suggestions or queries:smiley:
