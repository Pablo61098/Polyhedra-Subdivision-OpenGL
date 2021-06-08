
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

![Screenshot_20210608_070833](https://user-images.githubusercontent.com/37944675/121182223-7b6e3800-c828-11eb-9b5f-783d743e5f3a.png)

![Screenshot_20210608_070839](https://user-images.githubusercontent.com/37944675/121182249-81fcaf80-c828-11eb-8b17-c0612b6e1afd.png)

![Screenshot_20210608_070859](https://user-images.githubusercontent.com/37944675/121182254-82954600-c828-11eb-8ad2-6aaf0395f031.png)







