# fajarhide/contexere

⭐ 375 · Rust · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/fajarhide/contexere) · [官网](https://omni.weekndlabs.com/docs) · 个人维护

**给编程 agent 的上下文/令牌压缩层，降噪减 token 且不丢数据**

Contexere（原 OMNI）是插在编码 agent 工具输出与模型读取之间的上下文处理层：重复读取的文件折叠为一行句柄，构建/测试输出保留结果与失败项、去除进度噪音，输出中的令牌与密码替换为 [REDACTED]；被移除的内容保留在本机，可一条命令找回。README 称每次命令约耗时 21ms，示例中 7.6KB 文件二次读取降为 214B。通过 brew 或安装脚本安装，init 后以 hook 方式接入 Claude Code、Codex、Cursor 等多种 agent。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 重复读文件折叠为单行句柄（示例 7.6KB→214B）
- 构建/测试输出保留结果与失败项、丢弃进度噪音
- 输出中凭证替换为 [REDACTED]，凭 doctor 命令校验 hook 生效
- 被移除内容保留本机可找回，JSON/YAML/CSV 保持原样

## 适用场景

- 降低编码 agent 的 token 消耗与费用
- 防止密码/令牌泄露进模型上下文
- 让 Claude Code、Cursor 等工具读取更干净的命令输出

## 场景标签

 · 领域:开发者工具/LLM 基础设施

## 证据(README 行号)

> L5:  The context and token layer for coding agents. It shrinks noisy tool output, folds what an agent already read, and 
> L25: Contexere takes out what the model does not need, before the model reads it. Nothing is deleted: whatever it remove
> L73: |**Full** (rewrites tool output before the model reads it)|Claude Code, Codex CLI, Gemini CLI, OpenClaw, Hermes, Pi


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `b21a13024f4c` · [字段定义](../../DATASET.md)*
