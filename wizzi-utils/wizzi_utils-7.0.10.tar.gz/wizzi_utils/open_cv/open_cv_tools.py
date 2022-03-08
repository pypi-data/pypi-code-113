import numpy as np
import math
import os
from wizzi_utils.pyplot import pyplot_tools as pyplt
from wizzi_utils.misc import misc_tools as mt
# noinspection PyPackageRequirements
import cv2


def get_cv_version(ack: bool = False, tabs: int = 1) -> str:
    """ see get_cv_version_test() """
    """ see get_cv_version_test() """
    string = mt.add_color('{}* OpenCv Version {}'.format(tabs * '\t', cv2.getVersionString()), ops=mt.SUCCESS_C)
    string += mt.add_color(' - GPU detected ? ', ops=mt.SUCCESS_C)
    if cuda_on():
        string += mt.add_color('True', ops=mt.SUCCESS_C2)
    else:
        string += mt.add_color('False', ops=mt.FAIL_C2)
    if ack:
        print(string)
    return string


def load_img(path: str, ack: bool = True, tabs: int = 1) -> np.array:
    """ see imread_imwrite_test() """
    if os.path.exists(path):
        img = cv2.imread(path)
        if ack:
            size_s = mt.file_or_folder_size(path)
            file_msg = '{}({}) of shape {}'.format(path, size_s, img.shape)
            print('{}{}'.format(tabs * '\t', mt.LOADED.format(file_msg)))
    else:
        mt.exception_error(mt.NOT_FOUND.format(path), real_exception=False, tabs=tabs)
        img = None
    return img


def save_img(path: str, img: np.array, ack: bool = True, tabs: int = 1) -> None:
    """ see imread_imwrite_test() """
    d = os.path.dirname(path)
    if not d or os.path.exists(d):  # no dir, save locally or dir must exist
        cv2.imwrite(path, img)
        if ack:
            size_s = mt.file_or_folder_size(path)
            file_msg = '{}({}) of shape {}'.format(path, size_s, img.shape)
            print('{}{}'.format(tabs * '\t', mt.SAVED.format(file_msg)))
    else:
        mt.exception_error(mt.NOT_FOUND.format(os.path.dirname(path)), real_exception=False)
    return


def list_to_cv_image(cv_img: [list, np.array]) -> np.array:
    """
    :param cv_img: numpy or list. if list: convert to numpy with dtype uint8
    :return: cv_img
    see list_to_cv_image_test()
    """
    if mt.is_list(cv_img):
        cv_img = np.array(cv_img, dtype='uint8')
    return cv_img


def display_open_cv_image(
        img: np.array,
        ms: int = 0,
        title: str = 'cv_image',
        loc: (tuple, str) = None,
        resize: (float, int, str, tuple) = None,
        header: str = None,
        save_path: str = None,
        tabs: int = 1,
) -> int:
    """
    :param img: cv image in numpy array or list
    :param ms: 0 blocks, else time in milliseconds before image is closed
    :param title: window title
    :param loc: top left corner window location
        if tuple: x,y coordinates
        if str: see Location enum in pyplt. e.g. pyplt.Location.TOP_LEFT.value (which is 'top_left')
    :param resize: None, float>0, tuple=(w,h), str='fs'
    :param header: text to add at the top left
    :param save_path: if not none, saves image to this path
    :param tabs:
    :return key clicked
    e.g. using key:
    if k == ord('q'):
        mt.exception_error('q was clicked. breaking loop')
        break
    see display_open_cv_image_test()
    """
    img = list_to_cv_image(img)
    if resize is not None:
        img = resize_opencv_image(img, resize)
    if header is not None:
        add_header(img, header, bg_font_scale=1)
    if save_path is not None:
        save_img(path=save_path, img=img, ack=True, tabs=tabs)
    cv2.imshow(title, img)
    if loc is not None:
        if mt.is_str(loc):
            move_cv_img_by_str(img, title, where=loc)
        elif mt.is_tuple(loc):
            move_cv_img_x_y(title, x_y=loc)
    key = cv2.waitKey(ms)
    return key


