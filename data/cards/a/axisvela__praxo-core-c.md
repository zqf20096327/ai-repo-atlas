# axisvela/praxo-core-c

⭐ 3 · C · MIT · 推送 2026-11-26 · [GitHub](https://github.com/axisvela/praxo-core-c) · [官网](https://axisvela.github.io/praxo-core/languages/c/) · 组织维护

**面向 C 开发者的可嵌入 AI Agent 框架实现**

PRAXO-CORE 契约的 C11 实现，提供策略、工具调用、事件与检查点等 Agent 运行时能力，覆盖 OpenAI 兼容、Anthropic、Gemini 模型适配（调用方提供 HTTP 传输）、MCP 客户端、子代理委派、检索器等组件，附带 checkpoint、hitl、retry、structured-output 等十余个可运行示例与场景教程。该仓库为发现镜像，规范契约与参考实现在 monorepo 中；未发布安装包，仅支持源码 CMake 构建。声明本身不是托管模型、工作流引擎或安全控制器。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 提供 OpenAI 兼容/Anthropic/Gemini 三类模型适配，调用方提供 HTTP 传输，重新组装 SSE 流
- 内置 MCP 客户端、子代理委派、检索器与事件 sink 组合
- 支持策略绑定、工具范围、人工审批（hitl）与检查点编码/解码
- 提供 checkpoint、retry、provider-fallback、structured-output 等可运行示例与 7 个场景教程

## 适用场景

- 在 C/C++ 嵌入式工程中接入 LLM 并调用注册工具
- 为 Agent 调用设置策略、身份绑定与人工审批流程
- 实现流式输出、结构化输出校验与失败重试逻辑

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L3: C11 implementation of the PRAXO-CORE Core contract with source version `0.12.0`. The normative contract is `spec/`; 
> L40: |OpenAI-compatible model|native (transport seam)|`PxOpenAICompatible`; caller supplies HTTP transport; `px_openai_g
> L46: |Subagent delegation|native (synchronous seam)|`px_subagent_run`; no asynchronous manager|


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `2dd916811008` · [字段定义](../../DATASET.md)*
