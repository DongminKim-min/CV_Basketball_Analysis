# from ultralytics import YOLO

# model = YOLO("models/ball_detector_model.pt")

# results = model.track("input_videos/video_1.mp4", save = True)
# print(results)
# print("===================")
# for box in results[0].boxes:
#     print(box)

# ===============================================================

from utils import read_video, save_video
from trackers import PlayerTracker
from drawers import PlayerTracksDrawer
 
def main():
    # Read Videos
    video_frames = read_video("input_videos/nba_clip_high_angle.mp4")
    print(f"Number of frames: {len(video_frames)}\n")

    # Initialize Tracker
    player_tracker = PlayerTracker("models/player_detector.pt")

    # Run Trackers
    player_tracks = player_tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path="stubs/player_track_stubs2.pkl")

    # Draw Output
    # Initialize Drawers
    player_tracks_drawer = PlayerTracksDrawer()
    output_video_frames = player_tracks_drawer.draw(video_frames, player_tracks)

    # Save Videos
    save_video(output_video_frames, "output_videos/output_nba_clip_high_angle.avi")

    print("Output Video Saved.\n")

if __name__ == "__main__":
    main()