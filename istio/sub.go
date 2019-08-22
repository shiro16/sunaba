package main

import (
	//"fmt"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	//fmt.Fprintf(w, "Istio Example sub application")
	http.Error(w, "err", 503)
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":9081", nil)
}
