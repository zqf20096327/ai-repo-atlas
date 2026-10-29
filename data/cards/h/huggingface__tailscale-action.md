# huggingface/tailscale-action

⭐ 24 · BSD-3-Clause · 推送 2026-08-28 · [GitHub](https://github.com/huggingface/tailscale-action) · 组织维护

**GitHub Action：让 CI runner 接入 Tailscale 网络并支持 SSH 调试**

Hugging Face 维护的 GitHub Action，基于 tailscale/github-action 修改，用于两类场景：一是让 runner 接入 Tailscale 网络以访问内部共享资源（如镜像仓库）；二是在步骤失败或开启调试模式时自动启动 SSH 服务器，配合 Slack 通知进入 runner 调试工作流。提供 authkey、slackChannel、slackToken、waitForSSH、sshTimeout 等配置项。面向使用 GitHub Actions 的 CI 使用者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSD-3-Clause |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单步接入 Tailscale 网络（authkey 配置）
- 步骤失败或调试模式下自动启动 SSH 服务器
- Slack 通知集成（频道与 Bot Token 配置项）
- sshTimeout 可调整默认 5 分钟的等待时长

## 适用场景

- CI 流水线访问公司内部资源（如私有镜像仓库）
- 工作流失败时 SSH 登录 runner 排查问题
- 调试模式下远程观察 CI 步骤执行过程

## 场景标签

 · 领域:开发运维/CI 工具

## 证据(README 行号)

> L2: Hugging Face Github action to connect to tailscale (Based from https://github.com/tailscale/github-action)
> L4: You can use this github action for 2 differents use cases :

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/tailscale-action 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 low · 依据 README sha `e7eb8fb0dadf` · [字段定义](../../DATASET.md)*
