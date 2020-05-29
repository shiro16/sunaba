package main

import (
	"flag"
	"fmt"
	"github.com/chai2010/webp"
	"image"
	"image/gif"
	"image/jpeg"
	"image/png"
	"os"
	"strings"
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

	slice := strings.Split(args[1], ".")

	switch slice[len(slice)-1] {
	case "jpeg", "jpg":
		jpeg.Encode(fso, img, &jpeg.Options{})
	case "png":
		png.Encode(fso, img)
	case "gif":
		gif.Encode(fso, img, nil)
	case "webp":
		webp.Encode(fso, img, &webp.Options{Lossless: true})
	default:
	}
}