def resize_opencv_image(img: np.array, resize: (float, int, str, tuple), res_inter: int = cv2.INTER_AREA):
    """
    :param img: cv img
    :param resize:
        if float>0 or int>0(could be bigger than 1)
        if str: 'fs' for full screen
        if tuple: new dims (w,h)
    :param res_inter: resize interpolation. e.g. cv2.INTER_AREA, cv2.INTER_CUBIC
    img_size *= scale_percent
    see resize_opencv_image_test()
    """
    if mt.is_float(resize) or mt.is_int(resize):
        if resize <= 0:
            resize_image = img
            mt.exception_error('illegal value for scale_percent={}'.format(resize), real_exception=False, tabs=0)
        else:
            width = math.ceil(img.shape[1] * resize)
            height = math.ceil(img.shape[0] * resize)
            dim = (width, height)
            resize_image = cv2.resize(img, dim, interpolation=res_inter)
    elif mt.is_tuple(resize):
        resize_image = cv2.resize(img, resize, interpolation=res_inter)
    elif mt.is_str(resize) and resize == 'fs':
        max_x, max_y = pyplt.screen_dims()
        fs_dims = (max_x - 30, max_y - 100)
        resize_image = cv2.resize(img, fs_dims, interpolation=res_inter)
    else:
        resize_image = None
        mt.exception_error('illegal resize option={}. options=float,2d tuple or "fs"(full screen)'.format(resize),
                           real_exception=False, tabs=0)
    return resize_image


def move_cv_img_x_y(win_title: str, x_y: tuple) -> None:
    """
    :param win_title: cv img with win_title to be moved
    :param x_y: tuple of ints. x,y of top left corner
    Move cv img upper left corner to pixel (x, y)
    see move_cv_img_x_y_test()
    """
    cv2.moveWindow(win_title, x_y[0], x_y[1])
    return


def move_cv_img_by_str(img: np.array, win_title: str, where: str = pyplt.Location.TOP_LEFT.value,
                       task_bar_offset: int = None) -> None:
    """
    :param img: to get the dims of the image
    :param win_title: cv img with win_title to be moved
    :param where: see Location enum in pyplt. e.g. pyplt.Location.TOP_LEFT.value (which is 'top_left')
    :param task_bar_offset: size of taskbar for bottom locs
    Move cv img upper left corner to pixel (x, y)
    see move_cv_img_by_str_test()
    """
    where_full = pyplt.Location.where_to(w_short=where)
    if where_full is not None:  # if not None, shortcut was entered
        where = where_full
    try:
        window_w, window_h = pyplt.screen_dims()  # screen dims in pixels
        if window_w != -1 and window_h != -1:
            fig_w, fig_h = img.shape[1], img.shape[0]
            if task_bar_offset is None:
                # 75 is good
                task_bar_offset = 75
            x, y = pyplt.calc_x_y_by_loc_str(where, window_w, window_h, fig_w, fig_h, task_bar_offset=task_bar_offset)
            move_cv_img_x_y(win_title, x_y=(x, y))
        else:
            move_cv_img_x_y(win_title, x_y=(0, 0))
    except (ValueError, Exception) as e:
        mt.exception_error(e, real_exception=True)
        move_cv_img_x_y(win_title, x_y=(0, 0))
    return


def unpack_list_imgs_to_big_image(imgs: list, grid: tuple) -> np.array:
    """
    :param imgs: list of cv images
    :param grid: the layout you want as output
        (1,len(imgs)): 1 row
        (len(imgs),1): 1 col
        (2,2): 2x2 grid - supports len(imgs)<=4 but not more
    see unpack_list_imgs_to_big_image_test()
    """
    for i in range(len(imgs)):
        imgs[i] = list_to_cv_image(imgs[i])
        if len(imgs[i].shape) == 2:  # if gray - see as rgb
            imgs[i] = gray_scale_img_to_BGR_form(imgs[i])

    imgs_n = len(imgs)
    if imgs_n == 1:
        big_img = imgs[0]
    else:
        padding_bgr = list(pyplt.get_BGR_color('red'))
        height, width, cnls = imgs[0].shape
        rows, cols = grid
        big_img = np.zeros(shape=(height * rows, width * cols, cnls), dtype='uint8') + 255  # white big image

        row_ind, col_ind = 1, 1
        for i, img in enumerate(imgs):
            h_begin, h_end = height * (row_ind - 1), height * row_ind
            w_begin, w_end = width * (col_ind - 1), width * col_ind
            big_img[h_begin:h_end, w_begin:w_end, :] = img  # 0

            if rows > 1:  # draw bounding box on the edges. no need if there is 1 row or 1 col
                big_img[h_begin, w_begin:w_end, :] = padding_bgr
                big_img[h_end - 1, w_begin:w_end - 1, :] = padding_bgr
            if cols > 1:
                big_img[h_begin:h_end, w_begin, :] = padding_bgr
                big_img[h_begin:h_end, w_end - 1, :] = padding_bgr

            col_ind += 1
            if col_ind > cols:
                col_ind = 1
                row_ind += 1
    return big_img


