import React, { Component } from 'react';
import moment from 'moment';

// mock data - fetch from external source later
const mockFilters = ['location','family'];
const mockAlerts = [{
    type: 'Media Report',
    date: moment().format('MMM DD YYYY'),
    location: 'San Francisco, CA',
    keywords: ['location','family'],
    url: 'http://www.google.com',
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
},{
    type: 'Media Report',
    date: moment().format('MMM DD YYYY'),
    location: 'San Francisco, CA',
    keywords: ['location','family'],
    url: 'http://www.yahoo.com',
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.'
}];


// for selecting the filters to use
// todo: add toggling & local state for selected filters
const Filters = (props) => (
    <div className="filters">
        {props.filters.map((filter) => (
            <span className="filter-item keyword" key={filter}>
                {filter}
            </span>
        ))}
        <span className="filter-item keyword-selected">+ Add filter</span>
    </div>
);

// for the list of alerts that have been aggregated from the CSVs generated from the BE
const Alert = ({alert, key}) => (
    <div className = "alert-item" key={key}>
        <div className="alert-header">
            <div className="alert-type">
                {alert.type}
            </div>
            <div className="alert-date">
                {alert.date}
            </div>
        </div>
        <div className="alert-location">
            {alert.location}
        </div>
        <div className="alert-keywords">
            keywords: {alert.keywords.map((keyword) =>
                <span className="keyword-selected">{keyword}</span>
            )}
        </div>
        <div className="alert.text">
            {alert.text}
        </div>
        <div className="alert.source">
            source: <a href={alert.url}>{alert.url}</a>
        </div>
    </div>
);

class Alerts extends Component {
    render() {
        return (
            <div className="alerts">
                <div className="alerts-left">
                    <h1 className="title">Alerts</h1>
                    <Filters className="filters" filters={mockFilters}/>
                </div>
                <div className="alerts-right alerts-list">
                    {mockAlerts.map((alert,idx) => <Alert alert={alert} key={idx}/>)}
                </div>
            </div>
        );
    }
}

export default Alerts;