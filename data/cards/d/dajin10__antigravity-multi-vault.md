# dajin10/antigravity-multi-vault

⭐ 3 · Python · 推送 2026-11-25 · [GitHub](https://github.com/dajin10/antigravity-multi-vault) · 个人维护 · 中文 README

**为 Antigravity IDE 用户提供 N 账号仓切换的桌面工作台 Skill**

面向 Antigravity IDE 的多账号管理 Skill：通过本地脚本保存/恢复 Electron 会话快照，支持从 1 仓扩展至 N 仓、一键切换账号（切换时重启会话）、移除仓位与演示模式隐私打码。附 PySide6/QtWebEngine 桌面工作台，本地 HTTP 端口 28888 提供状态与健康检查。README 以 Agent-First 形式编写，指定 AI Agent（Antigravity/Claude Code/Codex）按 4 步协议自动完成部署。凭据经操作系统原生安全存储读写，零遥测，数据仅存本地。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- N 槽位账号仓保存、切换（switch-restart）与删除，附旧版数据无损迁移
- PySide6 无边框桌面工作台，本地端口 28888 健康探针
- 面向 AI Agent 的 4 步自动安装部署协议（SKILL.md 调度）
- 凭据经 OS 原生安全存储读写，切号前自动备份会话

## 适用场景

- 在 Antigravity 中管理并快速切换多个账号
- 演示场景下一键打码隐藏账号邮箱
- 让 AI Agent 自动完成本工具的安装与初始化

## 场景标签

 · 领域:开发工具/账号管理

## 证据(README 行号)

> L5: > **从 1 个账号起步，无限扩展至 N 个账号的 Antigravity 多仓工作台 Skill。**
> L7: > **人类用户无需手动敲命令**：把本仓库交给你的 AI Agent（Antigravity / Claude Code / Codex），说一句 **“帮我安装并启动这个多仓工作台”**，AI 将自动完成环境检查、依赖安装、Sk
> L16: 检查 Python 3.8+ 与 `PySide6`（用于渲染无边框圆角 WebEngine 桌面工作台）：


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `8927b166da42` · [字段定义](../../DATASET.md)*
