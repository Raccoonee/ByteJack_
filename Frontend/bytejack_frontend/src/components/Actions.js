

const Actions = () => {
    return (
        <div id="actions">
            <button id="deal" class="btn">Deal!</button>
            <button id="hit" class="btn" disabled>Hit</button>
            <strong>Wager:</strong> $<input id="wager" class="input-small" type="text" />
        </div>
    )
}

export default Actions