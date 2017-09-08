//
//  Channel.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import ObjectMapper

final class Channel: Mappable, CustomStringConvertible {
    var index: Int = .none
    var colorspace: ColorSpace = .rgb
    var pixels: [Pixel] = []

    required init?(map: Map) { }

    func mapping(map: Map) {
        index <- map["index"]
        colorspace <- (map["colorspace"], EnumTransform<ColorSpace>())
        pixels <- map["pixels"]

        pixels.forEach { $0.channel = self }
    }

    var description: String {
        return "Channel #\(index) (\(colorspace)): \(pixels.count) pixels"
    }
}
