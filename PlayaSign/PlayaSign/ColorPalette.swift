//
//  ColorPalette.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/6/17.
//
//

import Foundation

struct ColorPalette {
    let hueRange: CountableClosedRange<Int>
    let saturationRange: CountableClosedRange<Int>
    let valueRange: CountableClosedRange<Int>

    func randomColor() -> Color {
        let h = Int(arc4random_uniform(UInt32(hueRange.upperBound - hueRange.lowerBound)) + UInt32(hueRange.lowerBound))
        let s = Int(arc4random_uniform(UInt32(saturationRange.upperBound - saturationRange.lowerBound)) + UInt32(saturationRange.lowerBound))
        let v = Int(arc4random_uniform(UInt32(valueRange.upperBound - valueRange.lowerBound)) + UInt32(valueRange.lowerBound))

        return Color(h, s, v)
    }
}
