# leo123-tto/case-board

⭐ 52 · Rust · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/leo123-tto/case-board) · [官网](https://lawtools.top/?utm_source=github&utm_medium=repo&utm_campaign=caseboard) · 个人维护 · 中文 README

**律师个人案件可视化看板：LLM 抽取案件信息并生成分析报告**

面向个人律师和小团队的桌面应用（Tauri 2 + React 19 + Rust），把散落在文件夹里的诉讼材料汇总为案件进展看板，定位为取代 Excel 案件登记表。LLM 通读全案材料，自动填写案号、当事人、关键日期等结构化字段，并生成案件分析报告与类案检索文书，可导出 HTML/Word；执行模块接入元典 API 查被执行人并生成 LLM 风险提示报告。本地优先、源文件只读；但文本抽取/OCR 默认走云端（DeepSeek/MinerU），可选本机模型。本仓库为 0.4.x 源码，0.5 闭源免费软件另行分发；源码以 PolyForm Noncommercial 授权，商业用途需书面授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- LLM 全局抽取结构化 JSON 字段与完整案件分析报告，改字段只需改 prompt
- 元典 14 端点查被执行人 + DeepSeek 生成风险提示报告与深挖建议
- 保全续封/上诉期等关键日期自动到期提醒（颜色分级）
- 源文件只读、数据存本机，抽取/OCR 默认云端可选本机模型

## 适用场景

- 把文件夹里的诉讼材料整理成案件进展看板，不用手填字段
- 查被执行人并自动生成风险提示与财产线索报告
- 跟踪保全到期、上诉期等关键法律期限
- 生成案件分析报告并导出 Word 交付

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L20: - **关键信息 LLM 自动抽取** —— 用户不用手填字段
> L21: - **本地优先** —— 源文件只读不动;关键信息抽取 / OCR 默认走云端(DeepSeek / MinerU),可选配本机模型

## 星数曲线

```mermaid
xychart-beta
    title "leo123-tto/case-board 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-25"]
    y-axis "stars" 51 --> 53
    line [52, 52]
```

2026-10-22 52 → 2026-10-25 52（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `67621bacb40e` · [字段定义](../../DATASET.md)*
