package main

import (
	"fmt"
	"image"
	"image/jpeg"
	"os"
)

type SubImager interface {
	SubImage(r image.Rectangle) image.Image
}

func main() {
	f, err := os.Open("test.jpg")
	if err != nil {
		fmt.Println("open:", err)
		return
	}
	defer f.Close()

	img, _, err := image.Decode(f)
	if err != nil {
		fmt.Println("decode:", err)
		return
	}

	fso, err := os.Create("out.jpg")
	if err != nil {
		fmt.Println("create:", err)
		return
	}
	defer fso.Close()

	cimg := img.(SubImager).SubImage(image.Rect(50, 0, 150, 100))

	jpeg.Encode(fso, cimg, &jpeg.Options{Quality: 100})
}
