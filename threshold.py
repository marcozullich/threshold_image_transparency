import cv2
import numpy as np
import argparse
import os

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--img_in", type=str, required=True, help="/path/to/input_img")
    parser.add_argument("--thresh", type=int, default=100, help="Color intensity for image thresholding (default 100).")
    parser.add_argument("--img_out", type=str, required=True, help="/path/to/output_img")
    parser.add_argument("--resize_factor", type=float, default=1.0, help="Optional resizing factor")
    args = parser.parse_args()

    img = cv2.imread(args.img_in)
    if args.resize_factor is not None or args.resize_factor < 1.0:
        shape = tuple((np.array(img.shape[:2]) * args.resize_factor).astype("int32"))
        print(f"Old shape {img.shape[:2]} new shape {shape}")
        img = cv2.resize(img, (shape[1], shape[0]), interpolation = cv2.INTER_LANCZOS4)
    img_bin = cv2.threshold(
                cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                args.thresh, 255, cv2.THRESH_BINARY)[1]
    img_col = cv2.cvtColor(img_bin, cv2.COLOR_GRAY2BGR)
    blue, green, red = cv2.split(img_col)
    # alpha channel: 0 where white, 255 where black
    alpha = np.where(img_bin==0,255,0).astype("uint8")

    img_BGRA = cv2.merge((blue, green, red, alpha))
    cv2.imwrite(args.img_out, img_BGRA)
    print(f"Saved to {os.path.abspath(args.img_out)}")