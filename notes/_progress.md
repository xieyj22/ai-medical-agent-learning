# Learning Progress

## Profile

- Goal: AI 医疗全栈算法工程师
- Notes directory: `F:\claude_work_new\medical_p agent\notes`
- Daily study time: 2 hours
- Total duration: 12 weeks
- Teaching mode: Guided
- Created date: 2026-11-19
- Final outcome: 1 main project + 2 small projects + project documentation and demo materials

## Plan

### Phase 1: 工程基础与 AI 编程工具 (Week 1-2)

- [x] 开发环境、命令行、Python 基础、虚拟环境 — 熟练
- [x] Git / GitHub / Gitee、项目结构、README — 熟练
- [ ] HTTP、API、JSON、前后端通信 — 熟练
- [ ] Claude Code / Codex 基本协作流程 — 熟练
- [ ] 读懂、修改、调试 AI 生成代码 — 熟练
- [ ] 需求拆解：页面、接口、数据库、AI 调用、业务流程 — 熟练
- [ ] 查资料、读报错、定位 Bug 的基础方法 — 熟练

Phase 1 output: a CLI tool submitted to GitHub/Gitee with README.

### Phase 2: Web 全栈基础 (Week 3-4)

- [ ] HTML / CSS / JavaScript 基础 — 了解
- [ ] Streamlit / Gradio 快速 Demo — 熟练
- [ ] FastAPI 接口开发 — 熟练
- [ ] 接口设计、参数校验、错误处理、环境变量 — 熟练
- [ ] SQLite 基础、数据表设计、增删改查 — 熟练
- [ ] 前后端调用完整链路 — 熟练

Phase 2 output: a minimal demo with medical Q&A frontend, FastAPI backend, and SQLite storage.

### Phase 3: 大模型应用与 Prompt 工程 (Week 5-6)

- [ ] 大模型 API 调用、消息格式、模型参数 — 熟练
- [ ] Prompt 设计：角色、任务、约束、示例、输出格式 — 熟练
- [ ] 上下文管理、多轮对话、消息裁剪 — 熟练
- [ ] 结构化输出、JSON Schema、结果校验 — 熟练
- [ ] Tool Calling / Function Calling — 熟练
- [ ] 医疗场景免责声明、幻觉控制、敏感信息处理 — 了解

Phase 3 output: medical record structuring assistant with structured JSON output and validation.

### Phase 4: RAG 医疗知识库 (Week 7-8)

- [ ] 文档上传与解析：PDF / TXT / Markdown — 熟练
- [ ] 文本切分、清洗、元数据记录 — 熟练
- [ ] Embedding、向量存储、相似度检索 — 熟练
- [ ] Prompt 拼接、证据引用、拒答策略 — 熟练
- [ ] 医疗 RAG 问答系统完整实现 — 精通
- [ ] 向量数据库基础概念 — 了解

Phase 4 output: medical knowledge base Q&A v1 with document upload, chunking, evidence citation, and rejection strategy.

### Phase 5: AI Agent 与工作流编排 (Week 9-10)

- [ ] AI Agent 架构：规划、工具、记忆、工作流 — 精通
- [ ] Agent 工具设计与循环控制 — 熟练
- [ ] LangChain / LangGraph / Dify / Coze 至少一种 — 熟练
- [ ] 工作流编排、任务自动化基础 — 熟练
- [ ] 多智能体协作概念 — 了解
- [ ] 日志、错误处理、可观测性基础 — 了解

Phase 5 output: medical RAG Agent v2 with tools including knowledge retrieval, record structuring, report generation, and follow-up question generation.

### Phase 6: 部署、项目打磨与投递材料 (Week 11-12)

- [ ] 部署上线：环境变量、日志、本地服务、云端部署基础 — 熟练
- [ ] 前端页面完善与交互优化 — 熟练
- [ ] 测试、Bug 修复、性能优化基础 — 熟练
- [ ] 项目文档：架构、核心逻辑、技术选型、难点、迭代路线 — 精通
- [ ] Demo 截图、演示视频、项目链接准备 — 熟练
- [ ] 最终复盘与岗位要求逐条对照 — 精通

Phase 6 output: a demonstrable, reviewable, iterable AI Agent product with README, architecture notes, screenshots, demo video, and repository link.

## Log

### 2026-11-19
- Started Phase 1, topic: 开发环境、命令行、Python 基础、虚拟环境.
- Completed (partial): command line basics (`cd`, quoted paths with spaces), Python interpreter/third-party libraries, global dependency conflicts, virtual environment activation scope, requirements.txt recovery concept.
- Corrections: virtual environments are session-activated, not automatically selected by the current directory; A's activated venv persists after `cd` to B, while a fresh shell with no activation uses global Python.
- Final review answered: 1-3 correct; command mistakes corrected: `pip -m venv` -> `python -m venv`, `pip install -m requirements.txt` -> `pip install -r requirements.txt`.
- Environment check: Python 3.14.5 active from `C:\Python314\python.exe`; three Python paths found; pip 26.1.1 matches 3.14. Python 3.12 also installed at `C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe`.
- Error corrected: initial venv command failed because the shell was cmd, where `&` is not the call operator; user then correctly used PowerShell. In cmd, use `Activate.bat`; in PowerShell, use `Activate.ps1`.
- Final hands-on verified: created `.venv` with Python 3.12; activated it; `python --version` = 3.12.0; `python -m pip --version` points to `F:\claude_work_new\medical_p agent\.venv\Lib\site-packages\pip`.
- Corrections: default Python is chosen by PATH order, not install time; PATH merges system+user entries and first matching directory wins; to prioritize 3.12 temporarily, prepend its directory.
- Notes: no separate note file generated yet.
- Next: Git / GitHub / Gitee, project structure, README.
- Git lesson review answered: commit saves a local snapshot in `.git`, push uploads it to a remote (GitHub/Gitee); `git add main.py` + `git commit -m "..."` is correct; `.env` must be ignored because it may contain API keys/passwords; monolithic 1000-line `main.py` is hard to read/debug/extend; README must explain scenario, tech/run steps, features/limits.
- Correction: `git add .` stages all current changes and untracked files, including debug files and `.venv` unless ignored; Q2 needs this reason explicitly.
- Hands-on verified: `git init` succeeded; wrong path `notes/progress.md` was corrected to `notes/_progress.md` (Git paths are literal); first local commit `546aa97` created with `.env.example`, `.gitignore`, `README.md`, `notes/_progress.md`; `.venv/` was correctly ignored; LF→CRLF warnings are normal Windows line-ending conversion, not errors.
- Remote push verified: added `origin` as `https://github.com/xieyj22/ai-medical-agent-learning.git`, renamed branch to `main`, pushed successfully; local `main` tracks `origin/main`.
- Next: HTTP、API、JSON、前后端通信.
