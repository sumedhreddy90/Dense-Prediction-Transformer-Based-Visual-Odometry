import glob
import os
import cv2
import argparse


class KITTI:
    def __init__(self,
                 data_path=r"/dataset/sequences",
                 pose_path=r"/dataset/poses",
                 sequence="00",
                 camera_id="0",
                 ):
        """
        Dataloader for KITTI Visual Odometry Dataset (grayscale images)
            http://www.cvlibs.net/datasets/kitti/eval_odometry.php

        Arguments:
            data_path {str}: path to data sequences (default: "dataset/sequences")
            pose_path {str}: path to poses (default: "dataset/poses")
            sequence {str}: sequence to be tested (default: "00") (options: "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10")
        """
        self.data_path = data_path # path to data sequences
        self.sequence = sequence # sequence to be tested
        self.camera_id = camera_id # camera id (0 for left, 1 for right)
        self.frame_id = 0 # frame index

        # Read ground truth poses for the sequence
        with open(os.path.join(pose_path, sequence+".txt")) as f:
            self.poses = f.readlines() # list of ground truth poses

        # Get frames list for the sequence
        frames_dir = os.path.join(data_path, sequence, "image_{}".format(camera_id), "*.png") # path to frames
        self.frames = sorted(glob.glob(frames_dir)) # list of frames

        # Camera Parameters (from calib.txt)
        self.cam_params = {} # dictionary containing camera parameters
        frame = cv2.imread(self.frames[self.frame_id], 0) # read first frame
        self.cam_params["width"] = frame.shape[0] # image width
        self.cam_params["height"] = frame.shape[1] # image height
        self.read_intrinsics_param() # read camera intrinsics parameters
 
    def __len__(self):
        return len(self.frames) # number of frames in the sequence

    def get_next_data(self):
        """
        Returns:
            frame {ndarray}: image frame at index self.frame_id
            pose {list}: list containing the ground truth pose [x, y, z]
            frame_id {int}: integer representing the frame index
        """
        # Read frame as grayscale
        frame = cv2.imread(self.frames[self.frame_id], 0) # read frame
        self.cam_params["width"] = frame.shape[0] # update image width
        self.cam_params["height"] = frame.shape[0] # update image height
 
        # Read poses
        pose = self.poses[self.frame_id] # read pose
        pose = pose.strip().split() # split pose
        pose = [float(pose[3]), float(pose[7]), float(pose[11])]  # coordinates for the left camera
        frame_id = self.frame_id # frame index
        self.frame_id = self.frame_id + 1 # update frame index
        return frame, pose, frame_id # return frame, pose and frame index



    def read_intrinsics_param(self):
        """
        Reads camera intrinsics parameters

        Returns:
            cam_params {dict}: dictionary with focal lenght and principal point
        """
        calib_file = os.path.join(self.data_path, self.sequence, "calib.txt") # path to calib.txt
        with open(calib_file, 'r') as f:
            lines = f.readlines()
            line = lines[int(self.camera_id)].strip().split() # read line for the left camera
            [fx, cx, fy, cy] = [float(line[1]), float(line[3]), float(line[6]), float(line[7])] # read camera parameters

            # focal length of camera
            self.cam_params["fx"] = fx
            self.cam_params["fy"] = fy
            # principal point (optical center)
            self.cam_params["cx"] = cx
            self.cam_params["cy"] = cy


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-d", "--data_path",
        default=r"/dataset/sequences",
        help="path to dataset"
    )
    parser.add_argument(
        "-s",
        "--sequence",
        default="03",
        help="sequence to be evaluated",
    )
    parser.add_argument(
        "-p",
        "--pose_path",
        default=r"/dataset/poses",
        help="path to ground truth poses",
    )

    args = parser.parse_args() # parse arguments

    # Create dataloader
    dataloader = KITTI(
        data_path=args.data_path,
        pose_path=args.pose_path,
        sequence=args.sequence,
    )

    dataloader.read_intrinsics_param() # read camera intrinsics parameters


