# @Author : cheertt
# @Time   : 2019/6/27 10:17
# @Remark :

import os
import json

# 如：'zhuguangquan', 'guguoning', 'baoxiaofeng', 'hejia'
filename = '文件名-每次需要手动编辑'
jsonname = 'raw视频json文件名称'
# 版本1数据集只有四个名称，即四个主持人的名称，固定死
res = ['zhuguangquan', 'guguoning', 'baoxiaofeng', 'hejia']


def get_image(video_path, image_path):
    """
    获取视频对应的图片帧
    :param video_path: 原始视频路径
    :param image_path: 处理后图像的存放路径
    :return:
    """
    try:
        os.system('ffmpeg -i {0} -vf fps=fps=8/1 -q 0 {1}/%06d.jpg'.format(video_path, image_path))
    except:
        print('=======================================================')
        print(video_path)
        print('while handling image, something seems to have an error!')


if __name__ == '__main__':
    with open(jsonname, 'r') as load_f:
        load_dict = json.load(load_f)
        tmp = load_dict['videos']
        for r in res:
            lis = tmp.get(res[0])  # 获取某一个主持人的视频列表
            print('start......')
            for li in lis:
                # 判断当前路径是否存在，没有则创建new文件
                folder_path = 'host_video/frames/' +filename + '/' + li
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                # 处理操作，获取图片
                video_path = 'host_video_raw/' + filename + '.mp4'
                image_path = folder_path
                get_image(video_path, image_path)

    print('success!')