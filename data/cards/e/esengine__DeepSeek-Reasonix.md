# esengine/DeepSeek-Reasonix

⭐ 35,842 · Go · MIT · 推送 2026-10-18 · [GitHub](https://github.com/esengine/DeepSeek-Reasonix) · [官网](http://reasonix.io/) · 个人维护 · 中文 README

**开源终端/桌面编码 Agent：读写代码、跑命令与测试**

Reasonix 是开源 AI 编码助手，程序运行在用户本地，模型由用户自行配置并直接付费。用户用自然语言描述任务，它在指定项目文件夹内读取代码、编辑文件、运行命令与测试，并展示每步操作；支持权限分级、plan 模式与按会话回合的文件回滚（仅覆盖其编辑工具改动的文件）。分发形态包括 Studio 桌面应用、终端 CLI/TUI、浏览器界面与 VS Code 等 ACP 编辑器扩展，四者为同一引擎。2.x 处于活跃开发，1.x 处于维护状态。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 动量与使用信号

- 维护:`active` — 距上次 push 0.6 天,年发版 100,158 位贡献者
- 涨星:近 1 天 **+12**(自 20261016 起算)
- 安装:npm 包 `reasonix` 月下载 18,541
- 平台:— · 协议:OPENAI-API / MCP

## 能力要点

- DeepSeek 内置预设，任意 OpenAI 兼容端点经一条配置即可接入
- MCP 服务器提供工具/提示/资源，Extension Protocol 可拦截运行时事件
- CGO_ENABLED=0 单二进制静态分发，一条命令交叉编译六个目标
- 编辑工具改动的文件按会话回合可回滚，不触碰 git 历史

## 适用场景

- 在终端里用自然语言让 Agent 完成改代码、跑测试的任务
- 通过 VS Code 扩展在编辑器内使用带审批的编码助手
- 接入自有 OpenAI 兼容模型服务做本地编码代理

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L37:  An open-source coding agent for your terminal, desktop, browser and editor.
> L54: Reasonix is an open-source AI coding assistant. The program runs on your computer; the AI model is a service you co
> L113: - **Multi-model & composable.** DeepSeek ships as a preset; any

---
*卡片 v1 · prompt 1.4 · 生成 2026-10-18 · 置信度 high · 依据 README sha `93ca03e3f937` · [字段定义](../../DATASET.md)*
