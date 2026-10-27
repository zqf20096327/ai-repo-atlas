# memvid/design-memory

⭐ 131 · TypeScript · 推送 2026-02-15 · [GitHub](https://github.com/memvid/design-memory) · [官网](https://memvid.com) · 个人维护

**从网站提取设计系统并生成可复用设计记忆的 CLI 工具**

面向前端/设计工程开发者的命令行工具：用 Playwright 抓取网站，确定性提取颜色、字体、间距等设计要素，再由 LLM 做语义标注与设计原则提取，最终生成 .design-memory/ 文件夹内的 AI 优化 markdown 文件。全局 npm 安装，需另行安装 Playwright chromium；learn 命令需要 OPENAI_API_KEY 或 --api-key 参数。采用 Acquire/Analyze/Interpret/Project 四阶段流水线架构，代码文件限制在 60 行以内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Playwright 网页抓取与设计要素确定性提取
- LLM 语义标注与设计原则提取
- 生成 .design-memory/ 文件夹的 AI 优化 markdown 输出
- Acquire/Analyze/Interpret/Project 四阶段流水线

## 适用场景

- 从喜欢的网站提取设计系统供参考复用
- 为 AI 编码工具沉淀项目的设计规范与设计 token
- 分析网站的配色、字体、间距体系

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L3: Extract and interpret design systems from websites using deterministic analysis and LLM interpretation.
> L45: - **Interpret**: LLM-based semantic labeling and doctrine extraction

## 星数曲线

```mermaid
xychart-beta
    title "memvid/design-memory 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-27"]
    y-axis "stars" 130 --> 133
    line [131, 132, 131]
```

2026-10-18 131 → 2026-10-27 131（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `30f79868d81e` · [字段定义](../../DATASET.md)*
