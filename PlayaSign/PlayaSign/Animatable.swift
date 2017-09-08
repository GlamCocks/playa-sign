//
//  Animatable.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/6/17.
//
//

import Foundation

protocol Animatable {
    func setup(_ letters: [Letter])
    func render()
}