def display_open_cv_images(
        imgs: list,
        ms: int = 0,
        title: str = 'cv_image',
        loc: (tuple, str) = None,
        resize: (float, str, tuple) = None,
        grid: tuple = (1, 2),
        header: str = None,
        save_path: str = None,
        tabs: int = 1,
) -> int:
    """
    :param imgs: list of RGB or gray scale images
    :param ms: 0 blocks, else time in milliseconds before image is closed
    :param title: window title
    :param loc: top left corner window location
        if tuple: x,y coordinates
        if str: see Location enum in pyplt. e.g. pyplt.Location.TOP_LEFT.value (which is 'top_left')
    :param resize: None, float>0, tuple=(w,h), str='fs'
    :param grid: size of rows and cols of the new image. e.g. (2,1) 2 rows with 1 img on each
        grid slots must be >= len(imgs)
    :param header: text to add at the top left
    :param save_path: if not none, saves image to this path
    :param tabs:
    :return key clicked
    e.g. using key:
    if k == ord('q'):
        mt.exception_error('q was clicked. breaking loop')
        break
    see display_open_cv_images_test()
    """
    imgs_n = len(imgs)
    key = None
    if imgs_n > 0:
        total_slots = grid[0] * grid[1]
        assert imgs_n <= total_slots, 'grid has {} total_slots, but len(imgs)={}'.format(total_slots, imgs_n)
        big_img = unpack_list_imgs_to_big_image(imgs, grid=grid)
        key = display_open_cv_image(big_img, ms=ms, title=title, loc=loc, resize=resize, header=header,
                                    save_path=save_path, tabs=tabs)
    return key


def gray_scale_img_to_BGR_form(gray_img: np.array) -> np.array:
    """
    :param gray_img: from shape (x,y) - 1 channel (gray)
    e.g 480,640
    :return: RGB form image e.g 480,640,3. no real colors added - just shape as RGB
    see gray_to_BGR_and_back_test()
    """
    BGR_image = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
    return BGR_image


def BGR_img_to_gray(bgr_img: np.array) -> np.array:
    """
    :param bgr_img: from shape (x,y,3) - 3 channels
    e.g 480,640,3
    :return: gray image e.g 480,640. colors are replaced to gray colors
    see gray_to_BGR_and_back_test()
    """
    gray = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
    return gray


def BGR_img_to_RGB(bgr_img: np.array) -> np.array:
    """
    :param bgr_img: from shape (x,y,3) - 3 channels
    e.g 480,640,3
    :return: rgb image
    see BGR_img_to_RGB_and_back_test()
    """
    rgb_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB)
    return rgb_img


def RGB_img_to_BGR(rgb_img: np.array) -> np.array:
    """
    :param rgb_img: from shape (x,y,3) - 3 channels
    e.g 480,640,3
    :return: bgr image
    see BGR_img_to_RGB_and_back_test()
    """
    bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
    return bgr_img


class CameraWu:
    def __init__(self, port: int, type_cam: str = 'cv2'):
        self.port = port
        self.type_cam = type_cam
        try:
            pip_err = 'Error {}. pip install {}'
            failed_err = 'Failed to open CameraWu({}) on port {}'.format(type_cam, port)
            if type_cam == 'acapture':
                try:
                    # noinspection PyPackageRequirements
                    import acapture  # pip install acapture
                    if mt.is_linux():  # NOT TESTED
                        acapture.camera_info()
                    if not self.check_port_valid(port):
                        self.cam = None
                        raise Exception(failed_err)
                    self.cam = acapture.open(port)
                    success, frame = self.cam.read()
                    if frame is None:
                        self.cam = None
                        raise Exception(failed_err)
                except ModuleNotFoundError as e:
                    self.cam = None
                    raise ModuleNotFoundError(pip_err.format(e, 'acapture'))
            elif type_cam == 'imutils':
                try:
                    # noinspection PyPackageRequirements,PyUnresolvedReferences
                    from imutils import video  # pip install imutils
                    self.cam = video.VideoStream(src=port).start()
                    frame = self.cam.read()
                    if frame is None:
                        self.cam = None
                        raise Exception(failed_err)
                except ModuleNotFoundError as e:
                    self.cam = None
                    raise ModuleNotFoundError(pip_err.format(e, 'imutils'))
            else:  # type_cam == 'cv2'
                self.cam = cv2.VideoCapture(port)
                if not self.cam.isOpened():
                    self.cam = None
                    raise Exception(failed_err)
        except Exception as e:
            raise e
        return

    @classmethod
    def open_camera(cls, port: int, type_cam: str = 'cv2'):
        try:
            cam = cls(port, type_cam)
            print('\tCameraWu({}) successfully open on port {}'.format(type_cam, port))
        except (ModuleNotFoundError, Exception) as e:
            mt.exception_error(e, real_exception=True, tabs=1)
            cam = None
        return cam

    @staticmethod
    def check_port_valid(port: int) -> bool:
        """
        :param port:
        :return:
        """
        temp_cam = cv2.VideoCapture(port)
        if temp_cam.isOpened():
            ret = True
            temp_cam.release()
        else:
            ret = False
        return ret

    def __del__(self):
        try:
            if self.cam is not None:
                if self.type_cam == 'acapture':
                    # noinspection PyUnresolvedReferences
                    self.cam.destroy()
                    mt.sleep(2, ack=True, tabs=2)  # acapture need a moment to release
                elif self.type_cam == 'imutils':
                    # noinspection PyUnresolvedReferences
                    self.cam.stop()
                    mt.sleep(2, ack=True, tabs=2)  # imutils need a moment to release
                else:  # type_cam == 'cv2'
                    if self.cam.isOpened():
                        self.cam.release()
                        mt.sleep(2, ack=True, tabs=2)  # just in case
                print('\tCameraWu({}) closed on port {}'.format(self.type_cam, self.port))
        except AttributeError as e:
            mt.exception_error('e {}. can\'t close CameraWu'.format(e), real_exception=True)
        return

    def read_img(self) -> (bool, np.array):
        try:
            frame = None
            if self.type_cam == 'acapture':
                _, frame = self.cam.read()
                if frame is not None:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            elif self.type_cam == 'imutils':
                frame = self.cam.read()
            else:  # type_cam == 'cv2'
                if self.cam.isOpened():
                    # self.cam.release()
                    # self.cam = cv2.VideoCapture(self.port)
                    _, frame = self.cam.read()
                    # self.cam.set(cv2.CAP_PROP_POS_FRAMES, 0)
            success = False if frame is None else True
        except Exception as e:
            mt.exception_error('CameraWu: failed capture image. e {}'.format(e), real_exception=True)
            success, frame = False, None
        return success, frame


