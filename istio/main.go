package main

import (
	"fmt"
	"net/http"
	"io/ioutil"
)

func handler(w http.ResponseWriter, r *http.Request) {
	resp, err := http.Get("http://istio-example-app-sub-svc:9081")

	if err != nil {
		fmt.Println(err)
		return
	}

	defer resp.Body.Close()

	bodyBytes, err := ioutil.ReadAll(resp.Body)
    if err != nil {
		fmt.Println(err)
		return
    }

	fmt.Fprintf(w, "sub application response: "+string(bodyBytes))
}

func main() {
	http.HandleFunc("/", handler)
	http.ListenAndServe(":9080", nil)
}
