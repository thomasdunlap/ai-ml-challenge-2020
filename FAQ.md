# AI/ML Challenge 2020 - Frequently Asked Questions


## Is there a restriction on what platform/interface the solution uses?

We have no restrictions on the technology used in the solution other than those listed in the [challenge website](https://www.challenge.gov/challenge/GSA-artificial-intelligence-AI-machine-learning-ML-challenge/).

## What is your preference for the solution model type, such as “black box” models?

- You can submit whatever type of solution you choose, as long as it fulfills the criteria listed on the [challenge website](https://www.challenge.gov/challenge/GSA-artificial-intelligence-AI-machine-learning-ML-challenge/).
 
- In the Accuracy and Technical Evaluation section of the [Scoring Rubric](reference/AI_ML%20Challenge%20Scoring%20Rubric.pdf), the highest score of 5 indicates a solution that clearly explains the reasons for predictions made using the validation data, whereas a score of 1 indicates a "black box" solution. However, this is only one part of the scoring rubric, so it is up to you to determine what type of model is best for you. 

## May we include a commercially available product in our solution?

Please refer to the Ownership section of the [challenge website](https://www.challenge.gov/challenge/GSA-artificial-intelligence-AI-machine-learning-ML-challenge/) for details surrounding rules for products used in your solution. 

## Is there a standard way to determine how to separate documents into individual clauses?
Our advice is to make your best judgment on clauses, and refer to the Functionality and User Interface section in the [Scoring Rubric](reference/AI_ML%20Challenge%20Scoring%20Rubric.pdf): specifically, "The user interface of the solution is realistic and usable by a business user.” Thus, we encourage you to split clauses as you think would be most usable for a business user.

## Will other participants be able to see my submission?
The portion of your submissions that are uploaded to github are shared publicly (Validation Data File, Description of Methods Document, Source Code, Input Data, and Compiled Models). Thus, once you submit your solution to Github, it will be viewable by the public. See the [challenge website](https://www.challenge.gov/challenge/GSA-artificial-intelligence-AI-machine-learning-ML-challenge/) for a list of submission items that are sent via email and uploaded to github.

## Can you provide additional training data?
At this time, we are not planning to provide any additional training data. If we do, it will be posted in the [data](data) folder of this repository.

## Can we share our participation in the Challenge publicly, such as in a press release or a blog?
Yes!

## Can we ask questions to subject matter experts about EULAs?
Please direct any questions surrounding EULA classification to [challenge2020@gsa.gov](mailto:challenge2020@gsa.gov), and we will forward your question(s) to the relevant legal experts.

## How did you choose the metrics (F1 Score, Brier Score) to score submissions?
Below is more information about the F1 Score and Brier Scores as metrics for scoring:
 
### Brier Score
- Good for binary outcomes
- Answers the question: “How large was the error in the prediction?”
- Smaller scores (closer to zero) indicate better forecasts

### F1 Score
- Combines precision and recall into one metric
- Appropriate for imbalanced binary classification
- Best value at 1 and worst score at 0

## Who can participate in the challenge?
We welcome many types of solvers to participate, including individuals, teams, students, commercial companies, startups, and others. Please refer to the ‘Eligibility to Participate’ section of the [challenge website](https://www.challenge.gov/challenge/GSA-artificial-intelligence-AI-machine-learning-ML-challenge/) to see if you are eligible to participate. 

## How do we calculate the self-reported metrics of our solution?
You should split the training data provided into a training dataset and a test dataset. You should use the test dataset to calculate your self-reported metrics using the appropriate methods of calculating those metrics. You should decide the portion of the data to set aside as test data based on your own expertise.