def add_text(
        cv_img: np.array,
        header: str,
        pos: tuple,
        text_color: str = 'white',
        with_rect: bool = True,
        bg_color: str = 'black',
        bg_font_scale: int = 1
):
    """
    :param cv_img:
    :param header:
    :param pos:
    :param text_color: str
    :param with_rect:
    :param bg_color: str
    :param bg_font_scale: int. 1 or 2 - pos changes by scale and font
    :return:
    see add_text_test()
    """
    x, y = pos
    if bg_font_scale == 1:  # big font and scale
        font: int = cv2.FONT_HERSHEY_DUPLEX
        font_scale: float = 1
        font_thickness: int = 1
        text_size, _ = cv2.getTextSize(header, font, font_scale, font_thickness)
        text_w, text_h = text_size
        rect_pt1 = (x, y - 20)
        rect_pt2 = (x + text_w, y + text_h - 20)
    else:
        font: int = cv2.FONT_HERSHEY_DUPLEX
        font_scale: float = 0.5
        font_thickness: int = 1
        text_size, _ = cv2.getTextSize(header, font, font_scale, font_thickness)
        text_w, text_h = text_size
        rect_pt1 = (x, y)
        rect_pt2 = (x + text_w, y + text_h - 20)
    text_color = pyplt.get_BGR_color(text_color)

    # print(pos, (x + text_w, y + text_h))
    if with_rect:
        bg_color = pyplt.get_BGR_color(bg_color)
        cv2.rectangle(cv_img, pt1=rect_pt1, pt2=rect_pt2, color=bg_color, thickness=-1)
    cv2.putText(cv_img, text=header, org=pos, fontFace=font, fontScale=font_scale, color=text_color,
                thickness=font_thickness)
    return


def add_header(
        cv_img: np.array,
        header: str,
        loc: str = pyplt.Location.TOP_LEFT.value,
        x_offset: int = 0,
        text_color: str = 'white',
        with_rect: bool = True,
        bg_color: str = 'black',
        bg_font_scale: int = 1
) -> None:
    """
    :param cv_img: frame
    :param header: some text. e.g. iteration, timestamp ....
    :param loc: supports pyplt.Location.TOP_LEFT.value,  pyplt.Location.BOTTOM_LEFT.value
    :param x_offset: if left: x = 0 + x_offset. if right: x = x.shape[1] - x_offset
    :param text_color: as string e.g. 'red'
    :param with_rect: add rect around header
    :param bg_color: background rect color
    :param bg_font_scale: int. 1 or 2 - pos changes by scale and font
    :return:
    see add_header_test()
    """
    x_left = 0 + x_offset
    x_right = cv_img.shape[1] - x_offset
    if bg_font_scale == 1:
        y_up = 25
        y_down = cv_img.shape[0] - 5
    else:
        y_up = 15
        y_down = cv_img.shape[0] - 3

    if loc in [pyplt.Location.BOTTOM_LEFT.value, 'bl']:
        pos = (x_left, y_down)
    elif loc in [pyplt.Location.BOTTOM_RIGHT.value, 'br']:
        pos = (x_right, y_down)
    elif loc in [pyplt.Location.TOP_RIGHT.value, 'tr']:
        pos = (x_right, y_up)
    else:  # loc in [pyplt.Location.TOP_LEFT.value, 'tl]: # default
        pos = (x_left, y_up)
    add_text(cv_img, header, pos=pos, text_color=text_color, with_rect=with_rect, bg_color=bg_color,
             bg_font_scale=bg_font_scale)
    return


