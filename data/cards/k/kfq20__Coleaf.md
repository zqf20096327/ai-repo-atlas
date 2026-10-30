# kfq20/Coleaf

⭐ 20 · TypeScript · MIT · 推送 2026-05-07 · [GitHub](https://github.com/kfq20/Coleaf) · 个人维护 · 中文 README

**把 Overleaf Git 项目变成多人协作的 AI LaTeX 写作工作台**

本地优先的 Web 应用：连接 Overleaf 的 Git 仓库，浏览器内提供 Monaco 编辑器、文件树、自动保存、经 latexmk 编译的 PDF 预览，以及一个 agent 聊天框——agent 可列文件、读写文件、精确替换、查看 git 状态、创建本地 commit，但不会自动 push，同步回 Overleaf 须由用户点击触发。面向使用 Overleaf 协作写 LaTeX 论文的研究者，每个协作者用自己的模型凭据与 Overleaf token，支持 OpenAI-compatible Responses API。当前为 MVP，凭据明文存储、无内置用户认证，建议本地或可信环境使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- agent 具备 6 个工具（列文件/读写/精确替换/git 状态/本地 commit），限制作在当前 session workspace 内
- 人类控制同步：agent 不 push，用户点击 Sync to Overleaf 才 pull/rebase/push
- 每个协作者使用自己的模型凭据与 Overleaf token
- 后端经 latexmk 编译并在浏览器预览 PDF

## 适用场景

- 多人共写 LaTeX 论文时让 agent 做结构化修改、润色、补引用
- 在本地环境管理 Overleaf 项目的 AI 辅助编辑与 Git 同步
- 控制 agent 改动何时回传 Overleaf，避免自动 push 风险

## 场景标签

`AI 写作` `科研工具` · 领域:内容生成

## 证据(README 行号)

> L5: 把任意 Overleaf Git 项目变成一个 **多人协作的 AI LaTeX 写作工作台**。
> L27: - **Agent 聊天改论文**：agent 可以列文件、读文件、精确替换、写文件、查看 git 状态、创建本地 commit。
> L30: - **自带模型凭据**：支持 OpenAI-compatible Responses API endpoint，不需要平台级全局 API key。

## 星数曲线

```mermaid
xychart-beta
    title "kfq20/Coleaf 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-30 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `1faca78fdfdf` · [字段定义](../../DATASET.md)*
