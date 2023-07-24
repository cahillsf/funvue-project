#!/bin/bash
echo "Starting build"

while getopts r:t:i:p:d: flag
do
    case "${flag}" in
        r) repo=${OPTARG};;
        t) tag=${OPTARG};;
        i) image_name=${OPTARG};;
        p) path=${OPTARG};;
        d) dockerfilepath=${OPTARG};;
    esac
done
echo "Repo: $repo";
echo "Tag: $tag";
echo "Image Name: $image_name";
echo "Path: $path";

docker build -f $dockerfilepath -t $image_name:$tag $path
docker image tag $image_name:$tag $repo/$image_name:$tag
docker image push $repo/$image_name:$tag