def get_dims_from_cap(cap: cv2.VideoCapture) -> tuple:
    """
    :param cap:
    frames size as (int, int)
    :return:
    see Mp4_creator_test()
    """
    out_dims = None
    if cap.isOpened():
        orig_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # float `width`
        orig_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # float `height`
        out_dims = (orig_width, orig_height)
    return out_dims


def get_frames_from_cap(cap: cv2.VideoCapture) -> int:
    """
    :param cap:
    :return:
    see Mp4_creator_test()
    """
    video_total_frames = None
    if cap.isOpened():
        video_total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    return video_total_frames


class Mp4_creator:
    def __init__(self, out_full_path: str, out_fps: float, out_dims: tuple, tabs: int = 1):
        """
        :param out_full_path:
        :param out_fps:
        :param out_dims:
        :param tabs:
        see Mp4_creator_test()
        """
        # fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fourcc = cv2.VideoWriter_fourcc(c1='m', c2='p', c3='4', c4='v')

        self.out_full_path = out_full_path
        self.out_fps = out_fps
        self.out_dims = out_dims
        self.tabs = tabs
        self.frames_count = 0
        if not os.path.exists(os.path.dirname(out_full_path)):
            mt.exception_error('Cant create cv2.VideoWriter', real_exception=False, tabs=self.tabs)
            mt.exception_error(mt.NOT_FOUND.format(os.path.dirname(out_full_path)), real_exception=False,
                               tabs=self.tabs)
            self.result = None
        else:
            self.result = cv2.VideoWriter(
                filename=out_full_path,
                fourcc=fourcc,
                fps=out_fps,
                frameSize=out_dims
            )
        return

    def __del__(self):
        if self.result is not None:
            self.result.release()
            self.result = None
        return

    def __str__(self):
        string = '{}Mp4_creator\n'.format(self.tabs * '\t')
        string += '{}\ttarget file path: {}\n'.format(self.tabs * '\t', self.out_full_path)
        string += '{}\tfps: {}\n'.format(self.tabs * '\t', self.out_fps)
        string += '{}\tout_dims: {}'.format(self.tabs * '\t', self.out_dims)
        return string

    def add_frame(self, frame: np.array, ack: bool = False, tabs: int = 1) -> None:
        if self.result is not None:
            cur_out_dims = (frame.shape[1], frame.shape[0])
            if cur_out_dims == self.out_dims:
                self.result.write(frame)
                self.frames_count += 1
                if ack:
                    print('{}frame {} added'.format(tabs * '\t', self.frames_count))
            else:
                mt.exception_error(
                    'Shapes mismatch: Frame.shape={}, Video shape={}'.format(cur_out_dims, self.out_dims),
                    real_exception=False, tabs=tabs)
        else:
            mt.exception_error('Cant write frame', real_exception=False, tabs=self.tabs)
        return

    def finalize(self):
        if self.result is not None:
            self.result.release()
            self.result = None
            print('{}File ready({} frames): {}'.format(self.tabs * '\t', self.frames_count, self.out_full_path))
        return


def get_aspect_ratio_w(img_w: int, img_h: int, new_h: int) -> tuple:
    """
    if you want to resize and image, give h and this func will calculate w
    :param img_w:
    :param img_h:
    :param new_h: new height
    :return: (new_w, new_h) : new_w is the new width with aspect ratio preserved
    see get_aspect_ratio_test()
    """
    new_w = int((new_h / img_h) * img_w)
    return new_w, new_h


def get_aspect_ratio_h(img_w: int, img_h: int, new_w: int) -> tuple:
    """
    opposite of get_aspect_ratio_w()
    see get_aspect_ratio_test()
    """
    new_h = int((new_w / img_w) * img_h)
    return new_w, new_h


def cuda_on() -> bool:
    """
    returns true if cuda detects gpu devices.
    see cuda_on_gpu_test()
    the test has a small manual how to install open-cv from source with GPU support on win10
    :return:
    """
    count = get_gpu_devices_count()
    return count > 0


def get_gpu_devices_count() -> int:
    """
    if open-cv build from source with gpu support returns GPUs detected (0 if no GPU)
    :return:
    """
    count = cv2.cuda.getCudaEnabledDeviceCount()
    return count


