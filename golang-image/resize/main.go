package main

import (
	"flag"
	"fmt"
	"image"
	"image/jpeg"
	"os"
	"strconv"
	"golang.org/x/image/draw"
)

func main() {
	flag.Parse()
	args := flag.Args()

	f, err := os.Open(args[0])
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

	fso, err := os.Create(args[1])
	if err != nil {
		fmt.Println("create:", err)
		return
	}
	defer fso.Close()

	arg, _ := strconv.ParseFloat(args[2], 64)

	rct := img.Bounds()

	var w, h int
	if rct.Dx() > rct.Dy() { // 横長画像
		m := arg / float64(rct.Dx())
		w = int(arg)
		h = int(float64(rct.Dy()) * m)
	} else { // 縦長画像
		m := arg / float64(rct.Dy())
		w = int(float64(rct.Dx()) * m)
		h = int(arg)
	}

	dst := image.NewRGBA(image.Rect(0, 0, w, h))
	draw.CatmullRom.Scale(dst, dst.Bounds(), img, rct, draw.Over, nil)

	jpeg.Encode(fso, dst, &jpeg.Options{Quality: 100})
}
