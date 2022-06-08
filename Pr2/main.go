package main

import (
	"bufio"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"log"
	"os"
	"runtime"
	"sync"
	"time"
)

func readFile() {
	var waitGroup sync.WaitGroup
	file, err := os.Open("dict.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	fmt.Println(time.Now())
	for scanner.Scan() {
		if runtime.NumGoroutine() > 100 {
			waitGroup.Wait()
		}
		waitGroup.Add(1)
		go hashPassword(&waitGroup, scanner.Text())
	}
	waitGroup.Wait()
	fmt.Println(time.Now())

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}

func hashPassword(wg *sync.WaitGroup, str string) {
	defer wg.Done()
	data := []byte(str)
	hash := sha256.Sum256(data)
	comparisonHashes(hash[:], str)

}

var hashesArray = [3]string{
	"1115dd800feaacefdf481f1f9070374a2a81e27880f187396db67958b207cbad",
	"3a7bd3e2360a3d29eea436fcfb7e44c735d117c42d1c1835420b6b9942dd4f1b",
	"74e1bb62f8dabb8125a58852b63bdf6eaef667cb56ac7f7cdba6d7305c50a22f",
}

func comparisonHashes(hash []byte, password string) {

	for i := 0; i < len(hashesArray); i++ {
		if hashesArray[i] == hex.EncodeToString(hash[:]) {
			fmt.Println("password: ", password)
		}
	}
}

func main() {
	readFile()
}
