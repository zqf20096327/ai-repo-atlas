# gexijin/RTutor

⭐ 322 · HTML · NOASSERTION · 推送 2026-10-28 · [GitHub](https://github.com/gexijin/RTutor) · [官网](https://RTutor.ai) · 个人维护

**用自然语言对话分析数据的 R/Shiny 应用，自动生成并执行 R 代码**

基于 R 与 Shiny 的数据分析应用：用户上传数据后以自然语言提问，RTutor 通过 OpenAI ChatGPT 等 API 将问题翻译为 R 脚本并执行，返回结果，可生成 R Markdown 源文件与 HTML 报告。面向会写或不写代码的数据分析使用者，需自备 OpenAI API key（设置页、api_key.txt 文件或环境变量三种配置方式），仓库更新频繁，建议每次使用前重装。许可为 CC BY-NC 3.0，仅限非商业使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自然语言转 R 脚本并在 Shiny 内执行
- 可生成 R Markdown 源文件与 HTML 报告
- API key 支持设置页/文本文件/环境变量三种配置

## 适用场景

- 上传数据后用自然语言提问完成统计分析
- 把分析过程导出为 R Markdown 报告
- 不熟悉 R 编程时快速获得可运行的分析代码

## 场景标签

`数据分析` · 领域:效率与自动化

## 证据(README 行号)

> L7: RTutor is an AI-based app that can quickly generate and test R code. Powered by API calls to OpenAI's ChatGPT or oth
> L5: No code? No problem. Analyze data with simple, natural language. Upload your data, ask questions, and get results in

## 星数曲线

```mermaid
xychart-beta
    title "gexijin/RTutor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 321 --> 323
    line [322, 322]
```

2026-10-18 322 → 2026-10-28 322（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `3a13b1be6d3f` · [字段定义](../../DATASET.md)*
