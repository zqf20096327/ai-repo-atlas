# simpx/loopat

⭐ 83 · TypeScript · Apache-2.0 · 推送 2026-06-10 · [GitHub](https://github.com/simpx/loopat) · 个人维护

**自托管 AI 工作区：围绕上下文管理单人/团队协作的 agent 平台**

基于 Claude Agent SDK 的自托管 Web AI 工作区，核心围绕三个概念组织：Loop（推进任务）、Focus（注意力）、Context（上下文熵减）。团队聊天、代码编辑、agent 决策与记忆统一在同一上下文图，聊天线程可作为 loop 的一等上下文来源。每个 loop 在独立沙箱（默认 bubblewrap）中运行，使用版本化工具链与独立凭据库；知识/笔记通过 git 仓库在成员间同步。产物存于用户自控的 git 仓库，自带 API key。运行需 Node 启动，终端/聊天沙箱需 Linux + podman，macOS/Windows 经 Docker 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 团队聊天线程直接作为 loop 上下文来源
- 每 loop 独立沙箱（bwrap）+ 版本化工具链 + 凭据 vault
- 知识/notes 共享 git 仓库在团队成员间同步，观察经蒸馏管道上浮
- 自托管，产物存于自控 git 仓库，密钥 git-crypt 加密

## 适用场景

- 个人作为本地 AI 工作区跑 coding agent
- 小团队共享知识与上下文协作开发
- 需要可复现沙箱环境的 agent 会话管理

## 场景标签

`编码 Agent` `知识库管理` · 领域:编码与开发

## 证据(README 行号)

> L31: The agent itself is the [Claude Agent SDK][sdk]; what makes loopat
> L38: - **End-to-end context management.** Team chat (IM) threads, code

## 星数曲线

```mermaid
xychart-beta
    title "simpx/loopat 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 82 --> 84
    line [83, 83]
```

2026-10-18 83 → 2026-10-25 83（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1019a5b65ff2` · [字段定义](../../DATASET.md)*
