import pyzed.sl as sl


def image_capture():
    zed = sl.Camera()
    init_params = sl.InitParameters()
    init_params.depth_mode = sl.DEPTH_MODE.NEURAL  # Use ULTRA depth mode
    init_params.coordinate_units = sl.UNIT.MILLIMETER  # Use millimeter units (for depth measurements)
    init_params.depth_minimum_distance = 200
    init_params.depth_maximum_distance = 20000
    init_params.enable_image_enhancement = True
    init_params.depth_stabilization = True
    init_params.camera_fps = 30  # fps可选：15、30、60、100
    zed.open(init_params)
    return zed


def image_capture2(abc):
    zed = abc
    depth = sl.Mat()
    runtime_parameters = sl.RuntimeParameters()  # 设置相机获取参数
    runtime_parameters.sensing_mode = sl.SENSING_MODE.STANDARD
    runtime_parameters.confidence_threshold = 100
    runtime_parameters.texture_confidence_threshold = 100
    runtime_parameters.textureness_confidence_threshold = 100
    if zed.grab(runtime_parameters) == sl.ERROR_CODE.SUCCESS:
        zed.retrieve_measure(depth, sl.MEASURE.DEPTH)  # 深度值
    return depth


if __name__ == "__main__":
    a = image_capture()
    while 1:
        ll = 0
        p = 0
        b = image_capture2(a)
        for k in range(640, 643):
            for j in range(360, 363):
                if b.get_value(k, j)[1] is not None and b.get_value(k, j)[1] >= 200 and b.get_value(k, j)[
                    1] <= 20000 and b.get_value(k, j)[1] == b.get_value(k, j)[1]:
                    p += b.get_value(k, j)[1]
                    ll += 1
        if ll >= 5:
            print('原深度',p / ll,'深度',(p * 1.45/ll))
