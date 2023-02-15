import React, { useState, useEffect } from 'react';
import logo from '../assets/logo.png';
import { API_BASE_URL } from '../config';
import Blockchain from "./Blockchain";
import dayjs from 'dayjs';

let start = dayjs().unix()
setInterval(() => {
  let now = dayjs().unix();
  let diff = (now - start);
  console.log(`${diff} second(s) passed`);
  console.log(dayjs().unix());
  console.log(dayjs())
}, 5000);

function App() {
  const [walletInfo, setWalletInfo] = useState({});

  useEffect(() => {
    fetch(`${API_BASE_URL}/wallet/info`)
      .then(response => response.json())
      .then(json => setWalletInfo(json));
  }, []);

  const { address, balance } = walletInfo;

  return (
    <div className='App'>
      <img className="logo" src={logo} alt="application-logo" />
      <h3>Welcome to pychain</h3>
      <br />
      <div className="WalletInfo">
        <div>Address: {address}</div>
        <div>Balance: {balance}</div>
      </div>
      <br />
      <Blockchain />
    </div>
  );
}

export default App;
