# th0r3nt/JAWL

⭐ 40 · Python · MIT · 推送 2026-08-31 · [GitHub](https://github.com/th0r3nt/JAWL) · 个人维护 · 中文 README

**构建持续循环自主 AI agent 的异步 Python 框架**

面向开发者的异步 agent 框架：以事件驱动 ReAct 循环运行自主 agent，含本地 Web 管理驾驶舱（实时心跳、参数编辑、操作员聊天、日志流）。内置 Qdrant+KuzuDB 混合向量-图谱 RAG 记忆、分形 ToT 规划、贝叶斯假设推理、Swarm 子代理编排、Gatekeeper OS 访问控制（0-3 级）及带回滚的自修改部署会话。支持 Windows/Linux/macOS，严格要求 Python 3.11，最低 4GB 内存并需 2GB swap。通过 git clone 源码安装，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 事件驱动 ReAct 循环的持续运行 agent 框架
- Qdrant 向量 + KuzuDB 知识图谱混合 RAG 长期记忆
- 本地 Web Cockpit：实时监控、参数编辑、操作员对话
- Gatekeeper 分级 OS 访问控制，无需强制 Docker 隔离

## 适用场景

- 构建长期驻留、按事件唤醒的自主 agent
- 通过 Web 驾驶舱监控和配置运行中的 agent
- 在本地机器上带访问控制地运行操作 OS/文件/网络的 agent

## 场景标签

`Agent 框架` `Agent 记忆` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L3: **JAWL** is an asynchronous framework for creating continuous-loop autonomous AI agents (Event-Driven ReAct Loop) fe
> L5: The project is built around the concept of an autonomous agent operating within an event-driven reasoning and acting

## 星数曲线

```mermaid
xychart-beta
    title "th0r3nt/JAWL 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 39 --> 41
    line [40, 40]
```

2026-10-18 40 → 2026-10-25 40（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `241900373060` · [字段定义](../../DATASET.md)*
