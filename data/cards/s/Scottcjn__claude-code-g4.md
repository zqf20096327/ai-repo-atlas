# Scottcjn/claude-code-g4

⭐ 76 · C · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/Scottcjn/claude-code-g4) · [官网](https://rustchain.org) · 个人维护

**在 PowerPC G4/G5 老 Mac 上运行 Claude Code 的移植项目**

面向 Mac OS X Tiger (10.4) 与 Leopard (10.5) 的 PowerPC G4/G5 机器，移植 Claude Code 的使用能力：提供 Python 2.3 可用的 Claude API 客户端、QuickJS 的 JavaScript 实现，以及解决老系统 TLS 1.0 限制的 HTTP 代理助手。绕过无 Node.js、无现代 SSL 的限制，两条路径为 Python+TLS 代理和本地编译 QuickJS。已在 Power Mac G4、PowerBook G4、Power Mac G5 实机上验证。README 自称实验性移植。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- Python 与 QuickJS 两种在 Tiger/Leopard 上运行的实现路径
- 通过现代机器代理 HTTPS 解决老系统 TLS 1.0 限制
- 带 Tiger/Leopard 补丁的 QuickJS 及 G5 专属构建变体
- 在 G4/G5 实机（含双 1.25GHz G4、双 2.0GHz G5）上验证

## 适用场景

- 让收藏的 PowerPC 老 Mac 也能调用 Claude Code
- 在无 Node.js 的老系统上获得现代 JavaScript 运行环境（QuickJS）
- 复古硬件爱好者研究老平台移植方案

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L8: This is an experimental port of Claude Code concepts for Mac OS X Tiger (10.4) and Leopard (10.5) on PowerPC G4/G5 p
> L14: |`claude_code_g4.py`|Python Claude API client for Tiger|
> L36: QuickJS provides modern JavaScript on Tiger:


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c5cc84e2f5d8` · [字段定义](../../DATASET.md)*
