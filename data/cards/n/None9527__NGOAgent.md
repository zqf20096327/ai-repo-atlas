# None9527/NGOAgent

⭐ 37 · TypeScript · NOASSERTION · 推送 2026-04-13 · [GitHub](https://github.com/None9527/NGOAgent) · 组织维护 · 中文 README

**Go 编写的本地优先自主 Agent 系统（边缘 AI OS）**

以 Go 语言实现的自主智能体系统，包含 10 状态 ReAct 决策引擎、LoopPool 并发隔离、可孵化独立子 Agent 的 Swarm 架构、23+ 原子工具（文件编辑、异步命令、搜索、Web 检索、记忆）、Forge 沙箱测试未验证代码、SSE 断线恢复遥测与 Allow/Auto/Ask 权限三档审批。支持接入本地模型（Ollama、vLLM）或私有云 API，数据不出本地。面向企业私有化部署，采用 DDD 架构与 BSL 1.1 许可证，需从源码构建（Go ≥1.24、Node.js ≥18）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 状态 ReAct 决策引擎与 LoopPool 并发隔离
- Go 并发实现的真实 SubAgent Swarm（独立例程与私有内存区）
- 23+ 原子工具连接操作系统，含异步 CLI 与 SearXNG 代理搜索
- Allow/Auto/Ask 三档权限钩子与 Forge 沙箱

## 适用场景

- 在私有环境部署可自主执行任务的 Agent 处理重构等复杂工作
- 金融/医疗等数据敏感行业本地接入 Ollama/vLLM 运行智能体
- 通过 WebUI 与 SSE 断线恢复跟踪 Agent 工具调用链

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L9: In an era where data privacy is paramount, NGOAgent emerges as a production-ready, autonomous AI operating system. D
> L21: ### 2. 🧠 Agentic LoopPool™ & State Machine Engine

## 星数曲线

```mermaid
xychart-beta
    title "None9527/NGOAgent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 36 --> 38
    line [37, 37]
```

2026-10-18 37 → 2026-10-28 37（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `7af53db58e8c` · [字段定义](../../DATASET.md)*
