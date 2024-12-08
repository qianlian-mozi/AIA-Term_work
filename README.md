# AIA-Term_work

This is an AIA final assignment. Our team members are: **YirenQIU and Ghous**; we chose *task 2* --- *Create your own object detection algorithm, and compare the results w.r.t. a pre-trained YOLO model*.

We chose to modify the neck part of RT-DETR and replace it with the GSConv module to reduce the amount of calculation and thus reduce the complexity of the model.

We provide the following reports:
- A presentation PPT file, currently only lacking experimental comparison and analysis(We hope this could be helpful for beginners understanding the use of ultralytics' source codes easier, about ***where are the source codes exist***, ***why the configuration looks like that and how to format***, ***where and how to register your design's extra_module***...)
- The source code of the modified model --- GSconv-rtdetr based on Ultralytics platform 2024.11.28
- Data report on the modified model --- GSconv-rtdetr on visdrone 2024.11.28

The repository will keep in updating in the future.
