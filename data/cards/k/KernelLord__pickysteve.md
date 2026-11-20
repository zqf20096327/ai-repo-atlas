# KernelLord/pickysteve

⭐ 10 · Python · MIT · 推送 2026-07-16 · [GitHub](https://github.com/KernelLord/pickysteve) · 个人维护

**为 Claude Code/Cursor/Aider 等编码 agent 自动选配技能并过滤注入的中间层**

PickySteve 是一个轻量编排层：用便宜模型判断请求需要哪个技能，检索该技能并组装带不可信数据边界的上下文，再交给执行模型。流程含十个阶段：安全门扫描原始请求与每个检索候选（基于 stackone-defender 与 ONNX 分类器）、路由、BM25+嵌入混合检索、bge-reranker 重排、支配比例门控、组装。模型通过 OpenAI 兼容 API 接入，基准测试基于本地 Ollama qwen3:8b。当前为 Phase 1 MVP，无 PyPI 包，需 uv/git clone 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 两遍 fail-closed 安全门：原始请求与每个检索候选均经注入扫描，超时/错误时拒绝放行
- 检索文档以随机 nonce 边界包裹，防止被污染的技能文档伪造系统指令
- BM25+嵌入 RRF 融合检索与 bge-reranker-base 重排，附带支配比例门控
- 一条命令接入 18 个 agent（MCP stdio 或 OpenAI 兼容代理 :8077/v1）

## 适用场景

- 给 Claude Code/Cursor 等 agent 配置自动技能路由，避免把所有工具塞进上下文
- 为 MCP 技能生态加一层 prompt-injection 过滤
- 在本地 Ollama 上离线运行技能检索与路由

## 场景标签

`编码 Agent` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L13: PickySteve is a lightweight orchestration layer. A cheap model figures out which skill a request
> L49: Supports **Claude Code, Codex, Cursor, Windsurf, Cline, Roo Code, Gemini CLI, Qwen Code, Goose,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `d4dca87956a6` · [字段定义](../../DATASET.md)*