def sketch_image(cv_BGR: np.array, sigma_s: float = 50, sigma_r: float = 0.07, shade_factor: float = 0.08) -> (
        np.array, np.array):
    """
    :param cv_BGR:
    :param sigma_s: Range between 0 to 200
    :param sigma_r: Range between 0 to 1
    :param shade_factor: Range between 0 to 0.1
    :return:
    """
    sketch_gray, sketch_color = None, None
    if len(cv_BGR.shape) == 3:
        sketch_gray, sketch_color = cv2.pencilSketch(cv_BGR, sigma_s=sigma_s, sigma_r=sigma_r,
                                                     shade_factor=shade_factor)
    else:
        mt.exception_error(e='image must be BGR: image.shape={}'.format(cv_BGR.shape))

    return sketch_gray, sketch_color


def invert_image(cv_img: np.array) -> np.array:
    """
    :param cv_img: gray\BGR - invert colors
    :return:
    """
    invert = cv2.bitwise_not(cv_img)
    return invert


def get_color_maps(n: int = None) -> list:
    """
    see https://docs.opencv.org/4.x/d3/d50/group__imgproc__colormap.html
    :param n: how many random color maps
    :return: all(22) color maps or n random color maps in a list
    """
    cmaps = np.int32([
        cv2.COLORMAP_AUTUMN,
        cv2.COLORMAP_BONE,
        cv2.COLORMAP_JET,
        cv2.COLORMAP_WINTER,
        cv2.COLORMAP_RAINBOW,
        cv2.COLORMAP_OCEAN,
        cv2.COLORMAP_SUMMER,
        cv2.COLORMAP_SPRING,
        cv2.COLORMAP_COOL,
        cv2.COLORMAP_HSV,
        cv2.COLORMAP_PINK,
        cv2.COLORMAP_HOT,
        cv2.COLORMAP_PARULA,
        cv2.COLORMAP_MAGMA,
        cv2.COLORMAP_INFERNO,
        cv2.COLORMAP_PLASMA,
        cv2.COLORMAP_VIRIDIS,
        cv2.COLORMAP_CIVIDIS,
        cv2.COLORMAP_TWILIGHT,
        cv2.COLORMAP_TWILIGHT_SHIFTED,
        cv2.COLORMAP_TURBO,
        cv2.COLORMAP_DEEPGREEN
    ])
    if n is not None:
        n = min(n, len(cmaps))
        rand_ints = mt.np_random_integers(low=0, high=len(cmaps) - 1, size=(n,))
        cmaps = cmaps[rand_ints]
    return cmaps.tolist()


def add_color_map(cv_img: np.array, color_map: int = cv2.COLORMAP_AUTUMN) -> np.array:
    """
    :param cv_img: bgr\gray -> same result
    :param color_map: one of the values from get_color_maps():
    :return:
    """
    color_image = cv2.applyColorMap(cv_img, color_map)
    return color_image


def draw_plus(cv_img: np.array, plus_center_xy: tuple, plus_color: str = 'black', pixels: int = 20,
              add_center_text: bool = True, text_color: str = None, text_up: bool = True) -> None:
    """
    :param cv_img:
    :param plus_center_xy: center of the plus - no problem if it is outside of the image
    :param plus_color: as str
    :param pixels: distance from center.
        e.g. pixels=20: the bounding square of the plus is 40x40 and it's center is center_xy
    :param add_center_text: add the 2d point above the plus
    :param text_color: as str. if none, same as plus_color
    :param text_up: up/down relative to the plus
    :return:
    """
    plus_cBGR = pyplt.get_BGR_color(plus_color)

    x, y = plus_center_xy
    xy1 = (x, y - pixels)
    xy2 = (x, y + pixels)
    cv2.line(cv_img, pt1=xy1, pt2=xy2, color=plus_cBGR, thickness=1, lineType=cv2.LINE_AA)
    xy1 = (x - pixels, y)
    xy2 = (x + pixels, y)
    cv2.line(cv_img, pt1=xy1, pt2=xy2, color=plus_cBGR, thickness=1, lineType=cv2.LINE_AA)
    if add_center_text:
        if text_color is None:
            text_color = plus_color
        y_offset = 30 if text_up else -50
        add_text(cv_img, header='{},{}'.format(x, y), pos=(x - 65, y - y_offset), text_color=text_color,
                 with_rect=False, bg_font_scale=1)
    return


