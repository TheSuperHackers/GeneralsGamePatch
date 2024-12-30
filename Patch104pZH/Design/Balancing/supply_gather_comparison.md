# Supply Gather Comparison

This document presents the results of a comparison between different supply gather methods in *Generals: Zero Hour*.
The methods tested include **China Trucks** (regular trucks), **USA Chinooks**, and **GLA Workers**. The goal was
to determine the time required to exhaust a supply stash of 30,000 from a Supply Depot after its construction.

## Test Setup
- **Start Time**: The timer started as soon as the Supply Depot was completed.
- **Next Gatherer(s)**: New gatherer(s) were constructed immediately after the Supply Depot was finished.
- **Stop Time**: The timer stopped as soon as the last money was dropped into the Supply Depot.

## Test Results

### Efficient Supply

| Unit Type                   | Supply Depot Finished           | Supply Stash Exhausted          | Total Time (Frames)             | Total Time (Seconds)            |
|-----------------------------|---------------------------------|---------------------------------|---------------------------------|---------------------------------|
| 2 Original China Trucks     | 00:01:57.24 (3534)              | 00:12:23.14 (22304)             | 18,770                          | 625                             |
| 2 Reverse Gear China Trucks | Same as 2 Original China Trucks | Same as 2 Original China Trucks | Same as 2 Original China Trucks | Same as 2 Original China Trucks |
| 2 USA Chinooks              | 00:01:19.10 (2380)              | 00:12:09.03 (21873)             | 19,493                          | 645                             |
| 6 GLA Workers               | 00:00:38.07 (1147)              | 00:11:56.07 (21487)             | 20,340                          | 678                             |

### Poor Supply

| Unit Type                   | Supply Depot Finished | Supply Stash Exhausted | Total Time (Frames) | Total Time (Seconds) | Penalty (Frames) | Penalty (Seconds) | Penalty (%) |
|-----------------------------|-----------------------|------------------------|---------------------|----------------------|------------------|-------------------|-------------|
| 2 Original China Trucks     | 00:00:47.12 (1422)    | 00:13:21.05 (24035)    | 22,613              | 754                  | 3,843            | 128               | 17%         |
| 2 Reverse Gear China Trucks | 00:01:11.26 (2156)    | 00:11:39.20 (20990)    | 18,834              | 628                  | 64               | 2                 | 0.3%        |
| 2 USA Chinooks              | 00:00:49.17 (1487)    | 00:11:52.16 (21376)    | 19,889              | 663                  | 396              | 13                | 2%          |
| 6 GLA Workers               | 00:00:42.18 (1278)    | 00:12:40.20 (22820)    | 21,542              | 718                  | 1,202            | 40                | 5.5%        |

## Reference Images

### Efficient Supply
![Efficient Supply China](https://user-images.githubusercontent.com/4720891/183183732-02dcd8ad-beb3-4d0c-a8bc-eb91ca1a77c7.jpg)
![Efficient Supply USA](https://user-images.githubusercontent.com/4720891/183184549-96f1e86c-3724-4ef4-a229-5992656eb94c.jpg)
![Efficient Supply GLA](https://user-images.githubusercontent.com/4720891/183184948-80bc3b4c-a9cf-4482-ad9a-3fd3de96a2eb.jpg)

### Poor Supply
![Poor Supply China](https://user-images.githubusercontent.com/4720891/183187094-7e050629-4ce9-4711-a669-c66adb640bfb.jpg)
![Poor Supply USA](https://user-images.githubusercontent.com/4720891/183186165-fd838d57-2544-4845-8c9c-cc3a180034ef.jpg)
![Poor Supply GLA](https://user-images.githubusercontent.com/4720891/183185632-c21b71ed-32c4-418f-b66d-40c8980981aa.jpg)
