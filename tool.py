import pandas as pd
import numpy as np
def append_imgQuality(quality_file, df, di='\t', nanfill=-1):
    #quality_file='avito_results.txt'
    ## build a dict to hold imgname->features
    img2feat_dict={}
    expose_list=[]
    pallet_list=[]
    grey_list=[]
    blur_list=[]
    img_list=[]
    with open(quality_file,'r') as f:
        # name  expose  pallet  grey    blur
        for idx,s in enumerate(f):
            s=s.strip()
#            print s
            name, expose, pallet, gey, blur = s.split(di)
            img2feat_dict[name.split('.')[0]]=[float(expose),float(pallet),float(gey),float(blur) ]
    ad_id_list=[]
    for ad_id in df.index:
        imgname=df.image[ad_id]
        if imgname not in img2feat_dict:
            continue
        ad_id_list.append(ad_id)
        array = img2feat_dict[imgname]
        expose_list.append(array[0]);pallet_list.append(array[1]);grey_list.append(array[2]);blur_list.append(array[3])
    # make dataFrame...
    img_df = pd.DataFrame({'expose':expose_list, 'pallet':pallet_list,'grey':grey_list,'blur':blur_list}, index=ad_id_list)
    df=pd.concat([df, img_df], axis=1)
    df.expose.fillna(nanfill,inplace=True)
    df.pallet.fillna(nanfill,inplace=True)
    df.grey.fillna(nanfill,inplace=True)
    df.blur.fillna(nanfill,inplace=True)
    return df


