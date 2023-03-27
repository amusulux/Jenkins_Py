import os, time

images_before = os.popen("sudo docker images").read().strip().split("\n")[1:]
print(images_before)
os.popen("sudo docker build -t ubuntu:v1 home/remlab/Desktop/jenkin_agent/workspace/Sample_commit_project")
time.sleep(5)
images_after = os.popen("sudo docker images").read().strip().split('\n')[1:]
print(images_after)
if len(images_before) >= len(images_after):
    raise Exception("Image creation was unsuccessful")