def draw_x(cv_img: np.array, x_center_xy: tuple, x_color: str = 'black', pixels: int = 20,
           add_center_text: bool = True, text_color: str = None, text_up: bool = True) -> None:
    """
    :param cv_img:
    :param x_center_xy: center of the x - no problem if it is outside of the image
    :param x_color: as str
    :param pixels: distance from center.
        e.g. pixels=20: the diagonal from x_center_xy to the edges is 20
            so the diagonal of the bounding square of the x is 40
    :param add_center_text: add the 2d point above the plus
    :param text_color: as str. if none, same as plus_color
    :param text_up: up/down relative to the plus
    :return:
    """
    plus_cBGR = pyplt.get_BGR_color(x_color)

    x, y = x_center_xy
    pixels = int(pixels / np.sqrt(2))

    xy1 = (x - pixels, y - pixels)
    xy2 = (x + pixels, y + pixels)
    cv2.line(cv_img, pt1=xy1, pt2=xy2, color=plus_cBGR, thickness=1, lineType=cv2.LINE_AA)
    xy1 = (x + pixels, y - pixels)
    xy2 = (x - pixels, y + pixels)
    cv2.line(cv_img, pt1=xy1, pt2=xy2, color=plus_cBGR, thickness=1, lineType=cv2.LINE_AA)
    if add_center_text:
        if text_color is None:
            text_color = x_color
        y_offset = 20 if text_up else -40
        add_text(cv_img, header='{},{}'.format(x, y), pos=(x - 65, y - y_offset), text_color=text_color,
                 with_rect=False, bg_font_scale=1)
    return cv_img


def get_roi_2dpoints(cv_img: np.array, resize: float = None, mark_color: str = 'g',
                     add_center_text: bool = False, cursor_arrow: bool = False) -> list:
    """
    :param cv_img: gray\bgr
    :param resize: float in (0,1] - if none: no resize. else enlarge\reduce to 'resize'%
    :param mark_color:
    :param add_center_text: add 2d value above X mark
    :param cursor_arrow: if True and is_windows(), changes cursor to arrow style making it easier to select roi
    :return:
    """
    d2points = []
    # if resize not None, need to scale back the points
    resize_inv = None if resize is None else 1 / resize
    cv_img_clean = cv_img.copy()  # clone to delete
    if len(cv_img_clean.shape) == 2:  # gray - convert to 3 channel gray
        cv_img_clean = gray_scale_img_to_BGR_form(cv_img_clean)
    cv_img_temp = cv_img_clean.copy()  # clone not to draw on original image

    # noinspection PyUnusedLocal
    def get_roi_xy2(event, x, y, flags, param):
        """
        more events at https://docs.opencv.org/3.4/d0/d90/group__highgui__window__flags.html
        [cv2.EVENT_MOUSEMOVE, cv2.EVENT_LBUTTONDOWN, cv2.EVENT_RBUTTONDOWN, cv2.EVENT_MBUTTONDOWN,
         cv2.EVENT_LBUTTONUP, cv2.EVENT_RBUTTONUP, cv2.EVENT_MBUTTONUP, cv2.EVENT_LBUTTONDBLCLK,
         cv2.EVENT_RBUTTONDBLCLK, cv2.EVENT_MBUTTONDBLCLK, cv2.EVENT_MOUSEWHEEL, cv2.EVENT_MOUSEHWHEEL]
        """
        if cursor_arrow and event == cv2.EVENT_MOUSEMOVE and mt.is_windows():
            try:
                import win32api
                import win32con
                win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_ARROW))
            except Exception as e:
                mt.exception_error(e, real_exception=True)

        if event == cv2.EVENT_LBUTTONDOWN:
            if resize_inv is not None:
                x = int(x * resize_inv)
                y = int(y * resize_inv)
            xy = (x, y)
            draw_x(cv_img_temp, x_center_xy=xy, x_color=mark_color, pixels=20,
                   add_center_text=add_center_text, text_color=None, text_up=True)
            d2points.append(xy)
        return

    title = "select_roi: img shape {} ('d' to delete last, 'q' to finish)".format(cv_img_temp.shape)

    cv2.namedWindow(title)
    cv2.setMouseCallback(title, get_roi_xy2)

    for i in range(10 ** 10):
        k = display_open_cv_image(cv_img_temp, title=title, ms=1, loc='tl', resize=resize)
        if k == ord('d'):  # delete last selection
            if len(d2points) > 0:
                cv_img_temp = cv_img_clean.copy()  # delete all
                d2points.pop()  # remove last selection from list
                for d2p in d2points:  # draw the list
                    draw_x(cv_img_temp, x_center_xy=d2p, x_color=mark_color, pixels=20,
                           add_center_text=add_center_text, text_color=None, text_up=True)
        if k == ord('q'):
            break
    cv2.destroyAllWindows()
    return d2points


