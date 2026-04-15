import React from 'react';
import { Line } from 'react-chartjs-2';
import { Bar } from 'react-chartjs-2';
import './Dashboard.css';

const Dashboard = () => {
  // Sample data for demonstration
  const lineChartData = {
    labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
    datasets: [
      {
        label: 'User Engagement',
        data: [65, 59, 80, 81, 56, 55, 40],
        fill: false,
        backgroundColor: 'rgba(75,192,192,1)',
        borderColor: 'rgba(75,192,192,1)',
      },
    ],
  };

  const barChartData = {
    labels: ['Scan 1', 'Scan 2', 'Scan 3'],
    datasets: [
      {
        label: 'Recent Scans',
        data: [12, 19, 3],
        backgroundColor: ['rgba(255,99,132,1)', 'rgba(54,162,235,1)', 'rgba(255,206,86,1)'],
      },
    ],
  };

  return (
    <div className="dashboard">
      <h1>Dashboard</h1>
      <div className="stats">
        <h2>Statistics</h2>
        <p>Total Scans: 30</p>
        <p>Successful Scans: 28</p>
        <p>Failed Scans: 2</p>
      </div>
      <div className="charts">
        <h2>User Engagement Over Time</h2>
        <Line data={lineChartData} />
        <h2>Recent Scans Visualization</h2>
        <Bar data={barChartData} />
      </div>
    </div>
  );
};

export default Dashboard;