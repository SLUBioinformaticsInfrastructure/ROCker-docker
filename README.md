# ROCker: a docker

```bash
docker run --rm -it -v ~/Documents/mg_data/:/data/ rocker head /data/I-3_S46_L008_R1_001.fasta

docker run --rm -it -v ~/Documents/mg_data/:/data/ rocker ROCker search -i /data/I-3_S46_L008_R1_001.fasta \
                                                                        -k /home/rocker/rocker_exec/models/AmoA/AmoA_A.125.rocker \
                                                                        -o /data/I-3_S46_L008_R1_001_diamond.out \
                                                                        --search diamond \
                                                                        -t 3

docker run --rm -it -v ~/Documents/mg_data/:/data/ rocker head /data/I-3_S46_L008_R1_001.fasta > /data/file.head

docker run --rm -it -v ~/Documents/mg_data/:/data/ rocker python /home/rocker/test.py /data/I-3_S46_L008_R1_001.fasta /data/file.head

docker run --rm -it -v ~/Documents/mg_data/:/data/ rocker ROCker build -P /data/tatc.id -o prep -t 4 --aligner muscle --search diamond
```
