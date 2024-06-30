#!/bin/python
import mitsuba as mi
import drjit as dr

try: 
    mi.set_variant('cuda_ad_rgb')
except:
    print("CUDA doesn't seem to be available. Running on CPU.")
    mi.set_variant('scalar_rgb')

scene = mi.load_file("scene.xml")

# Low res image with a lot of static
spp_low = 256
print(f"Rendering low res image. Samples per pixel = {spp_low}")
image = mi.render(scene, spp=spp_low)
mi.util.write_bitmap(f"mitsuba_render_spp{spp_low}.png", image)

if mi.variant() == 'cuda_ad_rgb':
    # Higher res image
    print("Rendering low res image. This should take less than 3 minutes on an RTX 3060 Ti if you increase the resolution to 1024 x 720.")
    spp_high = 2000
    image_highres = mi.render(scene, spp=spp_high)
    mi.util.write_bitmap(f"mitsuba_render_spp{spp_high}.png", image_highres)
