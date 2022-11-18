import React from "react";

export type Setter<T> = (value: T) => void;

export type State<T> = [T, Setter<T>];