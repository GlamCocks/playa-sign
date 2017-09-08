//
//  Letter.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import CoreGraphics
import ObjectMapper

final class Letter: Mappable, CustomStringConvertible {
    var index: Int = .none
    var character: String = ""
    var channels: [Channel] = []
    var angle: CGFloat = 0
    private var width: CGFloat = 0
    private var height: CGFloat = 0
    private var x: CGFloat = 0
    private var y: CGFloat = 0

    var size: CGSize {
        return CGSize(width: width, height: height)
    }

    var origin: CGPoint {
        return CGPoint(x: x, y: y)
    }

    required init?(map: Map) { }

    func mapping(map: Map) {
        index <- map["index"]
        character <- map["character"]
        channels <- map["channels"]
        angle <- map["angle"]
        width <- map["width"]
        height <- map["height"]
        x <- map["left"]
        y <- map["top"]

        calculatePixelPositions()
    }

    var description: String {
        return "Letter #\(index) (\(character))"
    }

    private func calculatePixelPositions() {
        let angleRad = angle.degreesToRadians

        channels.flatMap { $0.pixels }.forEach { pixel in
            let relativeX = pixel.position.x * cos(angleRad) - pixel.position.y * sin(angleRad)
            let relativeY = pixel.position.y * cos(angleRad) + pixel.position.x * sin(angleRad)
            let absoluteX = origin.x + relativeX * size.width
            let absoluteY = origin.y + relativeY * size.height
            pixel.position = CGPoint(x: absoluteX, y: absoluteY)
        }
    }
}
