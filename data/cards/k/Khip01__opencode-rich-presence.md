# Khip01/opencode-rich-presence

⭐ 10 · JavaScript · MIT · 推送 2026-11-16 · [GitHub](https://github.com/Khip01/opencode-rich-presence) · 个人维护

**给 OpenCode 用户的 Discord Rich Presence 插件**

面向 OpenCode CLI 用户的 Discord Rich Presence 插件：将当前 AI 会话状态实时展示到 Discord 个人资料，内容包括模型名称、活动状态、上下文用量、花费与已用时长。支持 OpenCode v1/v2，跨 Linux/macOS/Windows，提供模板自定义、自动清除逻辑与内置活动日志。需 Node.js 18+、OpenCode CLI 与 Discord Desktop，通过安装脚本或 npm tarball 安装，带 CLI 管理命令。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时展示 OpenCode 会话的模型、活动、上下文用量与花费
- 支持 OpenCode v1 与 v2，自动检测版本并链接插件入口
- 可自定义 presence 模板，支持条件与变量替换
- 提供 install/update/info 等 CLI 命令与活动日志

## 适用场景

- 编码时让 Discord 好友看到我正在用的 AI 模型与会话状态
- 跟踪当前 AI 会话的上下文用量和花费
- 在多个 OpenCode 窗口间切换时保持状态显示稳定

## 场景标签

 · 领域:开发者工具/状态展示插件

## 证据(README 行号)

> L9: OpenCode Rich Presence gives your Discord profile a live view of what
> L30: - OpenCode CLI, v1 or v2


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `e7d5ec59e673` · [字段定义](../../DATASET.md)*
