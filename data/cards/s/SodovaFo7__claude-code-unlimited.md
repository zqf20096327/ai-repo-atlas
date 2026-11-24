# SodovaFo7/claude-code-unlimited

⭐ 3 · C++ · MIT · 推送 2026-11-23 · [GitHub](https://github.com/SodovaFo7/claude-code-unlimited) · 个人维护

**为 Claude Code CLI 自动轮换会话以规避用量限制的封装工具**

面向 64 位 Windows 10/11 的 Claude Code CLI 封装器：监视子进程输出流，实时检测用量上限消息，对当前会话做检查点保存并原地轮换，保留上下文同时获得新配额。参数经 config/settings.json 热加载控制，无外部依赖；提供会话状态存储、stderr 日志通道与 ccu status/rotate 命令。以预编译 zip 发行，也可用 CMake 从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时检测输出流中的上限消息并自动轮换会话
- 检查点-恢复机制，会话上下文保留
- config/settings.json 热加载配置，零外部依赖
- 提供 ccu status / ccu rotate 命令与 [ccu] 日志通道

## 适用场景

- 长时间使用 Claude Code CLI 编码时不中断会话
- 管理多个会话槽位并查看轮换状态
- 按自定义参数（轮换阈值、检查点保留等）控制轮换行为

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L18: **Claude Code Unlimited — Session Rotation Engine for Claude Code CLI** (`claude-code-unlimited`) is a dedicated, l
> L34: |**Session Watcher**|Streams child-process stdout through a bounded ring-buffer limit detector|`rotate_on_limit`, l


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 mid · 依据 README sha `7fce6ed3a8ad` · [字段定义](../../DATASET.md)*
