(ns day02.core
  (:require
    [clojure.edn :as edn]
    [clojure.string :as str]))


(def input (slurp "input.txt"))


(def red 12)
(def green 13)
(def blue 14)

(def games (str/split-lines input))


(defn check-color-available
  [color count]
  (cond
    (= color "red") (if (> count red) false true)
    (= color "green") (if (> count green) false true)
    (= color "blue") (if (> count blue) false true)
    :else true))


(defn process-rounds
  [rounds]
  (map (fn [element]
         (let [splitted (str/split element #" ")
               count (edn/read-string (first splitted))
               color (second splitted)] (check-color-available color count))) rounds))


(def map-result
  (map #(let [splited-game (str/split % #":")
              game-id (second (str/split (first splited-game) #" "))
              rounds (mapcat (fn [element] (map str/trim (str/split element #","))) (str/split (second splited-game) #";"))
              parsed (every? true? (process-rounds rounds))] (if (= parsed true) (edn/read-string game-id) 0)) games))


(def result (reduce + map-result))

(print result)


