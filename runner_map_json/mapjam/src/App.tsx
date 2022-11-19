import React, { ChangeEvent, ChangeEventHandler, useEffect, useRef } from 'react';
import logo from './logo.svg';
import './App.css';
import { Box, Button, Input } from '@chakra-ui/react';
import { Map, MapTile } from './dto/map';
import FileInput from './components/Input';
import Grid from './components/Grid';


function App() {
  const [map, _setMap] = React.useState<Map | null>(null);
  const [layers, setLayers] = React.useState<Map[] | null>(null);
  const [selectedLayer, setSelectedLayer] = React.useState<number>(0);
  const discretMap = useRef<Map | null>(map);

  useEffect(() => {
    setMap(map);
  }, []);

  const setMap = (map: Map | null) => {
    discretMap.current = map!;
    _setMap(map);
  }


  useEffect(() => {
    setMap(layers?.[selectedLayer] ?? null);
  }, [layers, selectedLayer]);

  const handleExport = () => {
    const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(layers));
    console.log(dataStr);
  }

  return (
    <div className="App">
      {map === null && <FileInput setter={setLayers} />}
      {map !== null && <Grid mapState={[map, setMap]} discretMap={discretMap} />}
      <Box display="flex" gap="0.5em" mx={3} mb={3}>
        {layers && layers.map((layer, i) => (
          <Button
            colorScheme={i === selectedLayer ? "blue" : "gray"}
            key={i}
            onClick={() => {
              if (layers) {
                const newLayers = [...layers];
                newLayers[selectedLayer] = discretMap.current!;
                setLayers(newLayers);
              }
              setSelectedLayer(i)
            }}>Layer {i}</Button>
        ))}
        {layers && <Button onClick={handleExport}>
          Export
        </Button>}
      </Box>
    </div>
  );
}

export default App;
