# bernatsampera/show-context

⭐ 3 · JavaScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/bernatsampera/show-context) · 个人维护

**本地页面展示 Claude Code 会话读取了什么及其来源**

面向 Claude Code 用户的 CLI 工具：在会话内运行后生成本地 HTML 页面，按真实 token 占用展示会话加载的 system prompt、工具定义、CLAUDE.md、skills、MCP 内容与每次文件/搜索/网页读取，并支持选中等回答追溯到其来源文件的具体行。通过 npm 全局安装或 npx 直接运行，需 Node.js 22+，无依赖；仅溯源功能经本地 Claude Code CLI 使用网络。依赖 Claude Code 的 transcript 格式，子代理读取暂不展示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按真实 token 用量展示会话上下文构成，可按大小过滤读取项
- 回答溯源：选中文本链接到所读文件的精确行
- 单文件自包含 HTML 输出，本地服务仅绑定 127.0.0.1 并带随机 token 验证
- 支持 --static、--no-open、会话 ID 选择与环境变量配置

## 适用场景

- 查看 Claude Code 会话的 token 都花在了哪些上下文上
- 核实某条回答依据的是哪些文件内容
- 决定会话中哪些加载项可以裁剪

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L9: Run it inside any Claude Code session (as `! npx show-context`). It opens one local page with the whole conversation
> L17: You can't see any of that from the chat. show-context makes it visible, so you know what to trim and which answers 
> L64: - Reads are files, shell reads and searches, MCP reads, skills and web results. Writes, edits and commands that run


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `a34d17450874` · [字段定义](../../DATASET.md)*
