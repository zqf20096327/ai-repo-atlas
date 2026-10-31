# SamuelFrost/super_projects

⭐ 21 · Python · NOASSERTION · 推送 2026-10-29 · [GitHub](https://github.com/SamuelFrost/super_projects) · 个人维护

**面向开发团队与 AI agent 的容器化父目录开发环境模板**

以 Dev Container 规范为基础的容器化开发环境模板：将 Docker、常用工具链（git/gh、Node/Python、mise、Chrome 远程调试）、XFCE 桌面 GUI（VNC/noVNC）、SSH agent 与 known_hosts 转发、Docker socket 挂载等配置代码化，通过 git fork 在团队/组织内共享。AI 部分为预置的 Gemini、Cursor、VS Code、Claude、Codex 工具配置及引导 agent 行为的属性集合，是环境中的组成部分而非本体功能。支持 VS Code、Cursor、Zed、JetBrains 等多种 IDE 与纯 CLI 方式使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Ubuntu 24.04 容器内置工具链与浏览器 VNC 桌面 GUI
- SSH agent/known_hosts 自动转发与 1Password/macOS Keychain 支持
- 预置 Gemini/Cursor/VS Code/Claude/Codex 的 AI 工具配置
- Docker outside of Docker 与 localhost 端口转发代理

## 适用场景

- 团队用一份 git 仓库统一共享开发环境配置
- 为 AI agent 提供带浏览器与工具的标准化容器工作环境
- 无 IDE 场景下用 devcontainer CLI 或 Docker Compose 启动环境

## 场景标签

 · 领域:开发工具/DevOps

## 证据(README 行号)

> L5: `super_projects` is a template for a containerized development environment designed to be your projects' parent dire
> L119: - AI tooling configurations for Gemini, Cursor, VS Code, Claude, and Codex.


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `2fc78cff7804` · [字段定义](../../DATASET.md)*
