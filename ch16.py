import streamlit as st
import SimpleITK as sitk
import matplotlib.pyplot as plt
import numpy as np

# Function to display a 2D slice of the segmentation
def display_slice(image, segmentation, slice_index):
    # Extract the 2D slice from the 3D image and segmentation
    image_slice = image[:, :, slice_index]
    segmentation_slice = segmentation[:, :, slice_index]

    # Plot the image and segmentation overlay
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    ax[0].imshow(image_slice, cmap='gray')
    ax[0].set_title("CT Image")

    ax[1].imshow(image_slice, cmap='gray')
    ax[1].imshow(segmentation_slice, cmap='Reds', alpha=0.3)  # Overlay segmentation in red
    ax[1].set_title("Spleen Segmentation Overlay")

    st.pyplot(fig)

# Streamlit interface for uploading and visualizing the segmentation
st.title("Spleen Segmentation Visualization")

# Upload .nii file (image)
#uploaded_image = st.file_uploader("Upload CT Image (.nii file)", type=["nii", "gz"])

# Upload .nii file (segmentation)
#uploaded_segmentation = st.file_uploader("Upload Segmentation Result (.nii file)", type=["nii", "gz"])

#if uploaded_image and uploaded_segmentation:
# Load image and segmentation using SimpleITK
image = sitk.ReadImage("Medical Decathlon Spleen/148/artifactFiles/imagesTr/spleen_10.nii.gz")
segmentation = sitk.ReadImage("Medical Decathlon Spleen/148/artifactFiles/labelsTr/spleen_10.nii.gz")

# Convert to numpy arrays for visualization
image_np = sitk.GetArrayFromImage(image).T
segmentation_np = sitk.GetArrayFromImage(segmentation).T

# Choose slice index to visualize
slice_index = st.slider("Choose Slice Index", 0, image_np.shape[2] - 1, image_np.shape[2] // 2)

# Display the selected slice with segmentation overlay
display_slice(image_np, segmentation_np, slice_index)