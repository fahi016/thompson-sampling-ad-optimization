Thompson Sampling for Ad Optimization
This repository contains Python code implementing Thompson Sampling, 
a Bayesian approach to solve the multi-armed bandit problem for ad optimization.

Usage
Clone the repository:
git clone https://github.com/your-username/thompson-sampling-ad-optimization.git
cd thompson-sampling-ad-optimization

Install dependencies:
pip install numpy pandas matplotlib

Run the script:
python thompson_sampling.py
Description
The thompson_sampling.py script uses Thompson Sampling to select ads based on click-through rates (CTR) from the
provided dataset (Ads_CTR.csv). It iteratively updates beliefs about each ad's CTR using Beta distributions, 
balancing exploration and exploitation.

File Structure
thompson_sampling.py: Python script implementing Thompson Sampling.
Ads_CTR.csv: Dataset containing ad click-through rates.
Detailed_explanation_of_code.pdf: Detailed explanation of the Python code implementation.
Explanation_of_Thompson_Sampling.pdf: PDF file explaining the theory and concepts of Thompson Sampling.
