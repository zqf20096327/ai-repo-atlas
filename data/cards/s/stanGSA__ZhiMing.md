# stanGSA/ZhiMing

⭐ 90 · Python · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/stanGSA/ZhiMing) · [官网](https://zhiming.mom) · 个人维护 · 中文 README

**给对命理与 AI 感兴趣的用户：事实可核验的多智能体命理咨询应用与 MCP Server**

从零手写的 Python LLM Agent 框架（不依赖 LangChain/LangGraph），围绕塔罗、西方占星、八字、五格、解梦、每日运势六个确定性插件构建。所有符号事实（星历、宫位、节气、干支、牌面）由确定性代码计算，LLM 仅做综合叙述，且回答中每条事实与 ref_id 逐项经代码校验，不匹配即拒绝并重写。支持 single/multi 两种执行模式、层级 token 预算、危机表达安全边界；另提供 10 个工具的 MCP stdio Server 供 Claude Desktop 调用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `dual` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 确定性排盘 + 逐项事实校验，幻觉回答被代码拒绝并重写
- multi 模式：编排器并行调度最多 5 个隔离领域专家并合并跨系统信号
- 10 个确定性工具的 MCP stdio Server，服务内部零 LLM 调用
- 危机表达即时中断并提供地区匹配的求助热线

## 适用场景

- 在 Claude Desktop 中接入八字/占星/塔罗确定性排盘工具
- 通过 CLI 或 Web UI 进行带事实溯源的命理咨询
- 作为 LLM Agent 工程的事实性约束参考实现

## 场景标签

`Agent 框架` `多智能体` `聊天机器人` · 领域:Agent 开发

## 证据(README 行号)

> L17: **ZhiMing** is a **framework-free LLM agent harness** written from scratch in Python (no LangChain, no LangGraph), 
> L63: `mcp_server/` exposes **10 deterministic calculation and lookup tools** over standard Model Context Protocol (MCP) 
> L141: Copy `.env.example` to `.env` and set `DEEPSEEK_API_KEY` (default model `deepseek-flash` in `config.yaml`). OpenAI


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `f8423482baaf` · [字段定义](../../DATASET.md)*
