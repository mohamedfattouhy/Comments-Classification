# MANAGE ENVIRONNEMENT
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from scrape_comments import comments_scraping
from comments_classification import Bert_Classification


def main():

    st.title("Scrape and classify comments")

    # Enter fields
    url = st.text_input("URL")
    regex_pattern = st.text_input("Regex Pattern")
    html_tag = st.text_input("HTML Tag")

    # Check input
    if st.button("Scrape"):

        if url and regex_pattern and html_tag:
            # Calling the comments_scraping function
            results = comments_scraping(url, regex_pattern, html_tag)

            # Display results
            st.subheader("Results")
            if results:
                st.write('Matches found ✅')
                st.write(f'{len(results)} comments were recovered')

                comments_classification = Bert_Classification(results)
                print(comments_classification)

                n_pos = comments_classification.count('Positive')
                n_neg = comments_classification.count('Negative')
                pos = ['Positive', n_pos]
                neg = ['Negative', n_neg]

                df = pd.DataFrame([pos, neg], columns=['Label', 'Count'])

                colors = {'Positive': '#2ECC71', 'Negative': '#C0392B'}
                # bar chart with plotly
                fig = go.Figure(data=[go.Bar(x=df['Label'],
                                             y=df['Count'],
                                             marker_color=[colors[val] for val in df['Label']],
                                             width=0.4
                                             )
                                      ]
                                )

                fig.update_layout(title='Comments classification',
                                  yaxis_title='Number of comments',
                                  showlegend=False)

                # Display the graph
                st.plotly_chart(fig)

            else:
                st.write("No comments found.")
        else:
            st.warning("Please fill in all the fields.")


if __name__ == "__main__":
    main()
