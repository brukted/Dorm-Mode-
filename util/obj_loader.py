def load_obj(content: str, swapyz = False):
    vertices = []
    uvs = []

    faces = []

    for line in content.split('\n'):
        if line.startswith('vt'):
            uv = list(map(float, line.split()[1:3]))
            uvs.append(uv)

        elif line.startswith('vn'):
            pass

        elif line.startswith('v'):
            vertex = list(map(float, line.split()[1:4]))
            if swapyz:
                vertex[1], vertex[2] = vertex[2], vertex[1]
            vertices.append(vertex)

        elif line.startswith('f'):
            t = line.split()[1:4]

            for ind in t:
                w = list(map(lambda x: int(x) - 1, ind.split('/')))
                if len(w) == 1:
                    x, y, z = vertices[w[0]].position
                    u, v = 0, 0

                    faces.append(u)
                    faces.append(v)
                    faces.append(x)
                    faces.append(y)
                    faces.append(z)
                else:
                    u, v = uvs[w[1]]
                    x, y, z = vertices[w[0]]

                    faces.append(u)
                    faces.append(v)
                    faces.append(x)
                    faces.append(y)
                    faces.append(z)

    return faces

