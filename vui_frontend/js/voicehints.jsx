import React from 'react'
import PropTypes from 'prop-types'

class VoiceHints extends React.Component {
    /* Component for voice assistant hints */

    constructor(props) {
        super(props);
        this.state = {
            hintslist: [],
            numhintstoshow: 4,
        };
    }

    componentDidMount() {
        /* Runs as soon as component is mounted */
        // TODO: get hints list dynamically, figure out where from
        this.setState(
            {
                hintslist = [
                   '"Call John."',
                   '"What\'s on my schedule?"',
                   '"Retrieve radiation data."',
                   '"Start taking notes."',
                   '"Send Kevin a message."',
                   '"What\'s the time?"',
                   '"What can you do?"',
                   '"I want to hear a joke!"',
                ]
            }
        )
    }

    render() {
        /* Renders the component */
        return (
            <div className="voicehints">
                <h1>Some things you can say:</h1>
                <React.Fragment>
                    <ul className="voicehintslist">
                        {
                            this.state.hintslist.slice(0, 4).map(
                                hintitem => (
                                    <li key={hintitem} className="voicehintsitem">
                                        {hintitem}
                                    </li>
                                )
                            )
                        }
                    </ul>
                </React.Fragment>
                <button type="button" onClick="">See More</button>
            </div>
        );
    }
}

VoiceHints.propTypes = {
    numhintstoshow: PropTypes.number.isRequired,
};

export default VoiceHints;