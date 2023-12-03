(ns day02.core
  (:require
    [clojure.edn :as edn]
    [clojure.string :as str]))


(def input (slurp "input.txt"))


(def color-counts
  {"red" 12
   "green" 13
   "blue" 14})


(def games (str/split-lines input))


(defn check-color-available
  [color count]
  (let [available (get color-counts color)]
    (and available (>= available count))))


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


(defn multiply-values
  [counts]
  (apply * (vals counts)))


(defn process-rounds2
  [rounds]
  (multiply-values (reduce (fn [counts color]
                             (let [splitted (str/split color #" ")
                                   count (edn/read-string (first splitted))
                                   color (second splitted)]
                               (update counts color (fnil #(max % count) 0))))
                           {"red" 0 "green" 0 "blue" 0} rounds)))


(def map-result2
  (map #(let [splited-game (str/split % #":")
              rounds (mapcat (fn [element] (map str/trim (str/split element #","))) (str/split (second splited-game) #";"))
              power  (process-rounds2 rounds)] power) games))


(def result2 (reduce + map-result2))

(print result2)
