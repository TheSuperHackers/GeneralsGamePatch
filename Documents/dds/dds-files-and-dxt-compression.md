# DDS files and DXT compression

Source
https://w3dhub.com/forum/topic/417101-dds-files-and-dxt-compression/

## What is DXT?

DDS is a container format designed for texture data and can have different amounts of compression applied (including none). There are 3 major compression formats defined in the Direct3D 6 standard: DXT1, DXT3 and DXT5. These are also called BC1/2/3 ("Block Compression") respectively. Later versions added BC4/5 (D3D10) and BC6/7 (D3D11). Each of these have their own use cases and advantages, so higher numbers are not just "better" versions.

The advantage of these compression formats compared to something more common like JPEG is that they can be uploaded to the GPU directly and always stay fully compressed in GPU memory. With hundreds of megabytes of textures this adds up quickly and allows us to improve performance (less memory bandwidth used) and target lower end/older GPUs with less VRAM. The decompression is implemented directly in hardware and happens transparently on memory access. The key ingredient for this to work is that the format is made out of independent 4x4 blocks of pixels that can be decompressed individually instead of the entire texture at once.

A more thorough look at the details of the compression formats can be found here: http://www.reedbeta.com/blog/understanding-bcn-texture-compression-formats/

## Which Format to Use?

The DXT-Formats mostly differ in their handling of the alpha channel (usually used for transparency).

