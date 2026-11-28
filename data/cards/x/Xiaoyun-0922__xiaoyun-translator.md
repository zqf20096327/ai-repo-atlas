# Xiaoyun-0922/xiaoyun-translator

⭐ 10 · JavaScript · GPL-3.0 · 推送 2026-08-07 · [GitHub](https://github.com/Xiaoyun-0922/xiaoyun-translator) · 个人维护 · 中文 README

**面向研究者的 Windows 本地 AI 翻译与论文阅读桌面应用**

基于 Tauri 2（Rust+React）的桌面工作台，整合划词翻译（Ctrl+D）、截图翻译与公式 OCR（Ctrl+E）以及 PDF/Markdown/DOCX/TeX 文献阅读器。翻译、OCR 与论文分析通过本地运行的 Ollama 调用 Gemma 4 多模态模型完成，不需账号或云端 API Key；译文保留 Markdown/LaTeX 格式，阅读器提供全文概要、章节摘要、术语、高亮、笔记与阅读进度管理，数据保存在本机。当前 Release 仅覆盖 Windows 10 22H2+/11 x64，macOS/Linux 仅有未签名、未完成实机验证的 CI 试验产物。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Ctrl+D 全局划词翻译，Ctrl+E 截图翻译与公式 OCR（Gemma 4 多模态）
- AI 论文/书籍阅读器：全文概要、章节摘要、关键术语、笔记与进度管理
- 本地优先：翻译、OCR、分析与朗读均在本机，不需云端 API Key
- 学术语境翻译：结合论文标题、前后文与术语库辅助消歧

## 适用场景

- 长期阅读英文论文和技术文档时随选随译
- 扫描版 PDF 的 OCR 翻译与公式识别
- 按项目、标签和进度管理个人文献库
- 无网络或不便使用云端 API 的环境下完成学术翻译

## 场景标签

`知识库管理` `科研工具` `OCR` · 领域:知识与检索

## 证据(README 行号)

> L5:  把划词翻译、公式 OCR 与本地 AI 文献阅读放进同一个桌面工作台。
> L23: Ollama 是一个**独立安装、在后台运行的本地 AI 程序**。小允翻译负责调用它完成翻译、OCR 和文献分析；两者都在本机运行，**不需要账号或 API Key**。
> L42: - **AI 论文与书籍阅读器**：导入 PDF、Markdown、DOCX 或 TeX；论文生成全文概要，书籍建立目录并按章节生成摘要与关键术语。

## 星数曲线

```mermaid
xychart-beta
    title "Xiaoyun-0922/xiaoyun-translator 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-11-28"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-26 10 → 2026-11-28 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `8a1dd14d3c43` · [字段定义](../../DATASET.md)*
