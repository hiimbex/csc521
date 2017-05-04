
(ns clojure-quirk.core
  (:gen-class)
  (:require [instaparse.core :as insta]))

(defn third [aList] (nth aList 2))
(defn fourth [aList] (nth aList 3))
(defn fifth [aList] (nth aList 4))
(defn sixth [aList] (nth aList 5))
(defn seventh [aList] (nth aList 6))

(defn ret-print [thingToPrint]
  (println thingToPrint)
  thingToPrint
); end ret-print

(defn CallByLabel [funLabel & args]
  (apply (resolve (symbol (name funLabel))) args)
); end CallByLabel

(defn Name [subtree scope]
  (ret-print "Name")
  (ret-print (second (second subtree)))
  (cond (= nil (get scope (second (second subtree))))
    (str (second (second subtree)))
    :else
    (get scope (second (second subtree))))
); end Name

(defn NumberA [subtree scope]
  (ret-print "NumberA")
  (cond
      (= 2 (count subtree))
      (Double/parseDouble (second (second subtree)))
      (= 2 :SUB (first (second subtree)))
      (- (Double/parseDouble (second (third subtree))))
      (= 2 :ADD (first (second subtree)))
      (Double/parseDouble (second (third subtree))))
); end Number

(defn Value [subtree scope]
  (ret-print "Value")
  (CallByLabel (first (second subtree)) (second subtree) scope)
); end Value

(defn Term [subtree scope]
  (ret-print "Term")
  (cond (= 2 (count subtree))
    (CallByLabel (first (second subtree))(second subtree) scope)
     (= :MULT (first (third subtree)))
        (*(CallByLabel (first (second subtree))(second subtree) scope)
        (CallByLabel (first (fourth subtree))(fourth subtree) scope))
      (= :DIV (first (third subtree)))
        (quot (CallByLabel (first (second subtree))(second subtree) scope)
        (CallByLabel (first (fourth subtree))(fourth subtree) scope)))
); end Term

(defn Factor [subtree scope]
  (ret-print "Factor")
  (cond (= 2 (count subtree))
    (CallByLabel (first (second subtree))(second subtree) scope)
    (= :EXP (first (third subtree)))
      (Math/pow (CallByLabel (first (second subtree))(second subtree) scope)
      (CallByLabel (first (fourth subtree))(fourth subtree) scope)))
); end Factor

(defn FunctionCall [subtree scope]
  (ret-print "FunctionCall")
  (= :RPAREN (first (second (fourth subtree))))
    (get scope (second (second (second subtree))))
); end FunctionCall

(defn Parameter [subtree scope]
  (ret-print "Parameter")
  (CallByLabel (first (second subtree))(second subtree) scope)
); end Parameter

(defn ParameterList [subtree scope]
  (ret-print "ParameterList")
  (CallByLabel (first (second subtree))(second subtree) scope)
); end ParameterList

(defn SubExpression [subtree scope]
  (println "SubExpression")
  (CallByLabel (first (third subtree))(third subtree) scope)
); end SubExpression

(defn Expression [subtree scope]
  (ret-print "Expression")
  (cond (= 2 (count subtree))
    (CallByLabel (first (second subtree))(second subtree) scope)
    (= :ADD (first (third subtree)))
      (+ (CallByLabel (first (second subtree))(second subtree) scope)
      (CallByLabel (first (fourth subtree))(fourth subtree) scope))
    (= :SUB (first (third subtree)))
      (- (CallByLabel (first (second subtree))(second subtree) scope)
      (CallByLabel (first (fourth subtree))(fourth subtree) scope)))
); end Expression

(defn MultipleAssignment [subtree scope]
  (ret-print "Multiple Assignment")
); end MultipleAssignment

(defn SingleAssignment [subtree scope]
  (ret-print "Single Assignment")
    (assoc scope (CallByLabel (first (third subtree))(third subtree) scope)
    (CallByLabel (first (fifth subtree))(fifth subtree) scope))
); end SingleAssignment

(defn Return [subtree scope]
  (ret-print "RETURN")
  (CallByLabel (first (third subtree))(third subtree) scope)
); end Return

(defn Print [subtree scope]
  (ret-print "PRINT")
  (ret-print (CallByLabel (first (third subtree)) (third subtree) scope))
); end Print

(defn Assignment [subtree scope]
  (ret-print "Assignment")
  (cond (= :SingleAssignment (first (second subtree)))
    (CallByLabel (first (second subtree))(second subtree) scope)
    (= :MultipleAssignment (first (second subtree)))
    (CallByLabel (first (second subtree))(second subtree) scope))
); end Assignment

(defn FunctionDeclaration [subtree scope]
  (ret-print "FunctionDeclaration")
  (= :RPAREN (first (second (fifth subtree))))
    (assoc scope (CallByLabel (first (third subtree))(third subtree) scope)
      (CallByLabel (first (second (seventh subtree))) (second (seventh subtree)) scope))
  ; (let
  ;     [functionName (CallByLabel (first (third subtree)) (third subtree) scope)
  ;     paramNames (CallByLabel (first (fifth subtree)) (fifth subtree) scope)]
  ; (assoc scope functionName (vector paramNames (seventh subtree)))
  ;)
); end FunctionDeclaration

(defn Statement [subtree scope]
  (ret-print "STATEMENT")
  (CallByLabel (first (second subtree)) (second subtree) scope)
); end Statement

(defn Program [subtree scope]
  (ret-print "PROGRAM")
  (if
    (< 2 (count subtree))
      ((def tempScope (merge scope (CallByLabel (first (second subtree))(second subtree) scope)))
      (CallByLabel (first (third subtree))(third subtree) tempScope)))
  (if
    (>= 2 (count subtree))
      (CallByLabel(first(second subtree)) (second subtree)scope))
  (System/exit 0)
); end Program

(defn interpret-quirk [subtree scope] (CallByLabel (first subtree) subtree {}))

(defn -main [& args]
  ;sample for reading all stdin
  (def stdin (slurp *in*))
  ;(ret-print stdin)

  ;(ret-print (first *command-line-args*))
  (if (.equals "-pt" (first *command-line-args*))
    (def SHOW_PARSE_TREE true)
  )
  (def quirk-parser (insta/parser (slurp "resources/quirk-ebnf") :auto-whitespace :standard))
  (def parse-tree (quirk-parser stdin))
  (if (= true SHOW_PARSE_TREE)
    (ret-print parse-tree)
    (interpret-quirk parse-tree {}))
  ;(interpret-quirk parse-tree {})
  ;(ret-print "done!")
)

(-main)
