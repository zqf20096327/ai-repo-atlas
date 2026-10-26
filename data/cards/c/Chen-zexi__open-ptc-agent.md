# Chen-zexi/open-ptc-agent

⭐ 731 · Python · MIT · 推送 2026-01-21 · [GitHub](https://github.com/Chen-zexi/open-ptc-agent) · 个人维护 · 中文 README

**开源实现 Anthropic 程序化工具调用（PTC）的代码执行 Agent 框架**

对 Anthropic 提出的 Programmatic Tool Calling（PTC）范式的开源实现：Agent 以在沙箱中编写并执行代码的方式调用工具，而非逐个 JSON 工具调用，代码在沙箱内处理数据、仅将最终结果返回模型。基于 LangChain DeepAgents 组件构建，沙箱由 Daytona 提供，支持任意 MCP 服务器工具自动转为 Python 函数、按需渐进式工具发现、子代理后台执行与 Agent Skills 标准，可配置 Anthropic/OpenAI 等多 LLM。提供核心库与交互式 CLI，需 Python 3.12+、Node.js 与 uv，通过 git clone 源码安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 以代码执行替代逐个 JSON 工具调用的 PTC 范式，宣称减少 token 消耗
- 任意 MCP 服务器工具自动转换为 Python 函数，支持渐进式工具发现
- Daytona 沙箱后端：文件系统隔离与快照支持
- 子代理后台并行执行、任务规划与对话自动摘要等中间件

## 适用场景

- 让 Agent 处理大体量结构化数据（如金融时序数据）并在沙箱内计算后再返回结果
- 将现有 MCP 服务器工具接入代码执行式 Agent 工作流
- 通过 CLI 交互式运行或以 Python 库、LangGraph API 形式集成部署

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: This project is an open source implementation of Anthropic recently introduced Programmatic Tool Calling (PTC), whi
> L36: > **Built on LangChain DeepAgents** - This project uses many components from DeepAgents and cli feature was bootstr
> L57: │   ├── ptc-agent/             # Core agent library

## 星数曲线

```mermaid
xychart-beta
    title "Chen-zexi/open-ptc-agent 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26"]
    y-axis "stars" 729 --> 732
    line [730, 731, 731]
```

2026-10-18 730 → 2026-10-26 731（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3de2ecba5317` · [字段定义](../../DATASET.md)*
