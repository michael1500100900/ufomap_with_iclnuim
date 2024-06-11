# Testy systemu do budowy map UFOMap na zbiorach danych z kamer RGB-D.

## Celem projektu jest uruchomienie systemu [UFOMap](https://github.com/UnknownFreeOccupied/ufomap) na podstawie instrukcji znajdujących się na Github i przetestowanie na zbiorach danych z kamer RGB-D np [ICL-NUIM](https://www.doc.ic.ac.uk/~ahanda/VaFRIC/iclnuim.html).

### Aby uruchomić projekt należy wykonać poniższe kroki i polecenia w terminalu:
### Dodatkowe kroki przy pierwszym uruchomieniu:
1. Stworzenie kontenera o nazwie ros_ufo_map:<br/>
   ```
   sudo docker run -it --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" --name ros_ufo_map ros:noetic-desktop-full \
   ```
2. Następnie uruchamiamy poleceniem:<br/>
   ```
   sudo docker start ros_ufo_map && sudo docker exec -it ros_ufo_map bash && source /opt/ros/noetic/setup.bash
   ```
3. Tworzymy ROS Workspace, tworząc i budując catkin workspace, używając po kolei następujących poleceń:<br/>
   ```
   mkdir -p ~/catkin_ws/src
   cd ~/catkin_ws/
   catkin_make
   source devel/setup.bash
   ```
4. Instalacja niezbędnych paczek:
    - ros-noetic-map-server:<br/>
      ```
      sudo apt-get install ros-noetic-map-server ros-noetic-dwa-local-planner
      ```
    - biblioteka Octomap:<br/>
      ```
      sudo apt-get install ros-noetic-octomap ros-noetic-octomap-server
      ```
    - model Turtlebota:<br/>
      ```
      sudo apt-get install ros-noetic-turtlebot3*
      ```
    - repozytorium zawierające skrypty konfiguracyjne i przykładowe mapy:
      ```
      cd ~/catkin_ws/src
      git clone https://github.com/dominikbelter/example_maps
      sudo rosdep init
      rosdep update
      ```
    - UFOMap:
      ```
      sudo apt install libtbb-dev
      cd ~/catkin_ws/src
      git clone https://github.com/UnknownFreeOccupied/ufomap.git
      rosdep install --from-paths . --ignore-src -r -y
      catkin build
      source ../devel/setup.bash
      ```
   
6. Pobranie niniejszego repozytorium i skompilowanie przestrzeni roboczej:<br/>
   ```
   cd ~/catkin_ws/src
   git clone https://github.com/michael1500100900/ufomap_with_iclnuim/
   cd ~/catkin_ws/
   catkin_make
   ```

### Kroki niezbędne przy każdym następnym uruchomieniu:
1. W pierwszym terminalu należy uruchomić roscore i zostawić w tle:<br/>
   ```
   xhost +local:root && sudo docker start ros_ufo_map && sudo docker exec -it ros_ufo_map bash && source /opt/ros/noetic/setup.bash
   ```
   ```
   roscore
   ```
2. W drugim (nowym) terminalu należy uruchomić OctoMap / UFOMap i zostawić uruchomione:<br/>
    - OctoMap:<br/>
       ```
       sudo docker exec -it ros_ufo_map bash && source /opt/ros/noetic/setup.bash
       ```
       ```
       cd ~/catkin_ws/src && catkin build && source ../devel/setup.bash
       ```
       ```
       roslaunch example_maps turtlesim3_waffle_octomap.launch
       ```   
    - UFOMap:<br/>
       ```
       sudo docker exec -it ros_ufo_map bash && source /opt/ros/noetic/setup.bash
       ```
       ```
       cd ~/catkin_ws/src && catkin build && source ../devel/setup.bash
       ```
       ```
       roslaunch ufomap_mapping server.launch
       ```
3. W trzecim (następnym) terminalu należy uruchomić RViz:
   ```
   sudo docker exec -it ros_ufo_map bash && source /opt/ros/noetic/setup.bash
   ```
   ```
   cd ~/catkin_ws/src && catkin build && source ../devel/setup.bash
   ```
   ```
   rosrun rviz rviz
   ```

> [!IMPORTANT]
> Disclaimer1: Nie wszystkie pliki z repozytorium są bezpośrednio wykorzystywane, ale były one wykorzystywane lub są też rozwiązaniami i pomysłami, które okazały się być ślepymi ścieżkami.

> [!IMPORTANT]
> Disclaimer2: Oryginalne pliki Data-Setu RGB-d ICL-NUIM oraz przekonwertowane na .bt i .pcd znajdują się na [dysku](https://drive.google.com/drive/folders/1aPyMmg4-4i7JuuM6qhULwWOQIY4SdHPU?usp=sharing) do celów poglądowych i żeby nie zaśmiecać tego repozytorium.
