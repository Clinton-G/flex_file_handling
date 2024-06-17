def sentiment_analysis(filename):
    positive_words = ['amazing', 'enjoy', 'beautiful', 'wonderful', 'memorable', 'fantastic', 'excellent', 'enlightening', 'unforgettable']
    negative_words = ['disappointing', 'poor', 'crowded', 'lackluster', 'scarce']

    with open(filename, 'r') as file:
        blog_entries = file.readlines()
            
        positive_count = 0
        negative_count = 0

        for entry in blog_entries:
            entry_lower = entry.lower()

            for word in positive_words:
                if word in entry_lower:
                    positive_count += entry_lower.count(word)
                
            for word in negative_words:
                if word in entry_lower:
                    negative_count += entry_lower.count(word)

    print("\nResults:")
    print('Positive Words:', positive_count)
    print('Negative Words:', negative_count)



def main():
    filename = 'travel_blogs.txt'
    sentiment_analysis(filename)

if __name__ == "__main__":
    main()

