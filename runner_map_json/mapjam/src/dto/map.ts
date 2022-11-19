export interface MapTile {
    x: number;
    y: number;
    id: string | null;
}

export interface Map {
    tiles: MapTile[];
    width: number;
    height: number;
}
