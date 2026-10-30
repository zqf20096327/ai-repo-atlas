# spences10/nopeek

⭐ 20 · TypeScript · MIT · 推送 2026-10-29 · [GitHub](https://github.com/spences10/nopeek) · 个人维护

**降低 LLM 编码会话中密钥意外泄露的 CLI 工具**

面向使用 LLM 编码 agent 的开发者的命令行工具。通过本地解析 .env/.tfvars/.tfvars.json 文件，用 `run` 将选定密钥仅注入单个子进程环境，或用 `load` 以 source_file/name_only/export 三种方式报告密钥名与加载状态而非值；另提供 set/list/remove 存取全局明文配置与 init 云 CLI 认证审计。采用 fail-closed 严格语法解析，检测到 agent 会话时拒绝 --allow-values/--value。限制：不做输出脱敏、环境沙箱，--persist 为全局明文存储。

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

- `run` 将选定密钥注入单个子进程及其后代，状态输出只报密钥名不报值
- 严格 fail-closed 语法解析 .env/.tfvars/.tfvars.json，畸形文件整体拒绝
- 检测到 LLM agent 会话时拒绝 --allow-values 与 --value，防止值进入对话
- 存储于 ~/.config/nopeek/config.json（0600 文件、0700 目录），含符号链接与所有权校验

## 适用场景

- 让编码 agent 在需要密钥时用 npx nopeek run 执行命令，避免把密钥粘贴进提示词
- 在 agent 会话中按密钥名单选加载 .env 变量
- 审计 AWS/hcloud/gcloud/Azure CLI 的认证是否需要迁移到更安全的配置方式

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L6: CLI for reducing accidental secret disclosure in LLM coding sessions.
> L27: Shell output visible to an LLM coding agent may be sent to a model

## 星数曲线

```mermaid
xychart-beta
    title "spences10/nopeek 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `9c55bb289d94` · [字段定义](../../DATASET.md)*
