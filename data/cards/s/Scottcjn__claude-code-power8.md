# Scottcjn/claude-code-power8

⭐ 89 · Apache-2.0 · 推送 2026-09-26 · [GitHub](https://github.com/Scottcjn/claude-code-power8) · [官网](https://rustchain.org) · 个人维护

**在 IBM POWER8/ppc64le 上安装运行 Claude Code CLI 的移植与安装指南**

提供 Anthropic Claude Code CLI 在 IBM POWER8 (ppc64le) Linux 上的可运行安装方案：锁定最后一个纯 JavaScript 版本 v2.1.112（v2.1.113 起上游改发平台专属 SEA 二进制，无 ppc64le 包），并附本仓库预编译的 ppc64le ripgrep 二进制与 v2.0.70 离线完整包。文档说明 Node.js ≥18 前置（可用官方预编译或源码构建）、各架构支持矩阵、供应商原生二进制缺口（audio-capture 未构建，语音模式不可用）与后续路径。已在 S824（Ubuntu 20.04）端到端验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 锁定纯 JS 版本 v2.1.112 作为 ppc64le 可用的版本上限
- 提供 ppc64le 预编译 ripgrep 二进制与离线安装包
- 给出各架构 SEA 二进制支持矩阵与 s390x/riscv64 推断结论
- 在真实 S824 硬件上完成 /login 与非交互 prompt 端到端验证

## 适用场景

- 在 POWER8 服务器上安装并运行 Claude Code CLI，免去转 x86 环境
- 了解上游 SEA 分发对非主流架构的影响与应对方案
- 离线或内网环境部署 Claude Code（缓存离线包）

## 场景标签

 · 领域:开发工具/跨架构移植

## 证据(README 行号)

> L12: **The First POWER8 Port of Claude Code — Running as of 2026-04-18 on v2.1.112.**
> L39: Assumes you have a working `node` and `npm` on PATH. Skip to *Node.js prerequisite* below if you need to build Node
> L79: |`binaries/ripgrep-ppc64le-linux.tar.gz`|Pre-built ripgrep 15.x for ppc64le (~2 MB). Used by Claude Code's Grep/Glo


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `91320563d37d` · [字段定义](../../DATASET.md)*