def get_named_roi_2dpoints(cv_img: np.array, names_colors: dict, resize: float = None,
                           add_center_text: bool = False, cursor_arrow: bool = False) -> dict:
    """
    :param cv_img: gray\bgr
    :param names_colors: dict of name to color (str, str) - recommended ordered dict
        e.g. names_colors = {'port1_top_left': 'g', 'port1_top_right': 'r', 'port1_bottom_right': 'b'}
        this is done so i can concat 2 image side by side. e.g. {'port1_g': 'g', 'port2_g': 'g'}
    :param resize: float in (0,1] - if none: no resize. else enlarge\reduce to 'resize'%
    :param add_center_text: add 2d value above X mark
    :param cursor_arrow: if True and is_windows(), changes cursor to arrow style making it easier to select roi
    :return: named_points. e.g. {'port1_top_left': (100,100), ... }
    notice if you press 'q' and didn't mark all the points, you'll get some of the points
    """
    names = list(names_colors.keys())
    colors = list(names_colors.values())
    named_points = {}
    current_idx = 0

    # if resize not None, need to scale back the points
    resize_inv = None if resize is None else 1 / resize
    cv_img_clean = cv_img.copy()  # clone to delete
    if len(cv_img_clean.shape) == 2:  # gray - convert to 3 channel gray
        cv_img_clean = gray_scale_img_to_BGR_form(cv_img_clean)
    cv_img_temp = cv_img_clean.copy()  # clone not to draw on original image

    # noinspection PyUnusedLocal
    def get_roi_xy2(event, x, y, flags, param):
        """
        more events at https://docs.opencv.org/3.4/d0/d90/group__highgui__window__flags.html
        [cv2.EVENT_MOUSEMOVE, cv2.EVENT_LBUTTONDOWN, cv2.EVENT_RBUTTONDOWN, cv2.EVENT_MBUTTONDOWN,
         cv2.EVENT_LBUTTONUP, cv2.EVENT_RBUTTONUP, cv2.EVENT_MBUTTONUP, cv2.EVENT_LBUTTONDBLCLK,
         cv2.EVENT_RBUTTONDBLCLK, cv2.EVENT_MBUTTONDBLCLK, cv2.EVENT_MOUSEWHEEL, cv2.EVENT_MOUSEHWHEEL]
        """
        if cursor_arrow and event == cv2.EVENT_MOUSEMOVE and mt.is_windows():
            try:
                import win32api
                import win32con
                win32api.SetCursor(win32api.LoadCursor(0, win32con.IDC_ARROW))
            except Exception as e:
                mt.exception_error(e, real_exception=True)

        if event == cv2.EVENT_LBUTTONDOWN:
            nonlocal current_idx
            if current_idx < len(colors):
                current_name = names[current_idx]
                current_color = colors[current_idx]
                if resize_inv is not None:
                    x = int(x * resize_inv)
                    y = int(y * resize_inv)
                xy = (x, y)
                draw_x(cv_img_temp, x_center_xy=xy, x_color=current_color, pixels=20,
                       add_center_text=add_center_text, text_color=None, text_up=True)
                named_points[current_name] = {
                    'c': current_color,
                    'xy': xy
                }
                current_idx += 1
                if current_idx < len(colors):
                    draw_next_info(cv_img_temp, _name=names[current_idx], _color=colors[current_idx])
        return

    def draw_next_info(_cv_img: np.array, _name: str, _color: str) -> None:
        h = cv_img.shape[0]
        # draw a black rectangle
        cv2.rectangle(_cv_img, pt1=(5, h - 25), pt2=(250, h - 5), color=pyplt.get_BGR_color('black'), thickness=-1)
        text_color = 'g' if _color in ['black', 'k'] else _color  # rect is black so don't allow black text color
        # add info text on the rect
        add_text(_cv_img, header='{}: {}'.format(_name, _color), pos=(5, h - 9), text_color=text_color, with_rect=False)
        return

    title = "select_roi:img shape {}('d' to delete last,'q' to finish). names={}, colors={}".format(cv_img_temp.shape,
                                                                                                    names, colors)

    cv2.namedWindow(title)
    cv2.setMouseCallback(title, get_roi_xy2)
    draw_next_info(cv_img_temp, _name=names[current_idx], _color=colors[current_idx])

    for i in range(10 ** 10):
        k = display_open_cv_image(cv_img_temp, title=title, ms=1, loc='tl', resize=resize)
        if k == ord('d'):  # delete last selection
            if len(named_points) > 0:
                cv_img_temp = cv_img_clean.copy()  # delete all
                last_idx = current_idx - 1
                last_name = names[last_idx]
                del named_points[last_name]
                current_idx -= 1  # set the pointer one back
                draw_next_info(cv_img_temp, _name=names[current_idx], _color=colors[current_idx])
                for name, c_xy_dict in named_points.items():  # draw the the remaining colors
                    c, d2p = c_xy_dict['c'], c_xy_dict['xy']
                    draw_x(cv_img_temp, x_center_xy=d2p, x_color=c, pixels=20,
                           add_center_text=add_center_text, text_color=None, text_up=True)
        if k == ord('q'):
            break
    cv2.destroyAllWindows()
    return named_points
