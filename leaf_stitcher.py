import cv2
import os
import glob
import sys

def stitch_leaf_segments(input_folder, output_filename="full_leaf_montage.jpg"):
    print(f"--- Starting Assembly for {input_folder} ---")

    # 1. Load Images
    # We look for common formats. You can add .tif if your microscope outputs that.
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
    image_paths = []
    for ext in extensions:
        image_paths.extend(glob.glob(os.path.join(input_folder, ext)))
    
    if not image_paths:
        print("Error: No images found in the folder.")
        return

    print(f"Found {len(image_paths)} segments. Loading...")

    images = []
    for path in image_paths:
        img = cv2.imread(path)
        if img is not None:
            images.append(img)
        else:
            print(f"Warning: Could not load {path}")

    # 2. Initialize the Stitcher
    # mode=1 is cv2.Stitcher_SCANS. 
    # This is CRITICAL for microscopy. It assumes the image is flat 
    # and we are mostly dealing with x,y translation, not 3D rotation.
    stitcher = cv2.Stitcher_create(mode=cv2.Stitcher_SCANS)

    # 3. Perform Stitching
    print("Stitching images... This may take a moment based on resolution.")
    status, stitched_image = stitcher.stitch(images)

    # 4. Check Results and Save
    if status == cv2.Stitcher_OK:
        print("Success! Stitching complete.")
        cv2.imwrite(output_filename, stitched_image)
        print(f"Full leaf assembly saved as: {output_filename}")
        
        # Optional: Resize for display if the result is massive
        h, w = stitched_image.shape[:2]
        print(f"Final Resolution: {w}x{h} pixels")
    else:
        # Error handling codes
        error_message = {
            cv2.Stitcher_ERR_NEED_MORE_IMGS: "Not enough images.",
            cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL: "Homography estimation failed (Could not find matching points).",
            cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL: "Camera parameter adjustment failed."
        }.get(status, f"Unknown error code: {status}")
        
        print(f"Stitching failed. Reason: {error_message}")
        print("Tip: Ensure there is at least 30% overlap and distinct texture in the images.")

# --- Execution ---
if __name__ == "__main__":
    # Ensure the folder exists before running
    target_folder = 'leaf_segments'
    
    if os.path.exists(target_folder):
        stitch_leaf_segments(target_folder)
    else:
        print(f"Please create a folder named '{target_folder}' and put your images inside.")