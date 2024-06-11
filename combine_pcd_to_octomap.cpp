#include <octomap/octomap.h>
#include <octomap/Pointcloud.h>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <boost/filesystem.hpp>
#include <iostream>

namespace fs = boost::filesystem;

int main(int argc, char** argv) {
    // Upewnij się, że przekazano ścieżkę do katalogu z plikami PCD
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <directory_with_pcd_files>" << std::endl;
        return -1;
    }

    fs::path pcd_dir = argv[1];
    pcl::PointCloud<pcl::PointXYZ>::Ptr combined_cloud(new pcl::PointCloud<pcl::PointXYZ>());

    // Przechodzimy przez wszystkie pliki PCD w katalogu i łączymy chmury punktów
    int file_count = 0;
    for (const auto& entry : fs::directory_iterator(pcd_dir)) {
        if (entry.path().extension() == ".pcd") {
            pcl::PointCloud<pcl::PointXYZ>::Ptr cloud(new pcl::PointCloud<pcl::PointXYZ>());
            std::cout << "Loading file: " << entry.path().string() << std::endl;
            if (pcl::io::loadPCDFile<pcl::PointXYZ>(entry.path().string(), *cloud) == -1) {
                PCL_ERROR("Couldn't read file %s\n", entry.path().string().c_str());
                continue;
            }
            *combined_cloud += *cloud; // Łączenie chmur punktów
            file_count++;
        }
    }

    std::cout << "Loaded " << file_count << " files." << std::endl;

    // Konwersja połączonej chmury punktów do formatu OctoMap
    octomap::Pointcloud octoCloud;
    for (const auto& point : combined_cloud->points) {
        octoCloud.push_back(point.x, point.y, point.z);
    }

    // Stworzenie Octree i wstawienie połączonej chmury punktów
    octomap::OcTree tree(0.1); // Rozdzielczość octree
    std::cout << "Inserting point cloud into Octree..." << std::endl;
    tree.insertPointCloud(octoCloud, octomap::point3d(0, 0, 0));

    // Zapisanie Octree do pliku
    tree.writeBinary("output.ot");

    std::cout << "OctoMap created and saved to output.ot" << std::endl;

    return 0;
}
