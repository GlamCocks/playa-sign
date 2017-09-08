//
//  Pixel.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import CoreGraphics
import ObjectMapper

final class Pixel: Mappable, CustomStringConvertible {
    var index: Int = .none
    var color: Color = .black
    private var x: CGFloat = 0
    private var y: CGFloat = 0
    private var isAbsolutePosition: Bool = false
    weak var channel: Channel? 

    var position: CGPoint {
        get {
            return CGPoint(x: x, y: y)
        }
        set {
            guard !isAbsolutePosition else {
                log.warning("Pixel's absolute position has already been calculated, ignoring...")
                return
            }

            x = newValue.x
            y = newValue.y
            isAbsolutePosition = true
        }
    }

    required init?(map: Map) { }

    func mapping(map: Map) {
        index <- map["index"]
        x <- map["x"]
        y <- map["y"]
    }

    var description: String {
        return "Pixel #\(index): \(color)"
    }
}
