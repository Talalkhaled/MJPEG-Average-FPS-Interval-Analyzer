# MJPEG-Average-FPS-Interval-Analyzer

**Author:** Talal Khaled Alharbi  
**Date:** 12 Mar. 2025  

This file serves as an **MJPEG-Streamer viewer**, a lightweight JavaScript-based tool designed to estimate the **FPS (frames per second)** of an MJPEG stream using the **average frame interval method**. It calculates FPS by measuring the time difference between consecutive frame loads and averaging over a rolling buffer of recent intervals.  

## Prerequisites  
This project depends on **MJPEG-Streamer**, an open-source command-line tool that streams JPEG files over an IP-based network from a webcam to a viewer.  

To use this program, **clone the following GitHub repository**:  
🔗 [MJPEG-Streamer Repository](https://github.com/jacksonliam/mjpg-streamer)  

To start streaming on a Linux system, execute the following command on the **streaming machine** using MJPEG-Streamer:  

```bash
mjpg_streamer -i "<UVC_INPUT_PLUGIN> -d <DRIVER_PATH> -r <CAMERA_RESOLUTION> -f <FRAME_RATE>" -o "output_http.so -w ./www -p 8080"
```

## Warnings  
- This repository **demonstrates** the technique of calculating **received FPS** using a **rolling window method**. It is intended for educational and testing purposes only.  
- The provided Linux command **streams video to the local network** **without authentication**. This means **any device on the network** can access the stream. Use caution when deploying in an unsecured environment.
