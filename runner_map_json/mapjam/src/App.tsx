import React, { ChangeEvent, ChangeEventHandler } from 'react';
import logo from './logo.svg';
import './App.css';
import { Button, Input } from '@chakra-ui/react';
import { Map, MapTile } from './dto/map';
import FileInput from './components/Input';
import Grid from './components/Grid';


function App() {
  const [map, setMap] = React.useState<Map | null>(null);

  return (
    <div className="App"> 
      {map === null && <FileInput setter={setMap} />}
      { map !== null && <Grid mapState={[map, setMap]} />}
    </div>
  );
}

export default App;
