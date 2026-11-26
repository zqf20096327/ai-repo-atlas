# tukorama/mcp-server-worldquantbrain

⭐ 3 · Python · MIT · 推送 2026-11-25 · [GitHub](https://github.com/tukorama/mcp-server-worldquantbrain) · [官网](https://pypi.org/project/mcp-server-worldquantbrain/) · 个人维护

**给 agent 接入 WorldQuant BRAIN 的 MCP 服务器与 LangChain 工具包**

非官方的 Model Context Protocol 服务器，将 WorldQuant BRAIN API 的数据字段查询、Fast Expression alpha 回测与结果读取封装为一组工具，供 Claude Code、Cursor、Claude Desktop、VS Code、ChatGPT 等 MCP 客户端调用；同一工具集也可通过 langgraph extra 作为 LangChain 工具在进程内使用，并附预构建 agent。针对 agent 驱动回测的常见问题做了机制设计：超时模拟返回 PENDING id 可续查、本地台账复用相同模拟避免重复消耗配额、返回裁剪后的结构化结果、会话落盘复用、submit_alpha 默认关闭并需显式开启。需 WorldQuant BRAIN 账号登录。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器 + LangGraph/LangChain 工具双形态，附预构建 agent 与 Mermaid 图生成
- 本地台账（ledger）复用相同模拟结果，避免重复消耗回测配额
- 超长模拟返回 PENDING id 由 get_simulation_status 续查，写入操作不自动重试
- submit_alpha 默认关闭，开启后先跑 BRAIN 检查与自相关门槛，支持人工确认步骤

## 适用场景

- 在 Claude Code 或 Cursor 中用自然语言查找数据字段并回测 alpha
- 用 LangGraph 构建带人工审批环节的 alpha 提交流程
- 管理多进程共享的回测台账，避免重复模拟浪费配额

## 场景标签

`金融量化` · 领域:学习与行业

## 证据(README 行号)

> L7: `mcp-server-worldquantbrain` is a Model Context Protocol (MCP) server for the
> L8: WorldQuant BRAIN API, with the same tools packaged for
> L9: LangGraph and LangChain. It lets an agent look up data fields, backtest Fast Expression (FASTEXPR)
> L107: The `langgraph` extra gives you plain LangChain tools in the same process, with no MCP server to


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `67637fe1ea1a` · [字段定义](../../DATASET.md)*
