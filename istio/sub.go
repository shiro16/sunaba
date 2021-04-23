package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Request Start")
	http.Error(w, "err", 503)
}

func main() {
	http.HandleFunc("/sub", handler)
	http.ListenAndServe(":9081", nil)
}
