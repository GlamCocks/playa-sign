//
//  Int+Helpers.swift
//  Socket
//
//  Created by Sebastian Thiebaud on 9/5/17.
//

import Foundation

extension Int {
    static let none = Int.max
}

extension Int {
    var degreesToRadians: Double {
        return Double(self) * .pi / 180
    }
}

extension FloatingPoint {
    var degreesToRadians: Self {
        return self * .pi / 180
    }

    var radiansToDegrees: Self {
        return self * 180 / .pi
    }
}
