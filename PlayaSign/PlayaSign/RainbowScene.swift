//
//  RainbowScene.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/6/17.
//
//

import Foundation

final class RainbowScene: Animatable {
    private struct RainbowLetter {
        let letter: Letter
        var color: Color

        mutating func nextColor() {
            color.hue += 1
        }
    }

    private var rainbowLetters: [RainbowLetter] = []

    func setup(_ letters: [Letter]) {
        let delta = 360 / letters.count

        for (i, letter) in letters.enumerated() {
            rainbowLetters.append(RainbowLetter(letter: letter, color: Color(i*delta, 100, 100)))
        }
    }

    func render() {
        for (i, rainbowLetter) in rainbowLetters.enumerated() {
            rainbowLetter.letter.channels.flatMap { $0.pixels }.forEach { $0.color = rainbowLetter.color }
            rainbowLetters[i].nextColor()
        }
    }
}