* Use BC1/DXT1 for pure RGB textures or hard "cut outs" which only need one bit of alpha (fully opaque or fully transparent; note that some tools have a separate mode for this called "DXT1A")
* Use BC2/DXT3 for RGBA textures with discrete "hard" alpha transitions (this format has 4 bits of alpha per pixel, so 16 different levels of transparency)
* Use BC3/DXT5 for RGBA textures with smooth interpolated alpha (use this over BC2 unless you're certain)

The data rate is constant regardless of image content: 4 bits per pixel for BC1 and BC4 and 8 bits per pixel for every other format. This means that BC1 should be used where applicable to save memory, don't forget the 1 bit of alpha comes (almost) free! BC2 use cases are rare, usually you probably want BC3. A nice overview of features and use cases for all BCn formats can be found here. Missing in this table is a particular trick for using DXT5 for better quality normal or bump maps explained here, also called DXT5nm or DXT5-xGxR and has direct support by a few tools (e.g. NVTT, see below).

The more modern BC4-7 formats should generally be avoided for now since the older Renegade-compatible W3D engine can't load them at all, W3D 5.0 (APB, AR and BFD) can't load them yet (though afaik it would be trivial to add support) and most importantly, 3ds Max and many other programs cannot open them (BCn App Support). Nevertheless, we might have a specific need for one of these formats in the future that warrants their use despite the tooling issues and we can always just use the uncompressed source texture for the .max files.

At some point in the future, I will specifically take a look at BC5 for optimum quality normal maps and general BC7 vs. BC3 quality since it should be tremendously better in most use cases at the same size. BC7 instead of BC1 should not be used frivolously due to being twice the size and also less amenable to further compression (e.g. zip) since it actually carries so much more information, but when you really need a near-lossless result, this will do it. Since the BC7 format is so much more complex, some encoders can take many hours for a single texture at high quality, but there are some faster ones out there (see below, so far I only tried Compressonator for BC7, will revisit this at some point).

## Which Exporter to Use?

This is where we get the reason why I wrote this post in the first place. I noticed some textures looking awfully blocky ingame with obviously off-color artifacts, which was caused by an extremely bad DXT encoder. I then set out to compare different compressors and stared at textures for hours (I also used PSNR metrics, but visual inspection was much more useful). In total I tested 7 different tools with two DXT1 textures we had uncompressed sources for.

First of all here's my personal ranking in terms of output quality:

* Crunch (https://github.com/Unity-Technologies/crunch/tree/unity/bin) tied with Nvidia Texture Tools
* Nvidia Texture Tools (NVTT, https://github.com/castano/nvidia-texture-tools)
* Compressonator (https://github.com/castano/nvidia-texture-tools)
* Nvidia Texture Tools for Adobe Photoshop (https://developer.nvidia.com/nvidia-texture-tools-adobe-photoshop)
* Paint.Net (https://www.getpaint.net/)
* ISPC Texture Compressor / Intel Texture Works Plugin for Photoshop (https://github.com/GameTechDev/ISPCTextureCompressor / https://github.com/GameTechDev/Intel-Texture-Works-Plugin)
* GIMP with DDS plug-in (https://www.gimp.org/ and https://code.google.com/archive/p/gimp-dds/downloads)
* DirectXTex (https://github.com/Microsoft/DirectXTex)
* DDS Converter (http://www.ddsconverter.com/ but I'd rather you throw it deep into the sea)

To motivate you to switch from a different tool, let me detail the issues encountered with the different encoders (comparison images are in the spoiler below).

No matter which tool you use, make sure it generates mipmaps unless it's a UI texture. Some will do this by default, some don't (Compressonator). Some tools also offer the ability to specify gamma/sRGB for mipmap generation. This should be set to sRGB/2.2 (default for most tools). If you're unsure about gamma, use a checkerboard texture to replace a terrain texture ingame, disable anisotropic filtering and look off into the distance, with proper gamma it should look about medium gray (with lighting taken into account), otherwise it will look darker (like here).

If you're working with tiled textures (terrain, walls), make sure you're telling the compressor so it doesn't break the smooth tiling (e.g. -wrap for Crunch, -repeat for NVTT), though the difference is usually minimal.

Crunch was originally developed for a more advanced purpose, so make sure you only use the command line options that produce a "normal" non-clustered output (in particular, do not use -bitrate or -quality). In terms of visual quality, it particularly excels at gradients and dark areas.

NVTT is very close overall, with Crunch displaying better performance on gradients, while NVTT beats it at high-frequency detail. Note: Do not use this tool for BC7, unless you want to literally wait for days for a single texture even with the "fast" encoding option.

Compressonator is one of the few tools to feature both a GUI and a command line interface, although the GUI can a bit weird to use. Make sure you generate mipmaps explicitly and set the quality to 1.0. In my experience the quality is always slightly behind Crunch/NVTT, but it's definitely not bad and it has been recommended a lot in the past. It can also compress to BC7 within a reasonable amount of time (35 seconds for a 4k texture with quality=0.05, though without comparison I can't speak for its visual quality).

Nvidia's Photoshop plugin for some reason continues to use a very old version of their texture tools (NVTT is basically a complete rewrite). It generally looks most similar to Crunch, suggesting a commonality in the algorithm used. However, it tends to produce some additional block artifacts on hard edges and has some more trouble with darker gradients. Overall it's still good enough to be okay to recommend, I'm just slightly disappointed that Nvidia doesn't update this plugin anymore.

Paint.Net is not terrible but very clearly behind the other options. Gradients and dark areas suffer from banding and block artifacts and some areas appear darker than in the source or have their hue shifted to a different color. The uneven gradients make the "block" structure of the compression very visible.

ISPC was a total disappointment. I thought it to be among the top tools, but on gradients (in particular darker ones) it just flat out fails and produces results comparable to the worst ones out of all tools with very extreme discoloration. Upsides are that it has good BC6/7 support and is very fast, so it may still be useful for these modes.

GIMP first disappoints with a "use perceptual error metric" option, which for unknown reasons makes the output worse rather than better. The output doesn't impress either way though, with even worse gradients and random hue shifts than Paint.Net. Surprisingly, it does fairly well at high-frequency detail, but that in no way makes up for its general poor performance.

DirectXTex from Microsoft may sound like a natural pick, but sadly it is one of the worst encoders I have seen so far. Simple flat areas turn into a blocky mess of different colors that weren't in the source at all, gradients look horrible, etc. As with GIMP, it does fairly well at high-frequency detail, but in doing so it introduces severe noise across the entire texture, sometimes looking a little bit like the JPEG artifacts we all know and love. This compressor also supports BC7, so I may come back to it in the future.

DDS Converter I haven't tested directly, but it was the source of the problems that caused me to investigate this issue in the first place. The quality is just godawful, in some parts it almost feels like the texture is lower resolution than it really is because entire 4x4 blocks share the same color for no particular reason, and it's not even the correct color! In addition, some detail introduces harsh artifacts and noise. I weep for all the people googling for "dds converter" and having to put up with shit quality textures because of this tool.
