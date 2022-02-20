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

function post(data)
{
    // post the data
    $.ajax({
        url: '/post_contract',
        data: {'data': data},
        type: 'POST',
        success: function(response) {
            if (response == "Yes")
            {
                alert("We detected no vunerability in this contract");
            }
            else if (response == "No")
            {
                alert("We detected a vunerability to the re-entry attack in this contract");
            }
            else if (response="Error")
            {
                alert("We could not process this request, sorry");
            }
        },
        error: function(error) {
            alert("We could not process this request, sorry");
        }
    });
}


// not vunerable
const EXAMPLE_1 = `
contract EtherStore {
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
const EXAMPLE_2 = `
contract VulnerableBank {
    
    mapping (address=>uint256) balance;
    
    function deposit () external payable {
        balance[msg.sender]+=msg.value;
    }
    function withdraw () external payable{
        require(balance[msg.sender]>=0,'Not enough ether');
        payable(msg.sender).call{value:balance[msg.sender]}("");
        balance[msg.sender]=0;
    }
    function banksBalance () public view returns (uint256){
        return address(this).balance;
    }
    function userBalance (address _address) public view returns (uint256){
        return balance[_address];
    }
}
`;