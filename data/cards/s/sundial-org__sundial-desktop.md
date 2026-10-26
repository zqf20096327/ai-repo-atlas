# sundial-org/sundial-desktop

⭐ 33 · TypeScript · Apache-2.0 · 推送 2026-09-03 · [GitHub](https://github.com/sundial-org/sundial-desktop) · 组织维护

**人与 AI 共写的实时多人 Markdown 编辑器**

基于 Tauri 的桌面 Markdown 编辑器，团队与 Claude Code / Codex agent 在同一文档内实时协作：文档为 Yjs CRDT，本地 sidecar 监视文件夹并驱动用户自有订阅上的 agent 引擎，agent 编辑以建议形式落文并可逐条接受/拒绝，每次修改附署名并链接到对应聊天轮次。默认本地优先，仅分享文档时经云端同步。macOS 提供下载安装，Windows/Linux 未提供构建，浏览器版在 sundial.md 运行。源码构建需 Node ≥ 23、pnpm 10 与 Rust 工具链。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CRDT（Yjs）实现人与 agent 无冲突共编，逐键署名
- agent 编辑以行级建议形式落地，可逐条接受/拒绝并回溯历史
- 驱动本机 Claude Code / Codex，复用已有订阅，无需 API key
- 纯 Markdown 磁盘文件，Obsidian 仓库可直接打开

## 适用场景

- 与队友和 AI 在同一文档实时协作撰写文档
- 让 agent 改写文稿后逐条审阅其修改
- 离线（飞机上）编辑、评论与查看历史
- 把 Obsidian 笔记库直接打开并按需分享单篇笔记

## 场景标签

`知识库管理` `AI 写作` · 领域:内容生成

## 证据(README 行号)

> L7: A Markdown editor where your team and your agents write in the same document, live. Claude Code and Codex join your 
> L37: - **Your subscription works here.** Claude Code and Codex run on your machine, inside the editor. No API key, no ac
> L41: - **Any model.** Local engines run on your subscriptions; signed in, swap between frontier and open models mid-conv

## 星数曲线

```mermaid
xychart-beta
    title "sundial-org/sundial-desktop 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-26"]
    y-axis "stars" 31 --> 34
    line [32, 33, 33]
```

2026-10-18 32 → 2026-10-26 33（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `16b1da62b126` · [字段定义](../../DATASET.md)*
