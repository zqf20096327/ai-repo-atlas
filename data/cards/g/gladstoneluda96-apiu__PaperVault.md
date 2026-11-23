# gladstoneluda96-apiu/PaperVault

⭐ 3 · Rust · 推送 2026-11-16 · [GitHub](https://github.com/gladstoneluda96-apiu/PaperVault) · 个人维护 · 中文 README

**本地优先学术论文管理台：PDF 解析、AI 摘要与翻译**

基于 Tauri 2 的本地优先论文管理应用：导入 PDF 或通过 arXiv/Semantic Scholar 获取后，将论文转为结构化 Markdown，生成中文摘要、问答、术语表与全文翻译；使用 SQLite FTS5 做本地全文搜索，并跟踪论文间双向引用关系。原文、数据库与分析结果默认保存在本地，LLM/DeepL 的 API Key 仅存于设备本地存储。目前处于早期开发阶段，安装包与跨平台适配仍在完善。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- PDF 转结构化 Markdown 并生成中文摘要、问答与术语表
- 英文论文全文翻译，可配置 LLM 或 DeepL
- SQLite FTS5 本地全文搜索与双向引用关系追踪
- 原文、数据库与分析结果默认保存在本地

## 适用场景

- 按项目、标签整理个人论文阅读材料
- 阅读英文论文时获取中文摘要与全文翻译
- 通过引用关系图梳理论文脉络

## 场景标签

`文档解析` `文档问答` `科研工具` · 领域:知识与检索

## 证据(README 行号)

> L3: PaperVault 是一款本地优先的学术论文管理工作台。导入 PDF 后，它会将论文转换为结构化 Markdown，并生成中文摘要、问答、术语表与全文翻译，帮助研究者按项目、标签和引用关系整理阅读材料。
> L22: - 英文论文全文翻译，优先使用所配置的 LLM 或 DeepL

## 星数曲线

```mermaid
xychart-beta
    title "gladstoneluda96-apiu/PaperVault 星数(近 2 点)"
    x-axis ["2026-11-16", "2026-11-23"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-16 3 → 2026-11-23 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `853f4ed60d38` · [字段定义](../../DATASET.md)*
