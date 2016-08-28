dd = [{'huxing': '房屋户型：2室1厅1卫1厨1阳台', 'beds_num': '共3张', 'address': '北京市东城区广渠门北里55号金桥国际酒店公寓', 'rent_type': '整套出租', 'price': '668', 'img': 'http://image.xiaozhustatic1.com/00,800,533/7,0,28,8368,1800,1200,916ca9e8.jpg', 'user_num': '宜住4人', 'title': '市中心两居天安门北京站天坛国贸临铁7号', 'housesize': '房屋面积：72平米'},
      {'huxing': '房屋户型：2室1厅1卫1厨1阳台', 'beds_num': '共3张', 'address': '北京市东城区广渠门北里55号金桥国际酒店公寓', 'rent_type': '整套出租', 'price': '668', 'img': 'http://image.xiaozhustatic1.com/00,800,533/7,0,28,8368,1800,1200,916ca9e8.jpg', 'user_num': '宜住4人', 'title': '市中心两居天安门北京站天坛国贸临铁7号', 'housesize': '房屋面积：72平米'}
]

with open ('ttt.txt','w') as f:
    for i in dd:
        for key in i:
            f.write(key+':')
            for v in i[key]:
                f.write(v)
            f.write('\n')
        f.write('\n')
