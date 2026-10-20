# bytedance/deer-flow

⭐ 84,072 · Python · MIT · 推送 2026-10-18 · [GitHub](https://github.com/bytedance/deer-flow) · [官网](https://deerflow.tech) · 组织维护 · 中文 README

**面向开发者的长时程 SuperAgent 编排框架：研究、编码与创作**

DeerFlow 是字节跳动开源的 super agent harness，通过编排子代理、记忆、沙箱与可扩展技能来处理耗时数分钟到数小时的任务。安装提供 make setup 交互式向导，引导选择 LLM 提供商、可选网络搜索及沙箱/bash/文件写入等安全偏好，生成 config.yaml 与 .env；另有面向编码代理的一句话引导安装说明。README 详述多种搜索/抓取后端（Brave、Tavily、DuckDuckGo、Serper、InfoQuest、Jina 等）对畸形响应的结构化错误处理，并提供 make doctor 自检与 make support-bundle 问题诊断包。v2.0 为完全重写，v1.x 分支继续维护原 Deep Research 框架。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.8 天,年发版 2,457 位贡献者
- 涨星:近 1 天 **+72**(自 20261016 起算)
- 安装:npm 包 `@minimax-ai/code` 月下载 57,110
- 平台:— · 协议:OPENAI-API / MCP / OLLAMA

## 能力要点

- 编排子代理、记忆与沙箱的长时程任务 harness
- make setup 交互式向导配置 LLM 提供商与安全偏好
- 多种网络搜索与抓取后端的结构化错误处理
- make doctor 自检与 support-bundle 问题诊断流程

## 适用场景

- 搭建能自主完成研究、编码与内容创作的长时程代理
- 为代理任务配置沙箱、bash 访问与文件写入等安全选项
- 接入多种网络搜索/抓取后端做深度调研

## 场景标签

`Agent 框架` `多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L12: DeerFlow (**D**eep **E**xploration and **E**fficient **R**esearch **Flow**) is an open-source **super agent harness
> L17: > **DeerFlow 2.0 is a ground-up rewrite.** It shares no code with v1. If you're looking for the original Deep Resea
> L103:  This launches an interactive wizard that guides you through choosing an LLM provider, optional web search, and ex

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 mid · 依据 README sha `921f4d5ae80e` · [字段定义](../../DATASET.md)*
