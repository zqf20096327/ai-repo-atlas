# IamCatoBot/text2sim-MCP-server

⭐ 25 · Python · MIT · 推送 2025-11-28 · [GitHub](https://github.com/IamCatoBot/text2sim-MCP-server) · [官网](https://text2sim.com) · 组织维护

**让 LLM 通过 MCP 创建并运行仿真模型的工具服务器**

The Cato Bot Company 开发的 Model Context Protocol 服务器，使大语言模型能够通过自然语言创建、校验和执行仿真模型。支持两大范式：基于 SimPy 的离散事件仿真与基于 PySD 的系统动力学仿真，采用 JSON Schema 2020-12 校验配置。暴露 16 个 MCP 工具，覆盖仿真执行、模型校验、模型存储与模板管理、Vensim 模型转换等。提供等待时间、利用率、吞吐量等统计分析与置信区间，解析概率分布时不执行代码。安装依赖 Python 3.12+ 与 uv，通过 Claude Desktop 等客户端接入。

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

- 支持 SimPy 离散事件仿真与 PySD 系统动力学两种范式
- 暴露 16 个 MCP 工具（仿真执行/校验/模型管理/模板/Vensim 转换）
- JSON Schema 2020-12 校验与多模式验证（partial/strict/structural）
- 基于正则的分布解析，无代码执行，含输入校验的安全设计

## 适用场景

- 在 Claude Desktop 等客户端中用对话迭代构建排队/流程仿真模型
- 将自然语言描述的存量流量模型转为可执行的系统动力学仿真
- 复用内置模板快速搭建并多次复制仿真获取置信区间

## 场景标签

 · 领域:仿真建模/LLM 工具生态

## 证据(README 行号)

> L6: A Model Context Protocol server providing multi-paradigm simulation capabilities through conversational interfaces. 
> L10: Text2Sim MCP Server enables Large Language Models to create, validate, and execute simulation models through natura

## 星数曲线

```mermaid
xychart-beta
    title "IamCatoBot/text2sim-MCP-server 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `f9f4cb07661e` · [字段定义](../../DATASET.md)*
