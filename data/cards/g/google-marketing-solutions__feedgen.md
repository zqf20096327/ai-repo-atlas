# google-marketing-solutions/feedgen

⭐ 268 · TypeScript · Apache-2.0 · 推送 2026-04-07 · [GitHub](https://github.com/google-marketing-solutions/feedgen) · 组织维护

**用 Vertex AI LLM 优化 Google Shopping 商品流的工具**

基于 Google Apps Script、以 Google Sheets 侧边栏形式运行的开源工具，面向使用 Google Merchant Center 的商家和广告主：调用 Vertex AI 的 Gemini/PaLM 基础模型，以零样本或少样本提示生成更优商品标题、更完整描述并补齐缺失属性，随后由模型自评打分供人工批量审批，结果可作为 Merchant Center 补充流导入。支持读取商品落地页文本与图片理解（限视觉模型），默认优先使用输入流已有属性值以降低幻觉。README 声明适用于最多约 3 万条商品，更大规模建议用 Product Studio API 或 BigQuery。开始方式为复制 Sheets 模板并按工作表指引初始化。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- LLM 生成/优化商品标题、描述并补齐缺失属性
- 少样本提示与 Vertex AI 模型微调路径（Gemini/PaLM 系列）
- 生成内容带模型自评分数，支持 Sheets 内批量审批
- 可读取商品落地页内容与图片信息辅助生成

## 适用场景

- 我想批量修复 Merchant Center 商品流的质量问题
- 用 LLM 为商品生成更完整的标题和描述
- 审批后再导入 Merchant Center 作为补充流

## 场景标签

`AI 写作` · 领域:内容生成

## 证据(README 行号)

> L47: **FeedGen** is an open-source tool that uses Google Cloud's state-of-the-art
> L53: The tool relies on GCP's Vertex AI API to provide both zero-shot and few-shot

## 星数曲线

```mermaid
xychart-beta
    title "google-marketing-solutions/feedgen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 267 --> 269
    line [268, 268]
```

2026-10-18 268 → 2026-10-27 268（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `ce6ba4d69e7b` · [字段定义](../../DATASET.md)*
