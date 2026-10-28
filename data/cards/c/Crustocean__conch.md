# Crustocean/conch

⭐ 34 · JavaScript · 推送 2026-03-05 · [GitHub](https://github.com/Crustocean/conch) · [官网](https://crustocean.chat/profile/conch) · 组织维护

**运行于 Crustocean 聊天的云端编码 agent：读仓库、写补丁、开 PR**

Conch 是基于 Claude 工具调用的云端编码 agent，通过 WebSocket 接入 Crustocean 平台，在聊天中 @提及即可下达编码任务：读取与搜索 GitHub 仓库文件、生成补丁、创建/合并 PR、清理分支。写入先缓存在内存中，经权限门控确认后才通过 Git Data API 提交。面向 Crustocean 用户和自托管开发者，需 Node.js >= 18、Anthropic API key 与 GitHub token；依赖私有包 @crustocean/sdk（需 npm link 或私有 registry）。支持 Docker、Railway 或任意 Node.js 主机部署，无状态、无数据库。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | — |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Claude 流式工具调用循环驱动读文件/搜索/写补丁/开 PR 全流程
- PR 创建、合并、删分支需用户在 UI 中权限门控确认
- 写入先在内存暂存，经 Git Data API 原子提交
- 无状态 worker，支持 Docker/Railway/任意 Node.js 主机部署

## 适用场景

- 在 Crustocean 聊天里让 agent 修 bug、加校验、重构代码并开 PR
- 为团队提供带权限审批的自动化 PR 工作流
- 通过 demo 模式无仓库体验完整 agent 流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L10: A cloud coding agent powered by Claude that reads repos, writes patches, and opens PRs — all steered from Crustocea
> L14: Conch connects to a GitHub repository and uses Claude's tool calling to:

## 星数曲线

```mermaid
xychart-beta
    title "Crustocean/conch 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-28 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `19edb71a21bb` · [字段定义](../../DATASET.md)*
