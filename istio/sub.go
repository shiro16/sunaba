package main

import (
	"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Istio Example sub application")
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":3001", nil)
}
