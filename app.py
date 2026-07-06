import os
from dotenv import load_dotenv
import streamlit as st
import fitz
from openai import OpenAI

# 加载密钥
load_dotenv()

client = OpenAI(
    api_key=os.getenv("ZHIPU_API_KEY"),
    base_url="https://open.bigmodel.cn/api/paas/v4/"
)

st.set_page_config(page_title="AI知识库问答", page_icon="📚")
st.title("📚 AI知识库问答")
st.markdown("上传一个 PDF 文件，AI 基于文件内容回答你的问题。")

# 初始化知识库文本
if "knowledge_base" not in st.session_state:
    st.session_state.knowledge_base = ""

# 文件上传
uploaded_file = st.file_uploader("选择 PDF 文件", type=["pdf"])

# 注意：以下所有代码都在 if uploaded_file: 内部
if uploaded_file:
    with st.spinner("正在提取文档内容..."):
        pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in pdf_doc:
            text += page.get_text()
        
        # 先保存需要的信息
        page_count = pdf_doc.page_count
        text_length = len(text)
        
        # 再关闭文档
        pdf_doc.close()

        st.session_state.knowledge_base = text
        st.success(f"文档加载成功！共 {page_count} 页，{text_length} 个字符。")

    # 显示文档预览
    with st.expander("📄 查看提取的文档内容"):
        st.text_area("文档内容", text[:3000] + "..." if len(text) > 3000 else text, height=200)

# 问答部分（知识库非空时才显示）
if st.session_state.knowledge_base:
    st.subheader("💬 基于文档提问")
    user_question = st.text_input("输入你的问题，AI 会基于文档回答")

    if user_question:
        with st.spinner("AI 正在查找答案..."):
            system_prompt = (
                "你是一个基于文档内容回答问题的AI助手。"
                "请严格根据以下文档内容回答问题。"
                "如果文档中没有相关信息，请明确告知用户'文档中未提及此内容'，不要编造答案。"
                f"\n\n【文档内容】\n{st.session_state.knowledge_base}"
            )

            response = client.chat.completions.create(
                model="glm-4-flash",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_question}
                ]
            )

            ai_reply = response.choices[0].message.content

            st.subheader("🤖 AI 回答")
            st.write(ai_reply)
else:
    st.info("👆 请先上传一个 PDF 文件。")