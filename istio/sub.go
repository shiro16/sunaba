package main

import (
	"fmt"
	"time"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	time.Sleep(time.Second * 2)
	fmt.Fprintf(w, "Istio Example sub application")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":9081", nil)
}
