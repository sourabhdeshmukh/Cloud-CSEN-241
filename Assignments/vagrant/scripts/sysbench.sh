#!/bin/bash

usage="$(basename "$0") [-h] [-s n] -- program to calculate the answer to life, the universe and everything

where:
    -h  show this help text"


while getopts ':h:' option; do
  case "$option" in
    h) echo "\n$usage"
       exit
       ;;
    :) printf "\nmissing argument for -%s !!!\n\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
   \?) printf "\nillegal option: -%s !!!\n\n" "$OPTARG" >&2
       echo "$usage" >&2
       exit 1
       ;;
  esac
done
shift $((OPTIND - 1))

PRIMES_UPTO=("20000" "200000")
TEST_MODE=("rndwr" "seqrewr")
TEST_RUNS=5
TEST_CASES=2
LogFile="/tmp/sysbench.log"
CPULogFile="/tmp/cpu_sysbench.log"
FILEIPLogFile="/tmp/fileio_sysbench.log"
MEMORYLogFile="/tmp/memory_sysbench.log"

for ((i=0; i<$TEST_CASES;i++))
do
  echo `date` "[INFO] Starting ${i+1} Test Case." | tee -a $LogFile
	for (( j=1; j <=$TEST_RUNS; j++ ))
	do
		echo `date` "[INFO] Running ${j} run of CPU Test Case ${i+1}" | tee -a $CPULogFile
    sysbench cpu --threads=1 --cpu-max-prime=${PRIMES_UPTO[$i]} --time=5  run | tee -a $CPULogFile

    if [ $? -ne 0 ]; then
      echo `date` "[ERROR] Error occured while performing ${i+1} CPU test case." | tee -a $CPULogFile
      exit 1
    else
		  echo `date`"[INFO] Completed ${j} run of CPU Test Case ${i+1}" | tee -a $CPULogFile
    fi
 
    echo `date` "[INFO] Running ${j} run of FILEIO Test Case ${i+1}" | tee -a $FILEIOLogFile
    sudo sync; echo 3 > /proc/sys/vm/dropcaches
    sysbench --threads=2 fileio --file-total-size=1G --file-test-mode=${TEST_MODE[$i]} prepare | tee -a $FILEIOLogFile
    sysbench --threads=2 fileio --file-total-size=1G --file-test-mode=${TEST_MODE[$i]} run | tee -a $FILEIOLogFile
    sysbench --threads=2 fileio --file-total-size=1G --file-test-mode=${TEST_MODE[$i]} cleanup | tee -a $FILEIOLogFile

    if [ $? -ne 0 ]; then
      echo `date` "[ERROR] Error occured while performing ${i+1} FILEIO test case." | tee -a $FILEIOLogFile
      exit 1
    else
		  echo `date`"[INFO] Completed ${j} run of FILEIO Test Case ${i+1}" | tee -a $FILEIOLogFile
    fi

    sysbench memory --memory-block-size=${MEMBLOCK[$i]} --memory-scope=global --threads=2 --time=10 run | tee -a $MEMORYLogFile
  
    if [ $? -ne 0 ]; then
      echo `date` "[ERROR] Error occured while performing ${i+1} Memory test case." | tee -a $MEMORYLogFile
      exit 1
    else
		  echo `date`"[INFO] Completed ${j} run of Memory Test Case ${i+1}" | tee -a $MEMORYLogFile
    fi
     
	done
	echo `date` "[INFO] Completed ${i+1} Test Case." | tee -a $LogFile
  echo "" | tee -a $LogFile
done


