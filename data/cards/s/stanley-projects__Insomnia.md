# stanley-projects/Insomnia

⭐ 10 · JavaScript · MIT · 推送 2026-09-07 · [GitHub](https://github.com/stanley-projects/Insomnia) · [官网](https://stanley-projects.github.io/Insomnia/) · 组织维护

**给 AI 编程用户的 Windows 防休眠工具：工作即唤醒**

面向 Windows 10/11 的免费开源防休眠工具，基于 Electron 的 powerSaveBlocker API 实现。通过三类信号决定是否阻止休眠：手动开关、进程监控（每 10 秒轮询 tasklist）、Hook 会话（Claude Code 等 AI 编码工具活跃时保持唤醒，空闲后释放）。首次启动自动检测已安装的 AI 编码工具并配置钩子，运行时无需安装 Node.js。仅支持 Windows，不支持 macOS/Linux。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对 Claude Code / Cursor / Codex 采用 Hook 式监控，区分“活跃工作”与“闲置打开”
- 支持按进程监控任意应用（开始菜单/注册表/商店应用自动发现）
- 系统托盘常驻，悬停显示当前保持唤醒的原因
- 首次启动自动检测并配置 AI 工具集成，无需 Node.js

## 适用场景

- AI 编码工具跑长任务时防止电脑休眠中断进程
- 本地跑 Ollama 大模型推理时保持唤醒
- 视频渲染、编译、演示等场景手动或按应用保持唤醒

## 场景标签

 · 领域:系统工具/开发者工具

## 证据(README 行号)

> L3: > **Insomnia is the smart Windows sleep-prevention utility that automatically keeps your PC awake while AI coding to
> L7: Insomnia is a free, lightweight Windows app that keeps your computer awake — automatically when AI coding agents are
> L99: Insomnia uses Electron's `powerSaveBlocker` API to prevent Windows from entering sleep mode. It evaluates whether t
> L151: - **Electron** — Cross-platform desktop framework (Windows support)


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `ca4e1e705f23` · [字段定义](../../DATASET.md)*
