# 📚 AI知识库问答

一个基于智谱 GLM-4-Flash 大模型的知识库问答网页应用，上传 PDF 文件后，AI 可基于文档内容精准回答你的问题。

## 功能
- 支持上传 PDF 文件，自动提取文档中的文本内容
- 展示文档基本信息（页数、字符数）及内容预览
- AI 严格基于文档内容回答问题，不编造答案
- 文档中无相关信息时，AI 会明确告知“文档中未提及此内容”

## 技术栈
- Python
- Streamlit（网页界面）
- 智谱 GLM-4-Flash（大模型）
- PyMuPDF（PDF 文本提取）
- python-dotenv（密钥管理）

## 如何运行
1. 克隆仓库：`git clone https://github.com/wanqiu-cloud/ai_knowledge_base.git`
2. 安装依赖：`pip install -r requirements.txt`
3. 创建 `.env` 文件并配置密钥（见下方）
4. 运行应用：`streamlit run app.py`

## 环境变量配置（.env）
ZHIPU_API_KEY=你的智谱API Key

## 项目结构
ai_knowledge_base/
- .env              # 密钥文件（需自行创建）
- .gitignore        # Git 忽略规则
- app.py            # 主程序
- requirements.txt  # 依赖清单
- readme.md         # 项目说明