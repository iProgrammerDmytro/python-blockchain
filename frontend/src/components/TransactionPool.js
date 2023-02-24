import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import Transaction from "./Transaction";
import { API_BASE_URL } from "../config";

function TransactionPool() {
  const [transaction, setTransaction] = useState([]);

  useEffect(() => {
    fetch(`${API_BASE_URL}/transactions`)
      .then(response => response.json())
      .then(json => setTransaction(json));
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
