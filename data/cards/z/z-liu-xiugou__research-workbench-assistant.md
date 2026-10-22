# z-liu-xiugou/research-workbench-assistant

⭐ 205 · Python · Apache-2.0 · 推送 2026-10-09 · [GitHub](https://github.com/z-liu-xiugou/research-workbench-assistant) · 个人维护 · 中文 README

**面向研究生的本地科研记录助手（Codex Skill）**

以 Codex Skill 形式安装的本地科研工作台：初始化独立目录，跨对话保存续接断点，由 Codex 在新对话中读取；提供进展/任务/决策/问题/文献等台账、修订留痕、Markdown+JSON 文献笔记、本地关键词检索、Crossref 在线文献发现与候选队列，可生成离线 HTML 研究总览，另有 backup/restore 与只读诊断命令。脚本无第三方 Python 依赖，除 Crossref 查询外不联网。当前为 v0.1.0-alpha.9 预览版，不支持 PDF 解析、Zotero 同步、多人协作等。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 跨对话续接断点：新对话按需读取本地保存的科研进度
- Crossref 在线文献发现（DOI 去重、来源留痕）与候选文献队列
- 修订留痕：追加新记录并标记替代关系，旧版本保留
- 离线 HTML 研究总览快照，无外部资源请求

## 适用场景

- 科研项目中记录目标、进展、问题和下一步，新对话续接
- 检索 Crossref 文献并维护候选/保留/排除队列与阅读笔记
- 生成离线总览页面集中查看断点、任务与笔记

## 场景标签

 · 领域:科研工具/知识管理

## 证据(README 行号)

> L9: 面向研究生的本地科研记录助手，以 Codex Skill 形式使用：记录目标、进展、问题和下一步，在新对话中按需续接；文献笔记保存为 Markdown 和 JSON。
> L56: |跨对话续接|保存本地断点，由 Codex 在新任务中读取；不是云端聊天记忆|
> L21: 需要：可用的本地 Codex、Python 3.10+、Git。脚本无第三方 Python 依赖，无需另填 API Key；Codex 本身仍需可用账户，可能产生使用费用。

## 星数曲线

```mermaid
xychart-beta
    title "z-liu-xiugou/research-workbench-assistant 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 204 --> 206
    line [205, 205]
```

2026-10-18 205 → 2026-10-22 205（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9e336f6565be` · [字段定义](../../DATASET.md)*
