samples = """Does this solidity smart contract have a vulnerability to a re-entry attack:

--SmartContract--
contract EtherStore {
    uint256 public withdrawalLimit = 1 ether;
    mapping(address => uint256) public lastWithdrawTime;
    mapping(address => uint256) public balances;
    
    function depositFunds() public payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdrawFunds (uint256 _weiToWithdraw) public {
        require(balances[msg.sender] >= _weiToWithdraw);
        // limit the withdrawal
        require(_weiToWithdraw <= withdrawalLimit);
        // limit the time allowed to withdraw
        require(now >= lastWithdrawTime[msg.sender] + 1 weeks);
        require(msg.sender.call.value(_weiToWithdraw)());
        balances[msg.sender] -= _weiToWithdraw;
        lastWithdrawTime[msg.sender] = now;
    }
 }

--Classification--
Yes

--SmartContract--
contract EtherStore {
    uint256 public withdrawalLimit = 1 ether;
    mapping(address => uint256) public lastWithdrawTime;
    mapping(address => uint256) public balances;
    
    function depositFunds() public payable {
        balances[msg.sender] += msg.value;
    }
    
    function withdrawFunds (uint256 _weiToWithdraw) public {
        require(!lock);
        lock = true;
        require(balances[msg.sender] >= _weiToWithdraw);
        // limit the withdrawal
        require(_weiToWithdraw <= withdrawalLimit);
        // limit the time allowed to withdraw
        require(now >= lastWithdrawTime[msg.sender] + 1 weeks);
        require(msg.sender.call.value(_weiToWithdraw)());
        balances[msg.sender] -= _weiToWithdraw;
        lastWithdrawTime[msg.sender] = now;
        lock = false;
    }
 }

--Classification--
No

--SmartContract--
contract HoneyPot {
  mapping (address => uint) public balances;
  function HoneyPot() payable {
    put();
  }
  function put() payable {
    balances[msg.sender] = msg.value;
  }
  function get() {
    if (!msg.sender.call.value(balances[msg.sender])()) {
      throw;
    }
      balances[msg.sender] = 0;
  }
  function() {
    throw;
  }
}

--Classification--
Yes

--SmartContract--
contract EtherStore {
    mapping(address => uint256) public balances;

    function transfer(address to, uint256 amount) external {
        if (balances[msg.sender] >= amount) {
            balances[to] += amount;
            balances[msg.sender] -= amount;
        }
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        require(msg.sender.call.value(amount)());
        balances[msg.sender] = 0;
    }
}

--Classification--
Yes

--SmartContract--
​​contract EtherStore {
    mapping(address => uint256) public balances;

    function transfer(address to, uint256 amount) external {
        require(!lock);
        lock = true;
        if (balances[msg.sender] >= amount) {
            balances[to] += amount;
            balances[msg.sender] -= amount;
        }
        lock = false;
    }

    function withdraw() external {
        require(!lock);
        lock = true;
        uint256 amount = balances[msg.sender];
        require(msg.sender.call.value(amount)());
        balances[msg.sender] = 0;
        lock = false;
    }
}

--Classification--
No

--SmartContract--
contract EtherStore {
    mapping(address => uint256) public balances;

    function transfer(address to, uint256 amount) external {
        if (balances[msg.sender] >= amount) {
            balances[to] += amount;
            balances[msg.sender] -= amount;
        }
    }

    function withdraw() external {
        uint256 amount = balances[msg.sender];
        balances[msg.sender] = 0;
        require(msg.sender.call.value(amount)());
    }
}

--Classification--
No"""
