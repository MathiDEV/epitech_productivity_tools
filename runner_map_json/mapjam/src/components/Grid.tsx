import { Box, Button } from "@chakra-ui/react";
import { Map, MapTile } from "../dto/map";
import sprites from '../data/sprites.json';
import Toolbox from "./Toolbox";
import React, { MouseEventHandler, useEffect, useRef, useState } from "react";
import { Setter, State } from "../dto/setter";
import { Tool } from "../dto/tools";


function setCase(map: Map, x: number, y: number, id: React.MutableRefObject<string | null>, setMap: Setter<Map | null>) {
    const newMap = { ...map };
    newMap.tiles = newMap.tiles.filter((t) => !(t.x === x && t.y === y))
    if (id.current) {
        newMap.tiles.push({ x, y, id: id.current });
    }
    setMap(newMap);
}

function paintPotRecursion(map: MapTile[], x: number, y: number, id: string | null, refId: string | null, width: number, height: number): MapTile[] {
    const tile = map.find((t) => t.x === x && t.y === y);
    const thisId = tile ? tile.id : null;
    if (!(x < 0 || x >= width || y < 0 || y >= height) && thisId === refId) {
        map = map.filter((t) => !(t.x === x && t.y === y));
        if (id)
            map.push({ x, y, id });
        let tempMap;
        tempMap = paintPotRecursion(map, x + 1, y, id, refId, width, height);
        tempMap = paintPotRecursion(tempMap, x - 1, y, id, refId, width, height);
        tempMap = paintPotRecursion(tempMap, x, y + 1, id, refId, width, height);
        tempMap = paintPotRecursion(tempMap, x, y - 1, id, refId, width, height);
        return tempMap;
    }
    return map;
}

function paintPot(map: Map, x: number, y: number, id: React.MutableRefObject<string | null>, setMap: Setter<Map | null>, refId: string | null) {
    const newTiles = [...map.tiles]
    const newMap = { ...map, tiles: paintPotRecursion(newTiles, x, y, id.current, refId, map.width, map.height) };
    setMap(newMap);
}

const Tile = React.memo(function Tile({ tile, onClick }: { tile: MapTile, onClick?: MouseEventHandler }) {
    return (
        <Box
            bgSize="100% 100%"
            w="2.5em"
            h="2.5em"
            onMouseDown={onClick}
            onMouseEnter={(e) => {
                if (e.buttons === 1) {
                    onClick?.(e);
                }
            }}
            bgColor="rgba(0,0,0,0.1)"
            bgImage={tile.id === null ? "" : `url(${sprites[tile.id as keyof typeof sprites].path})`}
            _hover={{ transform: "scale(1.1)", opacity: "0.5" }}
            transition="transform 0.2s, opacity 0.2s"
        />
    )
}, (prev, next) => prev.tile.id === next.tile.id);

function GridCases({ gridState, brushState, mapState, discretBrush, tooltype, discretMap, render }: { gridState: State<MapTile[][]>, brushState: State<string | null>, mapState: State<Map | null>, discretBrush: React.MutableRefObject<string | null>, tooltype: React.MutableRefObject<Tool>, discretMap: React.MutableRefObject<Map | null>, render: boolean }) {
    const [grid, setGrid] = gridState;
    const [brush, setBrush] = brushState;
    const [map, setMap] = mapState;

    return (<Box display="flex" flexDir="column" gap={render ? "0px" : "1px"} flexWrap="wrap">
        {grid!.map((row, i) => (
            <Box key={i} display="flex" gap={render ? "0px" : "1px"} flexWrap="nowrap">
                {row.map((tile, j) => (
                    <Tile tile={tile} key={j} onClick={() => {
                        if (tooltype.current === "brush") {
                            setCase(discretMap.current!, j, i, discretBrush, setMap)
                        } else if (tooltype.current === "pot") {
                            paintPot(discretMap.current!, j, i, discretBrush, setMap, tile.id);
                        } else if (tooltype.current === "picker") {
                            setBrush(tile.id);
                        }
                    }} />
                ))}
            </Box>
        ))
        }
    </Box>)
}

export default function Grid({ mapState, discretMap }: { mapState: State<Map | null>, discretMap: React.MutableRefObject<Map | null> }) {
    const [map, setMap] = mapState;
    const [tooltype, _setTooltype] = useState<Tool>("brush");
    const discretTooltype = useRef<Tool>("brush");
    const [brush, _setBrush] = useState<string | null>(null);
    const discretBrush = useRef<string | null>(null);
    const [grid, setGrid] = useState<MapTile[][]>([]);
    const [render, setRender] = useState<boolean>(false);

    const setBrush = (id: string | null) => {
        discretBrush.current = id;
        _setBrush(id);
    }

    const setTooltype = (tool: Tool) => {
        discretTooltype.current = tool;
        _setTooltype(tool);
    }

    useEffect(() => {
        const newGrid: MapTile[][] = [];
        for (let i = 0; i < map!.height; i++) {
            const row: MapTile[] = [];
            for (let j = 0; j < map!.width; j++) {
                row.push({ x: j, y: i, id: null });
            }
            newGrid.push(row);
        }
        map!.tiles.forEach((tile, i) => {
            newGrid[tile.y][tile.x] = tile;
        })
        setGrid(newGrid);
    }, [map])
    if (!discretMap.current)
        return null;
    return (
        <Box>
            <Box overflowX="scroll">
                <GridCases render={render} gridState={[grid, setGrid]} brushState={[brush, setBrush]} mapState={[map, setMap]} discretMap={discretMap} discretBrush={discretBrush} tooltype={discretTooltype} />
            </Box>
            <Toolbox brushState={[brush, setBrush]} toolState={[tooltype, setTooltype]} />
            <Button m={3} colorScheme={render ? 'blue' : 'gray'} onClick={() => setRender(!render)}>Render</Button>
        </Box>
    )
}