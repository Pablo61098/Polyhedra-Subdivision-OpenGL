def calculate_new_vector(v1, v2, n_v, norm):
    vector = [(a + b)/2 for a, b in zip(v1, v2)]
    # try in case there is a normal of 0
    try:
        if(norm):
            normal = sum([x**2 for x in vector])**(1/2)

            vector = [x/(normal) for x in vector]

        n_v += 1
        # if(len(vector) == 3):
        #     pass
        return vector, n_v
    except:
        return [], n_v

def update_figure(v, indices, norm):

    salto = 0
    nuevo_vertice = int(len(v)/3)
    
    len_indices = int(len(indices)/3)

    indices_salida = []

    for i in range(len_indices):
        

        v1_indice = indices[3*i + 0]
        v2_indice = indices[3*i + 1]
        v3_indice = indices[3*i + 2]


        v1 = [v[v1_indice * 3 + 0], v[v1_indice * 3 + 1], v[v1_indice * 3 + 2]]
        v2 = [v[v2_indice * 3 + 0], v[v2_indice * 3 + 1], v[v2_indice * 3 + 2]]
        v3 = [v[v3_indice * 3 + 0], v[v3_indice * 3 + 1], v[v3_indice * 3 + 2]]
        

        v1_2, nuevo_vertice = calculate_new_vector(v1, v2, nuevo_vertice, norm)
        v2_3, nuevo_vertice = calculate_new_vector(v2, v3, nuevo_vertice, norm)
        v1_3, nuevo_vertice = calculate_new_vector(v1, v3, nuevo_vertice, norm)

        [v.append(a) for a in v1_2]
        [v.append(a) for a in v2_3]
        [v.append(a) for a in v1_3]
        
        
        indices_salida += [v1_indice, nuevo_vertice - (3), nuevo_vertice - (1)]
        indices_salida += [v2_indice, nuevo_vertice - (3), nuevo_vertice - (2)]
        indices_salida += [v3_indice, nuevo_vertice - (1), nuevo_vertice - (2)]
        indices_salida += [nuevo_vertice - (1), nuevo_vertice - (2), nuevo_vertice - (3)]


    
    return [v, indices_salida]

    

a = 0.525731112119133606
b = 0.850650808352039932

v = [-a, 0.0, b,
        a, 0.0, b,
        -a, 0.0, -b,
        a, 0.0, -b,
        0.0, b, a,
        0.0, b, -a,
        0.0,-b, a,
        0.0, -b, -a,
        b, a, 0.0,
        -b, a, 0.0,
        b, -a, 0.0,
        -b, -a, 0.0
    ]


indices = [0,1,4,
            0,4,9,
            9,4,5,
            4,8,5,
            4,1,8,
            8,1,10,
            8,10,3,
            5,8,3,
            5,3,2,
            2,3,7,
            7,3,10,
            7,10,6,
            7,6,11,
            11,6,0,
            0,6,1,
            6,10,1,
            9,11,0,
            9,2,11,
            9,5,2,
            7,11,2
    ]

# v, indices = update_figure(v, indices)