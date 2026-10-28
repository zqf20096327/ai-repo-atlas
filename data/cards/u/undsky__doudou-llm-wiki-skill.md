# undsky/doudou-llm-wiki-skill

⭐ 33 · Python · NOASSERTION · 推送 2026-09-17 · [GitHub](https://github.com/undsky/doudou-llm-wiki-skill) · [官网](https://www.undsky.com) · 个人维护 · 中文 README

**LLM 驱动的个人知识库技能：整理素材并回答问题**

面向个人知识管理的 AI 技能包，运行于 doudou-ai-coding 及 Antigravity、Claude Code、OpenCode 等平台。LLM 负责素材摘要、实体/概念页拆分、交叉引用与一致性维护。素材不限文本：音视频、Office 文档、PDF、扫描件、图片分别交给 doudou-stt/doc/ocr 技能预处理成文本再入库。四层架构中 LLM 只读中间产物（gen/）构建 wiki，不读 raw/ 原件；知识库用 Obsidian（或 VS Code Foam）浏览。通过 /doudou-wiki 系列命令或自然语言触发 init/add/query 等操作。许可为 CC BY-NC 4.0，商业用途需单独授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持音视频/Office/PDF/扫描件/图片素材，经配套技能文本化后入库
- 四层架构：LLM 只读 gen/ 中间产物构建 wiki，不写 raw/ 原件
- scripts/scan.py 按扩展名确定性判定素材分派路线
- 知识库可用 Obsidian 或 VS Code Foam 浏览图谱与反链

## 适用场景

- 把访谈录音、扫描件、Office 文档统一整理成个人 wiki
- 基于自有知识库用自然语言提问获得回答
- 在 Claude Code 等编码平台中以项目级知识库管理素材

## 场景标签

`知识库管理` `文档问答` · 领域:知识与检索

## 证据(README 行号)

> L5:  LLM 驱动的个人知识库。LLM 负责所有繁重的整理 —— 摘要、交叉引用、归档、一致性维护；
> L25: 本项目为 https://github.com/undsky/doudou-ai-coding 提供项目级的知识库支持（支持 Antigravity、Claude Code、OpenCode 等平台）。
> L65: LLM 会自动分派转换、阅读素材、建摘要页、拆实体和概念页、维护交叉引用。

## 星数曲线

```mermaid
xychart-beta
    title "undsky/doudou-llm-wiki-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-28 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `42b3d7fa1aa1` · [字段定义](../../DATASET.md)*
