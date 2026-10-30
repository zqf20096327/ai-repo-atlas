# HeZeBang/keybearer

⭐ 16 · Rust · 推送 2026-06-12 · [GitHub](https://github.com/HeZeBang/keybearer) · 个人维护 · 中文 README

**SSH 凭据转发工具：LLM API Key 留本地，远端安全使用**

基于 Rust 的 credential 转发工具：API Key 存储在本地宿主机 config.yaml，本地 agent 通过 SSH agent forwarding 把凭据查询传递到远端，远端 keybearer run 用 seccomp 拦截 open/openat 系统调用，按需向 Codex、OpenCode、Claude Code 的配置文件注入 key（匿名 memfd，不落盘、不进入 shell 历史）。支持多 profile 按主机选择、合并注入保留用户自定义配置，配置文件 0600 权限并附 JSON Schema 校验。需自行 cargo 编译并上传二进制。README 声明 root 仍可观察进程，边界需在威胁模型中验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- API Key 仅存本地，通过 SSH agent forwarding 按需传递
- seccomp 拦截 open/openat，向 Codex/OpenCode/Claude Code 配置注入 key
- 无持久化：远端仅运行时匿名 memfd，断联即焚
- 多 profile 按主机绑定（KEYBEARER_PROFILE_ID），合并模式保留用户自定义配置

## 适用场景

- 在公共服务器/共享集群上运行 LLM CLI 而不把 API Key 写到远端磁盘
- 不同主机使用不同 provider（如公司集群用 OpenAI、个人服务器用 DeepSeek）
- 本地统一轮换 Key，多台远程主机立即生效

## 场景标签

 · 领域:开发工具/安全基础设施

## 证据(README 行号)

> L9: Keybearer 基于 SSH Agent Forwarding 的协议通道，通过 Seccomp hook 读取，实现安全的 API Key 传输通道。
> L23: 7. 运行 LLM CLI：`/tmp/keybearer run codex` / `opencode` / `claude`
> L118: `keybearer run` 会拦截以下文件的 `open`/`openat` 系统调用，注入 key 和配置：

## 星数曲线

```mermaid
xychart-beta
    title "HeZeBang/keybearer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e119bea9112c` · [字段定义](../../DATASET.md)*
