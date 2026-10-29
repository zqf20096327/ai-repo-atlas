# InternLM/VSR

⭐ 35 · Python · Apache-2.0 · 推送 2026-06-28 · [GitHub](https://github.com/InternLM/VSR) · 组织维护 · 中文 README

**ICLR 2026 论文官方代码：像素引导反馈的图表解析方法**

ICLR 2026 论文 "Visual Self-Refine: A Pixel-Guided Paradigm for Accurate Chart Parsing" 的官方仓库，作者来自香港中文大学与上海人工智能实验室。方法将图表解析转为像素引导的反馈回路：预测锚点、渲染、检查渲染图表并基于验证的像素修正最终解析结果。仓库提供图表生成脚本、数据管线（缩放重映射、锚点渲染）与基准评测脚本（eval_api.py 调用 API 对 ChartP 标注评测）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 像素引导反馈回路：预测锚点→渲染→检查→修正解析
- 提供图表生成、数据管线与基准评测三部分脚本
- 评测脚本以 JSON 标注与图像文件夹为输入输出解析结果

## 适用场景

- 复现论文的图表解析方法与基准评测
- 生成图表数据并构建训练/评测管线
- 在 ChartP 数据集上运行 API 评测

## 场景标签

`文档解析` · 领域:知识与检索

## 证据(README 行号)

> L1: 🏆 ICLR 2026
> L16:  Visual Self-Refine (VSR) turns chart parsing into a pixel-guided feedback loop: predict anchors, render them, insp
> L42: ### Benchmark evaluation

## 星数曲线

```mermaid
xychart-beta
    title "InternLM/VSR 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-18 35 → 2026-10-29 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `c0b2fc131647` · [字段定义](../../DATASET.md)*
