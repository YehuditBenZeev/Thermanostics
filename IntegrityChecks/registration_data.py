import numpy as np

# put 9 palm points from 1 to 9
LB_514 = np.float64([[[547,299], [490,158], [385,81], [339,122], [301,142],[260,141],[243,241],[295,316],[367,316]]])  ###
LF_514 = np.float64([[[479,114], [453,251], [369,304], [314,260], [267,241],[223,233],[214,142],[285,54],[386,72]]])  ###
RB_514 = np.float64([[[456,58], [477,199], [385,269], [338,231], [306,215],[257,217],[253,115],[283,42],[353,36]]])  ###
RF_514 = np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]])


images_514 = {
            '../514 images/514 RF dark.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF flip.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF HN.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF HW.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF light.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF move down.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF no arm.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF -r.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF rotate 25.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF s.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF VN.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF VW.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../514 images/514 RF w.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]])
}

images = {
            '../images/509 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/509 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/509 LB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/509 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/511 RF.bmp': np.float64([[[463,223], [455,87], [384,40], [332,75], [286,82],[246,83],[244,171],[296,249],[370,242]]]),
            '../images/511 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/511 LB.bmp': np.float64([[[366,314], [417,179], [340,107], [296,133], [271,141],[248,154],[212,253],[244,330],[302,328]]]),
            '../images/511 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/512 RF.bmp': np.float64([[[547,267], [451,138], [365,68], [302,99], [261,114],[220,116],[219,220],[282,300],[375,295]]]),
            '../images/512 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/512 LB.bmp': np.float64([[[350,327], [415,192], [363,104], [293,121], [258,126],[218,113],[168,213],[208,310],[284,321]]]),
            '../images/512 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/513 RF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/513 RB.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/513 LB.bmp': np.float64([[[406,227], [431,102], [329,49], [309,93], [274,111],[228,118],[242,208],[308,272],[355,254]]]),
            '../images/513 LF.bmp': np.float64([[[245, 47], [107, 133], [73, 173], [93, 217], [141, 303]]]),
            '../images/515 RF.bmp': np.float64([[[427,290], [438,160], [371,84], [327,121], [283,125],[256,120],[283,207],[272,291],[347,302]]]),
            '../images/515 RB.bmp': np.float64([[[377,50], [448,172], [390,237], [331,232], [283,225],[248,227],[214,139],[247,52],[309,50]]]),
            '../images/515 LB.bmp': np.float64([[[380,294], [430,160], [348,99], [306,127], [272,124],[250,123],[227,209],[259,294],[314,299]]]),
            '../images/515 LF.bmp': np.float64([[[409,112], [292,246], [316,303], [280,259], [220,242],[184,242],[189,154],[254,71],[326,84]]]),
            '../images/516 RF.bmp': np.float64([[[452,280], [440,138], [346,78], [300,110], [269,121],237,118],[220,218],284,300],[353,298]),
            '../images/516 RB.bmp': np.float64([[[422,62], [438,201], [353,262], [296,242], [274,232],[238,226],[216,133],[265,46],[329,45]]]),
            '../images/516 LB.bmp': np.float64([[[465,282], [505,139], [410,62], [376,94], [336,116],[300,123],[289,215],[360,298],[414,292]]]),
            '../images/516 LF.bmp': np.float64([[[500,89], [482,224], [409,288], [350,255], [299,233],[265,232],[245,141],[310,44],[412,51]]]),
            '../images/517 RF.bmp': np.float64([[[421,277], [464,150], [387,84], [345,125], [313,140],[279,135],[254,226],[317,307],[386,299]]]),
            '../images/517 RB.bmp': np.float64([[[391,75], [414,206], [344,262], [296,234], [270,221],[236,223],[225,131],[277,55],[329,64]]]),
            '../images/517 LB.bmp': np.float64([[[431,287], [464,150], [378,94], [341,128], [313,137],[287,136],[281,231],[326,307],[380,297]]]),
            '../images/517 LF.bmp': np.float64([[[427,95], [409,221], [342,286], [293,250], [259,236],[224,240],[200,152],[252,58],[343,69]]])
}
