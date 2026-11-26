# erdalnacitunc-create/evren-desktop

⭐ 3 · TypeScript · MIT · 推送 2026-11-22 · [GitHub](https://github.com/erdalnacitunc-create/evren-desktop) · 个人维护

**EVREN LLM API 的开源 Windows 桌面客户端：Agent、MCP、终端**

基于 Electron + React + TypeScript 的 Windows 桌面客户端，接入 EVREN LLM API（OpenAI/Anthropic 兼容），用户从官方页面获取 API key 后使用可用模型。功能包括：工具调用 Agent、MCP 扩展管理、持久 PowerShell 终端与代码块一键运行、工作区文件读写与 diff/撤销、Plan/Build 模式、Git 面板与 worktree、子 Agent、多模型并行合成、定时任务、语音转录输入，并提供本地 OpenAI 兼容 HTTP 服务器（Headless API/SDK/ACP 桥）。Windows 安装包为未签名状态（SignPath 申请未获批准）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Agent 工具调用 + MCP 扩展（资源/prompt/elicitation/任务）
- 本地 OpenAI 兼容 HTTP 服务器 + SDK + ACP v1 stdio 桥
- 工作区文件工具、diff 与步骤级 checkpoint 回滚，Git 面板与 worktree
- 多模型并行合成、子 Agent、定时任务、语音转录输入

## 适用场景

- 在 Windows 桌面上通过 EVREN API key 使用多个 LLM 模型对话与 Agent 任务
- 让 Agent 读写项目文件、运行检查并执行 Git 操作
- 管理 MCP 服务器扩展并运行其工具
- 通过本地 Headless API/ACP 桥把客户端能力接入其他程序

## 场景标签

`AI 助手` `编码 Agent` `语音识别` · 领域:编码与开发

## 证据(README 行号)

> L3: EVREN LLM API'si (OpenAI ve Anthropic uyumlu) icin acik kaynak Windows masaustu
> L41: - Ajan (araclar) araç destekleyen modellerde varsayilan olarak aciktir.
> L114: - [x] Headless API + SDK + ACP


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `4e233b97b9f9` · [字段定义](../../DATASET.md)*
