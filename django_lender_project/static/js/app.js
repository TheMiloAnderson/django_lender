Vue.component('books-list', {
    template: '#books-list-template',
    props: {
        books: Array,
        columns: Array
    },
    filters: {
        capitalize: function(str) {
            return str.charAt(0).toUpperCase() + str.slice(1)
        }
    },
    delimiters: ['[[',']]']
});

const v = new Vue({
    el: '#vue-booklist',
    data: {
        books: null,
        columns: ['title', 'author', 'status']
    },
    methods: {
        getBooks: function() {
            $.get(
                '/books/data',
                (res) => this.setData(res)
            );
        },
        setData: function(res) {
            this.books = res.map((book) => {
                return {
                    id: book.id,
                    url: book.url,
                    title: book.title,
                    author: book.author,
                    status: book.status
                }
            });
        }
    },
    mounted: function() {
        this.getBooks();
    }
});