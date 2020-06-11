function updateAccountsList(data) {
    var accountsList = '';
    $.each(data.content.accounts, (i, account) => {
        accountsList += '<div class="account-item" id="' +
            account.accountId +
            '">' +
            account.name +
            ' (' +
            (account.balances.available ? account.balances.available : 0) +
            '/' +
            (account.balances.current ? account.balances.current : 0) +
            ' ' +
            account.balances.isoCurrencyCode +
            ')' +
            '</div>';
    });
    $('#accounts-list').html(accountsList);
}

$(() => {
    $.ajaxSetup({beforeSend: function(xhr){
        xhr.setRequestHeader('Authorization', 'Token ' + localStorage.getItem('authToken'))
    }});
    $.get('/api/v1/identity/', (data) => {
        updateAccountsList(data);
    });
});

$('body').delegate('.account-item', 'click', (event) => {
    var accountId = event.toElement.id;
    $.get('/api/v1/transactions/?account=' + accountId, (data) => {
        var transactionsList = '';
        $.each(data.content, (i, transaction) => {
            transactionsList += '<div class="transactions-item' +
                (transaction.amount < 0 ? '">' : ' transactions-item-negative">') +
                transaction.date +
                ' ' +
                -transaction.amount +
                ' ' +
                transaction.isoCurrencyCode +
                ' - ' +
                transaction.name +
                '</div>'
        });
        $('#transactions-list').html(transactionsList);
    });
});
