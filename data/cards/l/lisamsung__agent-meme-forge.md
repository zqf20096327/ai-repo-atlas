# lisamsung/agent-meme-forge

⭐ 98 · Python · MIT · 推送 2026-09-04 · [GitHub](https://github.com/lisamsung/agent-meme-forge) · [官网](https://lisamsung.github.io/agent-meme-forge/) · 个人维护 · 中文 README

**把一张图或文字概念做成可发送的微信表情包的 Codex 技能**

面向 Codex/Claude 类 agent 的技能包：输入参考图或文字概念，经计划（JSON）→图像模型每张贴纸只画 4 张关键姿势→本地确定性渲染器插值 16 帧 240×240 GIF→打包为符合微信表情开放平台规格的 16/24 张套装。设有 sendability_gate（复用触发、情绪价值、创意钩、视觉梗）四道门槛，模型不绘制中文文字，字幕由本地排版。附 Playwright+Edge 提交流程手册。限制：需自备图像生成模型；商用提交前需自行复核微信平台规则。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 4 关键姿势→本地插值 16 帧的确定性渲染管线
- sendability_gate 四项门槛约束计划产出
- 微信规格打包（240×240<500KB、缩略图、封面、清单）
- QC 含棋盘格检测、边缘触碰、道具闪烁、面部漂移等检查

## 适用场景

- 为自己的微信形象生成一套可上传的表情包
- 用文字概念快速产出中文梗图贴纸套装
- 按微信开放平台规格批量导出并提交审核

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L3: > **没人用的表情包就是垃圾。** A Codex skill that turns one reference image — or a text concept — into a WeChat-ready animated C
> L36:    or text concept    ├──▶  plan ──▶  4 keyposes  ──▶  16-frame GIF  ──▶  WeChat upload pack
> L37:    + persona + style  ┘    (JSON)   (one image_gen      (local render,         (24 items,

## 星数曲线

```mermaid
xychart-beta
    title "lisamsung/agent-meme-forge 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-25"]
    y-axis "stars" 97 --> 106
    line [105, 98, 98]
```

2026-10-18 105 → 2026-10-25 98（-7）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `497cd7eec579` · [字段定义](../../DATASET.md)*
