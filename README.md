
<h1>Polyhedra Subdivision with OpenGL</h1>
 
This code show the aproximation of a polyhedron to an sphere by using iterative subdivision. 
Parameters of what figure shows up and if the approximation to an sphere is needed can be changed.

To execute this script you need to install

- glfw
- pyopengl
- pyrr
- pillow
- numpy

You can do this with:
    
    pip3 install glfw
    pip3 isntall pyopengl
    pip3 install pyrr
    pip3 install pillow
    pip3 install numpy

Note: you may need to use `pip3` instead `pip`.

The default figure to show is an octahedron, and it is applying the normalization method to approximate it to an sphere. 

You can change the figure with the following parameter at the time of execution:

    python3 polyhedra_subdivision.py --poly_type x
    
With x replace with any of this:
    box
    ico
    oc
    tri

Also, you can switch off the approximation to an sphere with the --no_norm parameter, so:

    python3 polyhedra_subdivision.py --poly_type box --no-norm
    

An example of the result is.

![Screenshot_20210504_022502](https://user-images.githubusercontent.com/37944675/121181832-0b5fb200-c828-11eb-9630-bb9ae6e4595f.png)


![Screenshot_20210504_022525](https://user-images.githubusercontent.com/37944675/121181848-0ef33900-c828-11eb-92f2-2c61bcae1f2f.png)


![Screenshot_20210504_022552](https://user-images.githubusercontent.com/37944675/121181855-11ee2980-c828-11eb-96ae-39a4c36ea8ce.png)








