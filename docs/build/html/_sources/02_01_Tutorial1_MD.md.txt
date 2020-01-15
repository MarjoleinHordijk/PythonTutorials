# Tutorial 1 MD version
This guide will demonstrate how you can use Python in QGIS to load, filter and manipulate spatial data. You will learn where to find the Python console and how to write scripts in the editor. Also, you will use the console to filter data layers for specific field values or using expressions. Further, you will find out how to access QGIS’s library of geoprocessing tools from the Python console and how to chain these tools using scripting.

## Opening up the Python Console

You can open up the Python Console from the top menu of QGIS (Plugins > Python Console) or by pressing <code>Ctrl + Alt + P</code></strong>.

![Screenshot_2](uploads/cc96d1f2e4c89e498b692c33a2cbaa21/Screenshot_2.png)

This console is a so called “interactive command line interface”, which means we can use it to access the toolbox of QGIS through lines of codes. 

When you type a line of code and press <code>Enter</code></strong>, the code will be immediately executed. 

You can try this with a very simple and common example in programming tutorials.
Try the code below to print “hello world” in the console.

```
print("Hello world!")
```

You just called the print **function**, and provided “Hello world!” (a string of text) as a **parameter**, which should result in an output similar to that in the image below.

![Screenshot_3](uploads/ed478c683efa63c4a303df7ecc9ed9a7/Screenshot_3.png)

If you want to run a set of code lines (e.g. a small script), it may be easier to use the editor. To access the editor you can click the small notepad icon in the console window (highlighted in the picture below).

![Screenshot_5](uploads/8684fe6aa0a91b797580c9171338f63d/Screenshot_5.png)

When you create a script in the editor, you can conveniently save it for later use.
You can run the coding in the editor window by pressing the small green play icon.

## Loading a Vector Layer

Now that we know where to find the Python Console, we can start using it to load data into our project. That is, we will load a vector layer using the **iface.addVectorLayer** function.

You will need four layers for this exercise:



*   A point layer containing the location of the train station of Eindhoven.
*   A polyline layer with all roads in Eindhoven.
*   A polygon layer with containing buildings.
*   A polygon layer with the outline of Eindhoven.

Please locate the geopackage (.gpkg) files on your hard drive. You can view the location by right clicking the file as shown below.

![Screenshot_4](uploads/261e14995d44bb1a588dc15226fe95d5/Screenshot_4.png)

We can create variables to store the references to these locations. For example, if your roads.gpkg file is stored at “C:\Users\username\Desktop\Example\Roads.gpkg”, we can use the following code to store this location to the **variable** “RoadsPath” (but you can choose any variable name!). Please note that since we are working in Python, you <span style="text-decoration:underline;">have to use forward slashes!</span>


```
RoadsPath = "C:/Users/username/Desktop/Example/Roads.gpkg"
```


Next we can do the same for the other files that we will be using.


```
TrainstationPath = "C:/Users/username/Desktop/Example/Trainstation.gpkg"
BuildingsPath = "C:/Users/username/Desktop/Example/Buildings.gpkg"
EindhovenPath = "C:/Users/username/Desktop/Example/Eindhoven.gpkg"
```


We can now use the **iface.addVectorLayer** function to add these layers to our project as follows.


```
iface.addVectorLayer(RoadsPath, "Roads", "ogr")
iface.addVectorLayer(TrainstationPath, "Trainstation", "ogr")
iface.addVectorLayer(BuildingsPath, "Buildings", "ogr")
iface.addVectorLayer(EindhovenPath, "Eindhoven", "ogr")
```

After this, the four layers should be included in your QGIS project.
That is, you should be able to see them in the map canvas.

You can find more details on how this function works and what parameters it takes from the documentation of QGIS (see [here](https://qgis.org/pyqgis/master/gui/QgisInterface.html#qgis.gui.QgisInterface.addVectorLayer)) or in [this](https://anitagraser.com/pyqgis-101-introduction-to-qgis-python-programming-for-non-programmers/pyqgis-101-loading-a-vector-layer/) tutorial. 


## Viewing vector layer attributes

We can use the **iface.showAttributeTable()** function to access the information that is stored for each feature in our layers. For example, we can find out what type a particular road is (e.g. a highway).

To do so, we need to create variables which store a reference to each layer, as is done below.


```
Roads = iface.addVectorLayer(RoadsPath, "Roads", "ogr")
Trainstation = iface.addVectorLayer(TrainstationPath, "Trainstation", "ogr")
Buildings = iface.addVectorLayer(BuildingsPath, "Buildings", "ogr")
Eindhoven = iface.addVectorLayer(EindhovenPath, "Eindhoven", "ogr")
```


(As you may recognize, this piece of coding is very similar to when we were loading the layers.)

We can now open the attribute table of the Roads layer using the **iface.showAttributeTable()** function using the following code. Note that we provide “Roads” (the name of the variable we created) as **parameter** to this function.


```
iface.showAttributeTable(Roads)
```


However, instead of opening the attribute table (which we could have easily done through the user interface), we can also access specific information. For example, the Buildings layer contains information on the total footprint of each building in the “area” field. We can use the **print()** and **field()** functions to print these surface areas to the console. 

However, we do need to write a small **for loop** for this. This means that we will “loop” through each feature (building) in our layer, look up the value in the “area” field and print this to the console. 


```
for feature in Buildings.getFeatures():
    print(feature["Area"])
```


The output in your console should look something like this.

![Screenshot_6](uploads/dcaba15a71e66c782562f7929ea5b9e8/Screenshot_6.png)