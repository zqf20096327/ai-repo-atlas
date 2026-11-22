# williamdh457/claude-anti-ban

⭐ 5 · PowerShell · MIT · 推送 2026-11-17 · [GitHub](https://github.com/williamdh457/claude-anti-ban) · 个人维护 · 中文 README

**面向 Claude 用户的防封环境配置 skill：让 AI 自动完成一致性环境搭建**

一个装入 Claude Code / Codex / Cursor 等 agent 的 skill 仓库：用户发出一段指令后，AI 按预设流程探测系统环境、清理旧账号痕迹、搭建代理节点、配置分流规则、对齐时区语言、封堵 DNS/WebRTC 泄露、可选建 Hyper-V 虚拟机，最后渲染一份 DOCX 使用手册。核心机制是把出口 IP、时区、语言、DNS、支付方式对齐到同一身份。附独立脚本（环境自检、IP 检测、痕迹清理、分流配置），不装 skill 也可单独运行。README 声明不修改客户端、不伪造身份、不绕过付费，且部分风控机制未经官方证实。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 全流程仅 7 个选择题需要用户决策，其余由 AI 自动执行
- 提供 Clash/sing-box/Surge 等多引擎分流规则文件
- 附跨平台自检脚本（时区/语言/DNS/出口 IP/延迟）
- 痕迹清理默认 dry-run、删除进废纸篓并设保护清单

## 适用场景

- 被封过后想在虚拟机里重建一套干净的 Claude 使用环境
- 检查现有网络的 DNS/WebRTC/时区指纹是否一致
- 为 Claude 订阅配置地区一致的付款与分流方案

## 场景标签

 · 领域:网络工具/访问环境配置

## 证据(README 行号)

> L3: > **全自动**：你把需求说一次，AI 探测环境、清痕迹、搭节点、配分流、对齐时区、封泄露、建虚拟机、验收、清场，全程只在 7 个必须由人决定的地方问你一次。
> L25: ### 1. 把这段发给你的 AI（Claude Code / Codex / Cursor）
> L139: ## 装进你的 Agent


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 mid · 依据 README sha `05c01d2665ce` · [字段定义](../../DATASET.md)*
