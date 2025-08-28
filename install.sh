yes | conda update -n base -c defaults conda
yes | conda create --name pydeq --file spec-file.txt
conda activate pydeq
