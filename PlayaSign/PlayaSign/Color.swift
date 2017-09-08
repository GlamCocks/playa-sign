//
//  Color.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import CoreGraphics

struct Color {
    var hue: Int
    var saturation: Int
    var value: Int

    static let white = Color(0, 0, 100)
    static let black = Color(0, 0, 0)
    static let red = Color(0, 100, 100)

    init(_ hue: Int, _ saturation: Int, _ value: Int) {
        self.hue = hue
        self.saturation = saturation
        self.value = value
    }

    func convert(to colorspace: ColorSpace) -> (UInt8, UInt8, UInt8) {
        guard colorspace != .hsv else {
            return (UInt8(hue), UInt8(saturation), UInt8(Double(value) * Defaults[.brightness]))
        }

        let h = CGFloat(hue) / 360.0
        let s = CGFloat(saturation) / 100.0
        let v = CGFloat(value) / 100.0 * CGFloat(Defaults[.brightness])

        var r: CGFloat
        var g: CGFloat
        var b: CGFloat

        let i = Int(h * 6)
        let f = h * 6 - CGFloat(i)
        let p = v * (1 - s)
        let q = v * (1 - f * s)
        let t = v * (1 - (1 - f) * s)
        
        switch (i % 6) {
        case 0:
            r = v
            g = t
            b = p
        case 1:
            r = q
            g = v
            b = p
        case 2:
            r = p
            g = v
            b = t
        case 3:
            r = p
            g = q
            b = v
        case 4:
            r = t
            g = p
            b = v
        case 5:
            r = v
            g = p
            b = q
        default:
            r = v
            g = t
            b = p
        }

        switch colorspace {
        case .rgb:
            return (UInt8(r * 255), UInt8(g * 255), UInt8(b * 255))
        case .grb:
            return (UInt8(g * 255), UInt8(r * 255), UInt8(b * 255))
        default:
            return (0, 0, 0) // This case shouldn't happen
        }
    }
}
