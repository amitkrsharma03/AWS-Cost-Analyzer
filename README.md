🚀 AWS Cost Optimizer & Predictor 🔥
📌 Project Overview
Tired of unexpected AWS bills? This project automates AWS cost tracking, visualizes spending trends, and helps you optimize costs using AWS services like Lambda, CloudWatch, S3, and IAM – all while staying within the AWS Free Tier! 🎯

🛠️ How It Works
1️⃣ AWS Lambda automatically fetches daily cost reports using Cost Explorer API.
2️⃣ CloudWatch triggers Lambda every day to keep data updated.
3️⃣ S3 stores historical cost data in JSON format.
4️⃣ Google Colab fetches the data from S3 and visualizes it using Matplotlib & Pandas.
5️⃣ IAM Roles & Policies secure access between services.

🔥 Features
✅ Automated Cost Tracking – No manual effort needed!
✅ Historical Cost Visualization – Get clear spending insights.
✅ Forecasting Ready – Can be extended for AWS cost predictions.
✅ Serverless & Free-Tier Friendly – No unexpected costs!

🏗️ Architecture Diagram
See in the repo!

📸 Screenshots
See in the repo!

🚀 How to Use
1️⃣ Setup AWS Services
Enable Cost Explorer in AWS.
Create IAM Roles & Policies (See /IAM-Config.md).
Deploy Lambda Function with Cost Explorer API.
Setup CloudWatch Scheduler for automation.
2️⃣ Upload Cost Data to S3
Run cost_fetcher.py to fetch and store cost reports in S3.
Confirm the data is stored properly.
3️⃣ Visualize the Data
Run cost_visualizer.py in Google Colab.

Fetch cost data from S3 and generate cost trends & insights.
🔥 Advanced Setup (Without Free-Tier Limitations)
If cost is not a concern, we can use more powerful AWS services instead of our current workaround:
Feature	Free-Tier Version	Paid/Advanced AWS Service
Cost Data Storage	S3 (Manual Upload)	Amazon Athena (Query Cost Data Dynamically) 📊
Cost Visualization	Google Colab + Matplotlib	Amazon QuickSight (BI Dashboards & Insights) 📈
Compute	Google Colab	EC2 or AWS Lambda (Automated Reports) ⚙️
Automation	CloudWatch Scheduler	AWS Step Functions (Fully Managed Workflow) 🔄
Forecasting	Manual Trend Analysis	AWS Cost Explorer (Forecasting Feature) 🔮

🔹 Athena would allow direct SQL-like querying of cost data without manual fetching.
🔹 QuickSight would provide interactive BI dashboards instead of Matplotlib graphs.
🔹 Step Functions could automate the entire pipeline seamlessly.
🔹 Cost Explorer Forecasting would give AI-driven cost predictions based on historical trends.

🏆 Why This Matters?
💡 Cost Optimization is KEY in AWS! This project helps track and reduce costs, making cloud spending predictable and manageable for individuals & businesses alike.

📜 License
MIT License – Free to use & modify!

🤝 Contributions
Want to improve this? PRs are welcome! 🙌
