$('#sub_1').click((e) => {
    e.preventDefault();

    // get data from the form
    let data = $('#contract_input').val();
    post(data);
})

$('#sub_2').click((e) => {
    e.preventDefault();

    // write the example to the text area
    $('#contract_input').val(EXAMPLE_1);
    post(EXAMPLE_1);
})

$('#sub_3').click((e) => {
    e.preventDefault();

    // write the example to the text area
    $('#contract_input').val(EXAMPLE_2);
    post(EXAMPLE_2);
})

$('#sub_4').click((e) => {
    e.preventDefault();

    // write the example to the text area
    $('#contract_input').val(EXAMPLE_3);
    post(EXAMPLE_3);
})

$('#sub_5').click((e) => {
    e.preventDefault();

    // write the example to the text area
    $('#contract_input').val(EXAMPLE_4);
    post(EXAMPLE_4);
})

function post(data) {

    if (data == "") {
        alert("No data was entered into the formz");
        return;
    }

    // post the data
    $.ajax({
        url: '/post_contract',
        data: { 'data': data },
        type: 'POST',
        success: function (response) {
            console.log(response)
            if (response == 0) {
                alert("We detected no vunerability in this contract");
            }
            else if (response == 1) {
                alert("We detected a vunerability to the re-entry attack in this contract");
            }
            else if (response = "Error") {
                alert("We could not process this request, sorry");
            }
        },
        error: function (error) {
            alert("We could not process this request, sorry");
        }
    });
}


// not vunerable
const EXAMPLE_1 = `
contract ShouldReturnSafe {
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
`;

// vunerable
const EXAMPLE_2 = `contract EtherStore {
    mapping(address => uint) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {
        uint bal = balances[msg.sender];
        require(bal > 0);

        (bool sent, ) = msg.sender.call{value: bal}("");
        require(sent, "Failed to send Ether");

        balances[msg.sender] = 0;
    }

    // Helper function to check the balance of this contract
    function getBalance() public view returns (uint) {
        return address(this).balance;
    }
}`;

const EXAMPLE_3 =  `
??????contract MyNewContract {
    mapping(address => uint256) public balances;
    function withdraw() external {
        require(!lock);
        lock = true;
        uint256 amount = balances[msg.sender];
        require(msg.sender.call.value(amount)());
        balances[msg.sender] = 0;
        lock = false;
    }
    function transfer(address to, uint256 amount) external {
        // lock used to prevent people from accessing this while it's running
        require(!lock);
        lock = true;
        if (balances[msg.sender] >= amount) {
            balances[to] += amount;
            balances[msg.sender] -= amount;
        }
        lock = false;
    }
}

`;

const EXAMPLE_4 = `
contract PaymentContract {
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

`;