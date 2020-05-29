package main

import (
	"fmt"
	"golang.org/x/image/draw"
	"image"
	"image/color"
	"image/jpeg"
	"os"
)

type SubImager interface {
	SubImage(r image.Rectangle) image.Image
}

type Image interface {
	image.Image
	Set(x, y int, c color.Color)
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

	f2, _ := os.Open("hoge.jpg")
	img2, _, _ := image.Decode(f2)

	rgba := image.NewRGBA(image.Rectangle{image.Point{0, 0}, image.Point{200, 200}})

	draw.Draw(rgba, image.Rectangle{image.Point{0, 0}, img2.Bounds().Size()}, img2, image.Point{0, 0}, draw.Src)

	rct := image.Rectangle{image.Point{25, 25}, img2.Bounds().Size()}

	draw.Draw(rgba, rct, img, image.Point{0, 0}, draw.Src)

	jpeg.Encode(fso, rgba, &jpeg.Options{Quality: 100})
}
