# talirezun/the-curator

⭐ 100 · JavaScript · NOASSERTION · 推送 2026-10-11 · [GitHub](https://github.com/talirezun/the-curator) · 个人维护

**把阅读资料整合为可共享的 markdown 知识库，并作为 agent 记忆**

本地优先的知识管理应用：导入 PDF/Markdown/文本后将其整理成互相链接的个人 wiki（新来源更新既有页面而非复制），支持自然语言提问并给出指向来源页面的回答；以纯 markdown 存储于用户自己的 GitHub 私有仓库，可在 Obsidian 中阅读。可选开启团队共建的 Shared Brain，并通过 MCP 桥与 `my-curator` 命令行向任意 agent 提供项目上下文、工作状态与基础文档，使工作可跨会话、跨模型、跨机器延续。Mac 提供 .dmg，Windows/Linux 手动部署，需 Node.js 18+。MCP 桥为 stdio 子进程，浏览器型助手不在范围内；agent 保存为建议性而非强制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 导入文档生成互相链接的 wiki，新来源增量更新既有页面
- 项目记忆（工作状态+基础文档）经单一 MCP 调用交给 agent，跨会话/模型/机器延续
- `my-curator` CLI：context/save/doctor/install-hooks，无需网络与凭证
- working-state 格式公开（docs/spec/working-state-v1.md），第三方工具可读写

## 适用场景

- 把长期阅读的资料沉淀为可提问的个人知识库
- 团队以 Shared Brain 共同维护同一 wiki
- 让编码 agent 在会话开始时恢复上次的进度与项目文档

## 场景标签

`Agent 记忆` `知识库管理` `文档问答` · 领域:Agent 开发

## 证据(README 行号)

> L35: **The Curator is the context engine.** It builds and keeps the context your work runs on — what you
> L43: the more you feed it, and you can ask it questions in ordinary language and get answers that point
> L95: local MCP client — an AI assistant allowed to launch a small helper program on your machine, like

## 星数曲线

```mermaid
xychart-beta
    title "talirezun/the-curator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 99 --> 101
    line [100, 100]
```

2026-10-18 100 → 2026-10-26 100（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `d0b0e802cf39` · [字段定义](../../DATASET.md)*
