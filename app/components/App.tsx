import "../css/App.css";
import Player from "./Player";
import Middle from "./Middle";
import Opponent from "./Opponent";

function App() {
  return (
    <div style={{ backgroundImage: "../public/tavolo.jpg" }}>
      <Opponent />
      <Middle />
      <Player />
    </div>
  );
}

export default App;
