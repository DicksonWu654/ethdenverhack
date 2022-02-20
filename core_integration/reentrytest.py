test = """​​contract EtherStore {
    mapping(address=> uint256) public balances

    function transfer(address to, uint256 amount) external {
        if (balances[msg.sender] >= amount) {
            balances[to] += amount
            balances[msg.sender] -= amount
        }
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender]
        require(msg.sender.call.value(amount)())
        balances[msg.sender] = 0
    }
}"""