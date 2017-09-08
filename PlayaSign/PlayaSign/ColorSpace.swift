//
//  ColorSpace.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import Foundation

enum ColorSpace: String, CustomStringConvertible {
    case rgb = "RGB"
    case grb = "GRB"
    case hsv = "HSV"

    var description: String {
        return rawValue
    }
}
