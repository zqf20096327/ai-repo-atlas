# izzzzzi/agent-assh

⭐ 21 · Go · MIT · 推送 2026-08-10 · [GitHub](https://github.com/izzzzzi/agent-assh) · 个人维护 · 中文 README

**为 LLM agent 准备的 SSH 工作流工具，节省上下文**

面向 LLM agent（Claude Code、Codex、Cursor 等）的 SSH 命令行工具：一条 connect 命令完成密钥引导、tmux 安装与持久会话建立；命令先返回紧凑 JSON 元数据，agent 再按需分页读取输出行，避免大输出进入上下文。提供会话执行/读取、文件传输、端口转发、多主机并行执行、主机清单扫描与后台任务等命令。安全方面：密码仅经环境变量、输出默认脱敏、destructive 命令默认拦截、安全规则文件 fail-closed。依赖系统 OpenSSH 客户端，tmux 会话面向 Unix-like 远端主机；交互式密码提示在 v1 不支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- connect 一步完成密钥引导、tmux 安装与持久会话建立
- 分页读取输出，audit --savings 统计被扣留的行数
- 输出默认脱敏（AWS/JWT/bearer/PEM 等）与 destructive 命令拦截
- 多 agent 技能安装（Claude Code/Codex/Cursor/Cline/Copilot CLI/OpenCode/Pi/AGENTS.md）

## 适用场景

- 让编程 agent 通过受控通道执行远程服务器运维任务
- 在 agent 上下文中只读取需要的输出片段以节省 token
- 跨多台主机并行执行命令与传输文件

## 场景标签

 · 领域:开发运维工具/agent 基础设施

## 证据(README 行号)

> L10: SSH-инструмент для LLM-агентов.
> L56: ## Установка скилла assh в AI-агентов
> L136: Вставьте эту инструкцию в Codex, Claude Code, OpenCode или другой terminal agent перед передачей SSH-данных:

## 星数曲线

```mermaid
xychart-beta
    title "izzzzzi/agent-assh 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `20451088454a` · [字段定义](../../DATASET.md)*
