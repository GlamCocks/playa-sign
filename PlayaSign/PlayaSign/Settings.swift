//
//  Settings.swift
//  PlayaSign
//
//  Created by Sebastian Thiebaud on 9/6/17.
//
//

import Foundation

extension DefaultsKeys {
    static let fps = DefaultsKey<Double>("system/fps")
    static let brightness = DefaultsKey<Double>("system/brightness")
    static let speed = DefaultsKey<Double>("system/speed")
    static let colorspaceCorrection = DefaultsKey<Bool>("system/colorspace_correction")
    static let scene = DefaultsKey<Animatable>("scene")
}

extension UserDefaults {
    func registerDefaults() {
        register(key: .fps, value: 50)
        register(key: .brightness, value: 1)
        register(key: .speed, value: 1)
        register(key: .colorspaceCorrection, value: false)
    }

    private func register<T>(key: DefaultsKey<T>, value: T?) {
        if !hasKey(key) {
            self[key._key] = value
        }
    }
}
