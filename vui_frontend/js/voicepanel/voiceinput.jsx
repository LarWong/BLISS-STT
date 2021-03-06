import React from 'react'
import PropTypes from 'prop-types'
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';

class VoiceInput extends React.Component {
    /* Component for voice assistant hints */

    constructor(props) {
        super(props);
        this.state = {
            voiceinputtext: ""
        };
    }

    componentDidMount() {
        /* Runs as soon as component is mounted */
        this.setState(
            {
                voiceinputtext: ""
            }
        );
    }

    handleInputChange(event) {
        this.setState(
            {
                voiceinputtext: event.target.value
            }
        );
    }

    handleInputSubmit(event) {
        // TODO: handle submit
        this.setState(
            {
                voiceinputtext: ""
            }
        );
    }

    render() {
        /* Renders the component */
        // TODO: set classes
        // TODO: make text hint change on mic icon click
        return (
            <Container className="voiceinput">
                <div className="voiceinputactions">
                    <table>
                        <tr>
                            <td>
                                <Button type="button"></Button>
                            </td>
                            <td>
                                <input name="voicein" placeholder="What can I help you with?" value={voiceinputtext} onChange={this.handleInputChange}></input>
                                <Button type="submit" onClick={this.handleInputSubmit} disabled={!this.state.voiceinputtext}>Send</Button>
                            </td>
                        </tr>
                    </table>
                </div>
            </Container>
        );
    }
}

VoiceInput.propTypes = {};

export default VoiceInput;