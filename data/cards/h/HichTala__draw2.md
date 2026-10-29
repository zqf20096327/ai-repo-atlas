# HichTala/draw2

⭐ 82 · Python · AGPL-3.0 · 推送 2026-10-27 · [GitHub](https://github.com/HichTala/draw2) · 个人维护

**在图像/视频中检测识别 Yu-Gi-Oh! 卡牌的目标检测器**

DRAW 2 是一个用于检测并识别 Yu-Gi-Oh! 卡牌的目标检测模型，支持图像、视频与摄像头输入，面向对战直播等场景；可通过 ydk 卡组文件提高识别效果，并以多语言显示卡名。提供 OBS 第三方插件，使直播者无需技术背景即可在直播中实时展示检测到的卡牌；仓库本身面向有编程基础的用户，通过 git clone 后 pip 安装使用。项目采用 AGPL-3.0 许可，模型识别 13k+ 种卡牌。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测并识别图像/视频/摄像头中的 Yu-Gi-Oh! 卡牌
- 提供 OBS 第三方插件，直播中实时展示检测到的卡牌
- 支持 ydk 卡组文件提升识别效果，卡名支持 EN/FR/IT/DE/PT 五种语言

## 适用场景

- 直播对战中实时展示我方场上卡牌供观众阅读
- 从录像或截图中批量识别出现的卡牌
- 在 OBS 中集成卡牌检测叠加显示

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L18: DRAW 2 (which stands for **D**etect and **R**ecognize **A** **W**ide range of cards version 2) is an object detecto
> L19: trained to detect _Yu-Gi-Oh!_ cards in all types of images, and in particular in dueling images.

## 星数曲线

```mermaid
xychart-beta
    title "HichTala/draw2 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-29"]
    y-axis "stars" 80 --> 83
    line [81, 82, 82]
```

2026-10-18 81 → 2026-10-29 82（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `f30dd8710669` · [字段定义](../../DATASET.md)*
