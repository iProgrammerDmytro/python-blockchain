import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Transaction from "./Transaction";
import { API_BASE_URL, SECONDS_JS } from "../config";

const POOL_INTERVAL = 10 * SECONDS_JS;

function TransactionPool() {
  const [transaction, setTransaction] = useState([]);

  const fetchTransactions = () => {
    fetch(`${API_BASE_URL}/transactions`)
    .then(response => response.json())
    .then(json => {
      console.log('transactions json', json);

      setTransaction(json);
    });
  }

  useEffect(() => {
    fetchTransactions();

    const intervalId = setInterval(fetchTransactions, POOL_INTERVAL);

    return () => clearInterval(intervalId);
  }, []);

  return (
    <div className="TransactionPool">
      <Link to="/">Home</Link>
      <hr />
      <h3>Transaction Pool</h3>
      {
        transaction.map(transaction => (
          <div key={transaction.id}>
            <hr />
            <Transaction transaction={transaction} />
          </div>
        ))
      }
    </div>
  )
}

export default TransactionPool;
