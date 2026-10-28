# Scottcjn/claude-code-monterey

⭐ 79 · Apache-2.0 · 推送 2026-08-06 · [GitHub](https://github.com/Scottcjn/claude-code-monterey) · [官网](https://rustchain.org) · 个人维护

**在 macOS Monterey 上安装运行 Claude Code 的兼容性文档**

记录 Claude Code 2.0.76 在 macOS Monterey 12.7.6（2013 Mac Pro、Intel x86_64）上成功运行的安装指南与兼容性文档：通过 nvm 安装 Node.js v22.21.0，再经 npm 全局安装 @anthropic-ai/claude-code，并给出 shell 集成、更新、故障排查（npm 未找到/权限错误/自动更新）步骤。另汇总多平台兼容信息（x86_64、ARM64，IBM POWER8 另见相关仓库）。仓库本体不提供代码，仅提供文档。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 nvm 安装、Node.js 版本固定（v22.21.0）、npm 全局安装的完整步骤
- 记录已验证的测试环境（Monterey 12.7.6 / Intel Xeon / Node v22.21.0）
- 附故障排查与自动更新说明
- 汇总多平台架构兼容信息（x86_64 / ARM64 / POWER8）

## 适用场景

- 在老款 Intel Mac（Monterey）上安装并运行 Claude Code
- 排查旧系统下 npm/权限等安装问题
- 了解 Claude Code 在非常见平台上的兼容情况

## 场景标签

 · 领域:开发工具文档/AI CLI

## 证据(README 行号)

> L1: # Claude Code for macOS Monterey (12.x)
> L12: ## Installation Steps


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `e75cf00079c4` · [字段定义](../../DATASET.md)*
