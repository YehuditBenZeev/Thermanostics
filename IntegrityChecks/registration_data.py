import numpy as np

# put 9 palm points from 1 to 9
LB_514 = np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]])  ###
LF_514 = np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]])  ###
RB_514 = np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]])  ###
RF_514 = np.float64([[[470, 276], [452, 146], [386, 90], [320, 114], [280, 134], [230, 130], [216, 230], [262, 310], [342, 316]]])


images_514 = {
            '../514 images/514 RF dark.bmp': np.float64([[[470, 276], [452, 146], [386, 90], [320, 114], [280, 134], [230, 130], [216, 230], [262, 310], [342, 316]]]),
            '../514 images/514 RF flip.bmp': np.float64([[[54, 273], [76, 141], [132, 95], [202, 115], [242, 128], [300, 132],[310, 232], [260, 308], [188, 316]]]),
            '../514 images/514 RF HN.bmp': np.float64([[[399, 250], [383, 123], [333, 80], [273, 102], [239, 114], [203, 118], [18, 208], [227, 278], [293, 282]]]),
            '../514 images/514 RF HW.bmp': np.float64([[[539, 275], [511, 132], [437, 79], [367, 111], [325, 127], [269, 131], [249, 231, [307, 311], [391, 313]]]]),
            '../514 images/514 RF light.bmp': np.float64([[[470, 276], [452, 146], [386, 90], [320, 114], [280, 134], [230, 130], [216, 230], [262, 310], [342, 316]]]),
            '../514 images/514 RF move down.bmp': np.float64([[[456, 275], [432, 139], [368, 83], [309, 115], [265, 129], [217, 131], [199, 231], [247, 309], [329, 313]]]),
            '../514 images/514 RF no arm.bmp': np.float64([[[467, 259], [447, 123], [383, 65], [321, 99], [277, 113], [484, 312], [215, 213], [267, 295], [349, 297]]]),
            '../514 images/514 RF -r.bmp': np.float64([[[464, 220], [434, 90], [362, 42], [298, 76], [258, 94], [216, 102], [208, 202], [262, 278], [34, 22]]]),
            '../514 images/514 RF rotate 25.bmp': np.float64([[[490, 176], [412, 66], [334, 44], [284, 98], [256, 124], [214, 148], [238, 246], [320, 296], [394, 264]]]),
            '../514 images/514 RF s.bmp': np.float64([[[235, 138], [226, 73], [193, 45], [160, 57], [140, 68], [115, 65], [108, 115], [131, 155], [171, 158]]]),
            '../514 images/514 RF VN.bmp': np.float64([[[472, 248], [448, 126], [384, 72], [320, 102], [280, 116], [234, 117], [214, 208], [266, 280], [346, 282]]]),
            '../514 images/514 RF VW.bmp': np.float64([[[470, 298], [448, 150], [382, 84], [320, 124], [282, 140], [232, 140], [216, 250], [266, 336], [348, 338]]]),
            '../514 images/514 RF w.bmp': np.float64([[[474, 275], [456, 141], [378, 77], [320, 115], [280, 129], [236, 131], [216, 231], [268, 311], [348, 313]]])
}

images = {
            '../images/509 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/509 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/509 LB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/509 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/511 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/511 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/511 LB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/511 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/512 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/512 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/512 LB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/512 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/513 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/513 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/513 LB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/513 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/515 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/515 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/515 LB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/515 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/516 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/516 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/516 LB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/516 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/517 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/517 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/517 LB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/517 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]])
}
