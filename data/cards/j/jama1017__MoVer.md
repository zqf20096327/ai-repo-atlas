# jama1017/MoVer

⭐ 41 · Python · Apache-2.0 · 推送 2026-10-23 · [GitHub](https://github.com/jama1017/MoVer) · [官网](https://mover-dsl.github.io/) · 个人维护

**面向动效动画的一阶逻辑验证 DSL 及 LLM 生成管线**

SIGGRAPH 2025 论文 MoVer 的官方实现：提供基于一阶逻辑的领域特定语言，验证动画是否满足各类时空运动性质；可作为 LLM 动效生成管线中的验证环节，含动画合成、MoVer 程序合成与验证三部分。另含转换器，可将 GSAP HTML/SVG 动画抽取为 JSON 并渲染为 PNG/SVG/MP4/GIF。提供 5,600 条 prompt 数据集与自建数据集脚本，通过 LiteLLM 支持云端与本地 LLM，渲染依赖 Chromium，MP4/GIF 导出需 FFmpeg。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 基于一阶逻辑的时空性质验证 DSL（含 not 谓词消解重复对象引用）
- LLM 动效生成管线：动画合成、程序合成、验证三阶段，YAML 配置驱动
- mover-convert 将 GSAP HTML 转为采样 JSON 及 MP4/GIF/PNG/SVG 输出
- 5,600 条 prompt 数据集与自建数据集生成脚本

## 适用场景

- 在 LLM 生成动效动画后自动验证是否满足描述的时空性质
- 把 GSAP 动画转为 JSON 数据或导出为视频/帧序列
- 构建或复用论文的动效 prompt 数据集做评测

## 场景标签

 · 领域:图形学/动画验证

## 证据(README 行号)

> L14: This repository contains the official implementation of MoVer, a domain-specific language based on first-order logi
> L63: Both installations support cloud and local LLMs through LiteLLM. Chromium

## 星数曲线

```mermaid
xychart-beta
    title "jama1017/MoVer 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 39 --> 42
    line [40, 41, 41]
```

2026-10-18 40 → 2026-10-29 41（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `e81cc7c21b8a` · [字段定义](../../DATASET.md)*
