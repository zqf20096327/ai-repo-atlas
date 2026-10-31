# KyuDan1/Talk-to-Your-Slides

⭐ 34 · Jupyter Notebook · 推送 2026-07-06 · [GitHub](https://github.com/KyuDan1/Talk-to-Your-Slides) · 组织维护

**LLM agent 通过对话直接编辑 PowerPoint 幻灯片，附基准数据集**

ACL 2026 Findings 论文配套系统：LLM 驱动的 agent 通过 COM/python-pptx 读取活动 PowerPoint 会话中的对象级结构信息，按用户自然语言指令执行幻灯片编辑，采用 Planner/Parser/Processor/Aplier/Reporter 五段分层流水线，将高层语义规划与底层对象操作分离，无需视觉像素交互。支持 OpenAI GPT-4.1 系列、Gemini、Claude 3.7 Sonnet，提供 Flask Web UI 与 CLI 两种运行方式，需 Windows 上启用 VBA 访问。另发布人工标注的 TSBench/TSBench-Hard 评测数据集（379/300 条指令）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 分层编辑设计：高层语义规划与底层对象操作分离
- 通过 COM 接口操作活动 PowerPoint 会话，绕过视觉像素交互
- 五段模块化流水线（Planner/Parser/Processor/Aplier/Reporter）
- 附带 TSBench 与 TSBench-Hard 人工标注评测数据集

## 适用场景

- 用自然语言指令批量修改幻灯片文本与格式
- 翻译幻灯片内容、修正拼写错误、生成演讲备注
- 用 TSBench 数据集评测幻灯片编辑 agent 的表现

## 场景标签

`模型评测` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L20: While GUI-based agents have demonstrated visual control capabilities, they often suffer from high computational cos
> L167: ### 🎯 Supported Models

## 星数曲线

```mermaid
xychart-beta
    title "KyuDan1/Talk-to-Your-Slides 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 33 --> 35
    line [34, 34]
```

2026-10-18 34 → 2026-10-31 34（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `16bb12628c96` · [字段定义](../../DATASET.md)*
