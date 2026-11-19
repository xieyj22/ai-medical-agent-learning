# AI 医疗全栈算法工程师学习计划

本项目是 12 周学习路线的实践仓库，目标是从零完成一个可演示、可复盘、可继续迭代的 AI 医疗 Agent 产品。

## 项目目标

最终产出：

1. 主项目：医疗知识库 RAG Agent
2. 小项目 1：病历结构化助手
3. 小项目 2：医疗报告生成 / 随访助手
4. 项目文档、截图、演示视频与仓库链接

## 技术路线

- 前端：Streamlit / Gradio，后续可选 React / Next.js
- 后端：FastAPI
- 数据库：SQLite，后续可选 PostgreSQL
- AI：大模型 API、Prompt、结构化输出、Tool Calling、RAG、Agent
- 工程：Python 3.12、Git、GitHub/Gitee、虚拟环境

## 当前状态

- [x] 开发环境、命令行、Python 基础、虚拟环境
- [ ] Git / GitHub / Gitee、项目结构、README
- [ ] HTTP、API、JSON、前后端通信
- [ ] Claude Code / Codex 基本协作流程
- [ ] 读懂、修改、调试 AI 生成代码
- [ ] 需求拆解：页面、接口、数据库、AI 调用、业务流程
- [ ] 查资料、读报错、定位 Bug 的基础方法

## 本地运行

当前阶段还没有应用代码。Python 环境要求 3.12。

```powershell
python --version
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

如果还没有 `requirements.txt`，先跳过最后一条命令。

## 目录结构

```text
medical_p agent/
├── README.md
├── .gitignore
├── .env.example
├── requirements.txt
├── app/
├── tests/
└── notes/
    └── _progress.md
```

## 说明

本项目用于学习和演示，不构成医疗诊断建议。
