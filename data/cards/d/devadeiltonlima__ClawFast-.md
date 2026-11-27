# devadeiltonlima/ClawFast-

⭐ 10 · MIT · 推送 2026-11-26 · [GitHub](https://github.com/devadeiltonlima/ClawFast-) · 个人维护

**终端里的 AI 渗透测试 Agent：recon、漏洞验证到报告**

ClawFast 是一个运行在终端（另有 Windows 桌面 App，beta）的 AI 安全 Agent，用葡萄牙语对话驱动：执行命令、发 HTTP 请求、映射目标、发现漏洞并生成报告（laudo）。功能包括只读代码审计、子域/端口 recon、四 Agent 编排评估（Discovery/Web/Source/Validator）、Google Dorks、逆向工程（APK/ELF/PE 等）。以单一可执行文件分发，内置运行时，无需 Node/npm；密钥保存在本地，支持通过 /api 接入 25 个 AI 网关、Tor 出口与 safe-mode 确认，并要求仅在获授权的系统上使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单二进制分发，内置运行时，安装前校验 SHA-256
- 兼容 Claude/Codex 格式的 SKILL.md 技能安装与适配
- 通过 MCP 让 Claude Code/Codex/Gemini 驱动 clawfast（127.0.0.1 + token）
- 上下文自动压缩与模型故障时自动 fallback

## 适用场景

- 对已授权目标做 recon 并验证 IDOR/SSRF 等漏洞
- 在项目目录内做只读安全代码审计
- 通过 Dorks 搜索暴露的备份、配置与 .git

## 场景标签

`编码 Agent` `网络安全` · 领域:编码与开发

## 证据(README 行号)

> L17: O clawfast é um operador de segurança que trabalha na sua frente. Ele roda comando, faz requisição HTTP, mapeia o a
> L84: |**25 gateways de IA**|`/api` conecta NVIDIA, OpenRouter, Gemini, OpenAI, Claude, Groq, DeepSeek, Ollama, LM Studio
> L155: **Instalar:** baixe o `clawfast-app-windows-x64.exe` e rode. O motor vem dentro do instalador, então não precisa i


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `d2ca9ffab0ad` · [字段定义](../../DATASET.md)*
