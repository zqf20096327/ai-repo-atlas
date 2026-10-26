# sodam-ai/SoDam-WikiMate

⭐ 49 · JavaScript · Apache-2.0 · 推送 2026-09-11 · [GitHub](https://github.com/sodam-ai/SoDam-WikiMate) · 组织维护 · 中文 README

**把散落资料整理成 Obsidian 笔记的 Claude Code 插件+MCP 核心**

面向 Windows 个人用户的 Claude Code 插件与可移植 MCP 服务器（v0.10.0，8 个 MCP 工具）：通过自然语言指令让 AI 把网页、PDF、对话日志等整理为 Obsidian 笔记，并做自动链接、MOC 目次、分类、一行摘要与原子笔记，可选同步 Notion 索引；另含只读查询（出处核验）、仓库健康检查（重复/断链/孤儿，归档而非删除）与任务日志。执行遵循分析→计划→人工批准→执行→复核→记录流程，含 prompt 注入防御与 source_hash 去重。Codex/Gemini CLI 以 MCP 方式接入但部分功能未验证。需 Node.js 18+，无独立运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 8 个 MCP 工具：collect/lint/fix/runlog/vaults/link/classify/summarize
- 写操作前强制 dry-run 计划与人工批准，原文本体不被修改
- 仓库健康检查采用归档（99_Archive）与自动备份，不做删除
- prompt 注入防御与 source_hash 去重

## 适用场景

- 用一句话把链接、PDF 等资料整理进 Obsidian 笔记库
- 自动给相关笔记建立链接并生成 MOC 目次笔记
- 检查笔记库的重复、断链与孤儿笔记并安全清理
- 在 Notion 生成整理结果的索引列表

## 场景标签

`知识库管理` · 领域:知识与检索

## 证据(README 行号)

> L3: AI 에이전트에게 **"정리해줘"** 라고 말하면, 흩어진 자료(웹 링크·PDF·대화 로그·텍스트)를 **내 옵시디언 볼트에 노트로 정리**하고, 관련 있는 노트끼리 **연결**하고, **분류**하고, **요
> L63: |**MCP**|AI와 도구를 이어 주는 **표준 통로(콘센트)**. Wikimate는 이 통로를 통해 일해요.|
> L161: codex mcp add wikimate --env OBSIDIAN_VAULT_PATH=D:/내/볼트/경로 -- node D:/받은/경로/SoDam-WikiMate/mcp/server.mjs

## 星数曲线

```mermaid
xychart-beta
    title "sodam-ai/SoDam-WikiMate 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-26"]
    y-axis "stars" 48 --> 51
    line [50, 49, 49]
```

2026-10-18 50 → 2026-10-26 49（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `0ffed2c7c9c5` · [字段定义](../../DATASET.md)*
