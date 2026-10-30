# fokdelafons/lustra

⭐ 27 · Dart · AGPL-3.0 · 推送 2026-06-03 · [GitHub](https://github.com/fokdelafons/lustra) · [官网](https://lustra.news/) · 组织维护

**面向公民的立法追踪与直接民主平台，AI 生成中立法案摘要**

Flutter 移动端与 Web 单仓库应用，后端基于 Firebase 与 Google Cloud Run，AI 引擎为 Vertex AI（Gemini Flash）。功能：解析政府原始数据（PDF/XML），用 temperature=0 的 LLM 与严格 JSON 提示词生成去除情绪化语言的中立摘要并链接原始出处；支持公民对法案投票与起草公民立法。核心逻辑与数据源解耦，新国家接入只需编写 Data Adapter；系统提示词在应用内公开。需自行搭建 Firebase 项目并配置 Flutter 环境运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- temperature=0 与严格 JSON 提示词生成中性化法案摘要，并链接原始 PDF/XML 出处
- 公民投票与公民立法起草功能
- 国家数据通过 Data Adapter 接入，核心逻辑与数据源解耦
- 系统提示词在应用内公开（Radical Transparency）

## 适用场景

- 以中立摘要跟踪本国立法动态并查看原始文本
- 公民对法案投票、起草公民立法
- 为本国接入 Lustra 平台编写数据适配器

## 场景标签

 · 领域:政务/公民科技

## 证据(README 行号)

> L7: **Lustra** is a digital public infrastructure designed to track legislation and empower civic oversight. It parses r
> L14: 2. **Context Sterilization:** Using LLMs with temperature=0 and strict JSON prompts to strip emotional language.
> L21: * **AI Engine:** Vertex AI (Gemini Flash) via strictly typed API calls.

## 星数曲线

```mermaid
xychart-beta
    title "fokdelafons/lustra 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `0d3d3183c0f7` · [字段定义](../../DATASET.md)*
