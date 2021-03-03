import numpy as np

# put 9 palm points from 1 to 9
image_ref = {
    'LB_514': np.float64([[[547, 299], [490, 158], [385, 81], [339, 122], [301, 142], [260, 141], [243, 241], [295, 316], [367, 316]]]),
    'LF_514': np.float64([[[479,114], [453,251], [369,304], [314,260], [267,241],[223,233],[214,142],[285,54],[386,72]]]),
    'RB_514': np.float64([[[456,58], [477,199], [385,269], [338,231], [306,215],[257,217],[253,115],[283,42],[353,36]]]),
    'RF_514': np.float64([[[470, 276], [452, 146], [386, 90], [320, 114], [280, 134], [230, 130], [216, 230], [262, 310], [342, 316]]])
}

images_514 = {
            '../514 images/514 RF dark.bmp': np.float64([[[470, 276], [452, 146], [386, 90], [320, 114], [280, 134], [230, 130], [216, 230], [262, 310], [342, 316]]]),
            '../514 images/514 RF flip.bmp': np.float64([[[54, 273], [76, 141], [132, 95], [202, 115], [242, 128], [300, 132],[310, 232], [260, 308], [188, 316]]]),
            '../514 images/514 RF HN.bmp': np.float64([[[399, 250], [383, 123], [333, 80], [273, 102], [239, 114], [203, 118], [18, 208], [227, 278], [293, 282]]]),
            '../514 images/514 RF HW.bmp': np.float64([[[539, 275], [511, 132], [437, 79], [367, 111], [325, 127], [269, 131], [249, 231], [307, 311], [391, 313]]]),
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
            '../images/509 RF.bmp': np.float64([[[478, 252], [428, 122], [380, 86], [314, 116], [274, 132], [232, 134], [226, 226], [286, 296], [364, 290]]]),
            '../images/509 RB.bmp': np.float64([[[412, 64], [456, 200], [392, 254], [324, 236], [278, 228], [238, 228], [216, 132], [282, 54], [324, 60]]]),
            '../images/509 LB.bmp': np.float64([[[504, 308], [504, 162], [444, 106], [384, 134], [302, 138], [344, 144], [274, 230], [340, 320], [384, 314]]]),
            '../images/509 LF.bmp': np.float64([[[504, 109], [484, 247], [446, 287], [376, 267], [334, 257], [296, 255], [272, 167], [342, 83], [400, 87]]]),
            '../images/511 RF.bmp': np.float64([[[463, 223], [455, 87], [384,40], [332,75], [286,82],[246,83],[244,171],[296,249],[370,242]]]),
            '../images/511 RB.bmp': np.float64([[[419,65], [430,190], [355,240], [307,215], [259,189],[219,187],[223,91],[279,21],[335,35]]]),
            '../images/511 LB.bmp': np.float64([[[366,314], [417,179], [340,107], [296,133], [271,141],[248,154],[212,253],[244,330],[302,328]]]),
            '../images/511 LF.bmp': np.float64([[[479,121], [454,255], [391,299], [323,269], [291,256],[254,251],[252,158],[299,83],[380,84]]]),
            '../images/512 RF.bmp': np.float64([[[547,267], [451,138], [365,68], [302,99], [261,114],[220,116],[219,220],[282,300],[375,295]]]),
            '../images/512 RB.bmp': np.float64([[[423,108], [451,243], [332,310], [268,275], [233,262],[205,255],[196,148],[273,70],[345,85]]]),
            '../images/512 LB.bmp': np.float64([[[350,327], [415,192], [363,104], [293,121], [258,126],[218,113],[168,213],[208,310],[284,321]]]),
            '../images/512 LF.bmp': np.float64([[[434,104], [416,242], [343,305], [287,264], [248,250],[214,252],[210,151],[270,71],[351,82]]]),
            '../images/513 RF.bmp': np.float64([[[501,252], [477,141], [410,90], [370,123], [337,135],[287,129],[281,214],[345,292],[429,281]]]),
            '../images/513 RB.bmp': np.float64([[[474,130], [471,252], [359,259], [341,242], [297,237],[301,239],[297,153],[261,85],[414,105]]]),
            '../images/513 LB.bmp': np.float64([[[406,227], [431,102], [329,49], [309,93], [274,111],[228,118],[242,208],[308,272],[355,254]]]),
            '../images/513 LF.bmp': np.float64([[[447,174], [403,288], [337,226], [294,292], [253,267],[205,261],[212,169],[314,114],[374,137]]]),
            '../images/515 RF.bmp': np.float64([[[427,290], [438,160], [371,84], [327,121], [283,125],[256,120],[283,207],[272,291],[347,302]]]),
            '../images/515 RB.bmp': np.float64([[[377,50], [448,172], [390,237], [331,232], [283,225],[248,227],[214,139],[247,52],[309,50]]]),
            '../images/515 LB.bmp': np.float64([[[380,294], [430,160], [348,99], [306,127], [272,124],[250,123],[227,209],[259,294],[314,299]]]),
            '../images/515 LF.bmp': np.float64([[[409,112], [292,246], [316,303], [280,259], [220,242],[184,242],[189,154],[254,71],[326,84]]]),
            '../images/516 RF.bmp': np.float64([[[452,280], [440,138], [346,78], [300,110], [269,121],[237,118],[220,218],[284,300],[353,298]]]),
            '../images/516 RB.bmp': np.float64([[[422,62], [438,201], [353,262], [296,242], [274,232],[238,226],[216,133],[265,46],[329,45]]]),
            '../images/516 LB.bmp': np.float64([[[465,282], [505,139], [410,62], [376,94], [336,116],[300,123],[289,215],[360,298],[414,292]]]),
            '../images/516 LF.bmp': np.float64([[[500,89], [482,224], [409,288], [350,255], [299,233],[265,232],[245,141],[310,44],[412,51]]]),
            '../images/517 RF.bmp': np.float64([[[421,277], [464,150], [387,84], [345,125], [313,140],[279,135],[254,226],[317,307],[386,299]]]),
            '../images/517 RB.bmp': np.float64([[[391,75], [414,206], [344,262], [296,234], [270,221],[236,223],[225,131],[277,55],[329,64]]]),
            '../images/517 LB.bmp': np.float64([[[431,287], [464,150], [378,94], [341,128], [313,137],[287,136],[281,231],[326,307],[380,297]]]),
            '../images/517 LF.bmp': np.float64([[[427,95], [409,221], [342,286], [293,250], [259,236],[224,240],[200,152],[252,58],[343,69]]])
}
