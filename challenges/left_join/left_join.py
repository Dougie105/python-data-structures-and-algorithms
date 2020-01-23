def left_join(map1,map2):

    output = []

    for key in map1:

        if key in map2:

            output.append([key,map1[key],map2[key]])

        else :
            output.append([key,map1[key],None])

    return output