# Jetbrains AI Code Completion Internship - Test Task Report

I explored the capabilities of tiny_starcoder in completing code segments from my personal projects. 

Initially, I worked with longer code segments (up to 2048 tokens) and tried to predict larger chunks of missing code (1-15 lines of code). However, this didn't work well - tiny_starcoder mostly generated nonsense, which makes sense given its size (164M parameters). I considered using larger models like the regular starcoder, but the computational requirements and processing time made this impractical for this project.

I then changed my approach by using shorter code snippets (<512 tokens), reducing the size of the missing segments (1-3 lines of code), and selecting code segments more carefully. This adjustment proved more effective, leading to more reasonable completions from the model.

I manually reviewed each completion using a 5-point scale:
1. Completely incorrect
2. Partially correct but mostly wrong
3. Almost acceptable but still incorrect
4. Acceptable
5. Perfect match

While many completions still received low scores (mostly 1s), there were several acceptable and even perfect completions, showing that the model can be effective in certain contexts.

To evaluate the model more automatically, I used several automatic metrics:
- Exact Match
- CHRF
- BLEU
- ROUGE-L
- Levenshtein Distance

For correlation analysis, I used Pearson and Spearman correlation coefficients. As expected, CHRF, BLEU and ROUGE-L showed positive correlation, and Levenshtein distance showed negative correlation with manual reviews. Exact match had weaker correlation, since only one example had a perfect match.

Despite working with a small dataset (22 examples), the results provided valuable insights into both the model's capabilities and evaluation methods. The correlation between some automatic metrics and manual reviews was surprisingly strong, suggesting that these metrics could be useful in code completion tasks.

While tiny_starcoder has limitations, it showed potential for simple code completion tasks. The experience also gave me practical exposure to working with code completion models and evaluation metrics, some of which I hadn't used before.

The correlation results suggest that ROUGE-L and BLEU might be particularly useful for automated evaluation of code completion tasks, though no single metric perfectly matched human judgment.


