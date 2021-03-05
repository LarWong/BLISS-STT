import React from 'react'
import PropTypes from 'prop-types'

class VoiceHints extends React.Component {
    /* Component for voice assistant hints */

    constructor(props) {
        super(props);
        this.state = {
            hintslist: [],
        };
    }

    componentDidMount() {

    }

    render() {
        return (
            <div className="voicehints">
                <h1>Some things you can say:</h1>
                <React.Fragment>
                    <ul className="voicehintslist">
                        {
                            this.state.hintslist.map(
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

};

export default VoiceHints;